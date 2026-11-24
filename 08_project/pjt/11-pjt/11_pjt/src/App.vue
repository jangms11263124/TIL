<template>
  <div class="app-container">
    <header class="dashboard-header">
      <div class="dashboard-title">
        <h1>금융·경제 상품 시각화 대시보드</h1>
        <p>finance_economy.jsonl 데이터셋 분석 (F307 ~ F312)</p>
      </div>
      <div>
        <span class="req-badge" style="padding: 6px 12px; font-size: 0.85rem; font-weight: 600;">Interactive Dashboard</span>
      </div>
    </header>

    <!-- Loading State -->
    <div v-if="isLoading" style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 300px; gap: 16px;">
      <div style="font-size: 1.2rem; font-weight: 500; color: var(--accent-blue);">데이터셋 로딩 및 가공 중...</div>
      <div style="font-size: 0.9rem; color: var(--text-secondary);">총 10,000건의 거래 데이터를 파싱하고 있습니다.</div>
    </div>

    <div v-else>
      <!-- Stats Summary cards -->
      <section class="stats-grid">
        <div class="stat-card">
          <span class="stat-label">분석 대상 기업 수</span>
          <span class="stat-value">{{ formatNumber(filteredCompanies.length) }} 개</span>
        </div>
        <div class="stat-card">
          <span class="stat-label">평균 주가 (종가 기준)</span>
          <span class="stat-value">{{ formatNumber(Math.round(stats.avgClose)) }} 원</span>
        </div>
        <div class="stat-card">
          <span class="stat-label">총 거래량</span>
          <span class="stat-value">{{ formatVolume(stats.totalVolume) }} 주</span>
        </div>
        <div class="stat-card">
          <span class="stat-label">최고 시가총액</span>
          <span class="stat-value">{{ formatMarketCap(stats.maxMarketCap) }}</span>
        </div>
      </section>

      <!-- F312 Interactive Control Panel -->
      <section class="controls-panel">
        <!-- Search Input -->
        <div class="control-group">
          <label for="search">종목 검색 (명칭 또는 코드)</label>
          <input 
            type="text" 
            id="search" 
            v-model="searchQuery" 
            placeholder="예: 솔라케미칼, 171583" 
            class="control-input"
          />
        </div>

        <!-- Top N Slider -->
        <div class="control-group">
          <label for="topN">비교 종목 수 (Top N 시가총액): {{ topN }}개</label>
          <div class="control-slider">
            <input 
              type="range" 
              id="topN" 
              v-model.number="topN" 
              min="5" 
              max="30" 
              step="1"
            />
          </div>
        </div>

        <!-- Min Market Cap Slider -->
        <div class="control-group" style="flex: 2;">
          <label for="minCap">최소 시가총액 필터: {{ formatMarketCap(minMarketCap * 1e12) }} 이상</label>
          <div class="control-slider">
            <input 
              type="range" 
              id="minCap" 
              v-model.number="minMarketCap" 
              min="0" 
              max="1500" 
              step="50"
            />
          </div>
        </div>
      </section>

      <!-- Search Detail Panel (F312 Action Detail) -->
      <section v-if="searchResult" class="dashboard-card" style="margin-bottom: 24px; border-color: var(--accent-blue);">
        <div class="card-header">
          <h2 style="color: var(--accent-blue);">🔍 종목 상세 조회</h2>
          <span class="req-badge" style="background-color: rgba(56, 189, 248, 0.2); color: var(--accent-blue);">F312</span>
        </div>
        <div class="card-body" style="min-height: auto;">
          <div class="detail-grid">
            <div class="detail-item">
              <div class="detail-label">종목명</div>
              <div class="detail-value" style="color: var(--accent-blue);">{{ searchResult.name }}</div>
            </div>
            <div class="detail-item">
              <div class="detail-label">종목코드</div>
              <div class="detail-value">{{ searchResult.code }}</div>
            </div>
            <div class="detail-item">
              <div class="detail-label">기준 거래일</div>
              <div class="detail-value">{{ searchResult.date }}</div>
            </div>
            <div class="detail-item">
              <div class="detail-label">시가총액</div>
              <div class="detail-value">{{ formatMarketCap(searchResult.market_cap_krw) }} ({{ formatNumber(searchResult.market_cap_krw) }} 원)</div>
            </div>
            <div class="detail-item">
              <div class="detail-label">주가 범위 (시가 / 종가 / 고가 / 저가)</div>
              <div class="detail-value">
                {{ formatNumber(searchResult.open) }} / {{ formatNumber(searchResult.close) }} / {{ formatNumber(searchResult.high) }} / {{ formatNumber(searchResult.low) }} 원
              </div>
            </div>
            <div class="detail-item">
              <div class="detail-label">거래량</div>
              <div class="detail-value">{{ formatNumber(searchResult.volume) }} 주</div>
            </div>
          </div>
        </div>
      </section>

      <!-- F311 Grid Layout Dashboard -->
      <main class="dashboard-grid">
        <!-- F307 Schema Table -->
        <DataInfo />

        <!-- F308 Comparison Chart -->
        <ComparisonChart :companies="topNCompanies" />

        <!-- F309 Trend Chart -->
        <TrendChart :trendData="monthlyTrend" />

        <!-- F309 Distribution Chart -->
        <DistChart :distributionData="marketCapDistribution" />

        <!-- F310 Interpretation & Insights -->
        <ResultInterpretation />
      </main>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import DataInfo from './components/DataInfo.vue'
import ComparisonChart from './components/ComparisonChart.vue'
import TrendChart from './components/TrendChart.vue'
import DistChart from './components/DistChart.vue'
import ResultInterpretation from './components/ResultInterpretation.vue'

export default {
  name: 'App',
  components: {
    DataInfo,
    ComparisonChart,
    TrendChart,
    DistChart,
    ResultInterpretation
  },
  setup() {
    const allCompanies = ref([])
    const isLoading = ref(true)

    // Interactive inputs (F312)
    const searchQuery = ref('')
    const topN = ref(10)
    const minMarketCap = ref(0) // In Trillion KRW (10^12)

    // Format helpers
    const formatNumber = (val) => {
      return val ? val.toLocaleString() : '0'
    }

    const formatVolume = (val) => {
      if (val >= 1e9) return (val / 1e9).toFixed(2) + ' 십억'
      if (val >= 1e6) return (val / 1e6).toFixed(2) + ' 백만'
      return formatNumber(val)
    }

    const formatMarketCap = (val) => {
      if (!val) return '0 원'
      const trillion = val / 1e12
      if (trillion >= 1.0) {
        return trillion.toFixed(2) + ' 조 원'
      }
      const billion = val / 1e8
      return billion.toFixed(2) + ' 억 원'
    }

    // Load and Parse JSONL Data
    const loadData = async () => {
      try {
        const response = await fetch('/finance_economy.jsonl')
        const text = await response.text()
        const lines = text.split('\n')
        
        const parsedData = []
        for (const line of lines) {
          if (!line.trim()) continue
          try {
            const item = JSON.parse(line)
            parsedData.push({
              name: item.name,
              code: item.code,
              date: item.date,
              open: Number(item.open),
              close: Number(item.close),
              high: Number(item.high),
              low: Number(item.low),
              volume: Number(item.volume),
              market_cap_krw: Number(item.market_cap_krw)
            })
          } catch (e) {
            console.error('Failed to parse line:', line, e)
          }
        }
        allCompanies.value = parsedData
      } catch (err) {
        console.error('Error fetching/parsing finance data:', err)
      } finally {
        isLoading.value = false
      }
    }

    onMounted(() => {
      loadData()
    })

    // Filtered list by Market Cap (F312 dynamic reactivity)
    const filteredCompanies = computed(() => {
      const minCapBytes = minMarketCap.value * 1e12
      return allCompanies.value.filter(c => c.market_cap_krw >= minCapBytes)
    })

    // Top N companies by Market Cap for Comparison Chart
    const topNCompanies = computed(() => {
      return [...filteredCompanies.value]
        .sort((a, b) => b.market_cap_krw - a.market_cap_krw)
        .slice(0, topN.value)
    })

    // Monthly Market Trend (aggregated from all loaded records for global trend)
    const monthlyTrend = computed(() => {
      const groups = {}
      for (const item of allCompanies.value) {
        // e.g. "2024-04-30" -> "2024-04"
        if (!item.date) continue
        const month = item.date.substring(0, 7)
        if (!groups[month]) {
          groups[month] = { sumClose: 0, count: 0, totalVolume: 0 }
        }
        groups[month].sumClose += item.close
        groups[month].count += 1
        groups[month].totalVolume += item.volume
      }

      return Object.keys(groups)
        .sort()
        .map(month => ({
          month: month,
          avgClose: Math.round(groups[month].sumClose / groups[month].count),
          totalVolume: groups[month].totalVolume
        }))
    })

    // Market Capitalization Distribution (F309 distribution - updates dynamically)
    const marketCapDistribution = computed(() => {
      let under1T = 0
      let oneToTenT = 0
      let tenToFiftyT = 0
      let fiftyToHundredT = 0
      let overHundredT = 0

      const oneT = 1e12
      const tenT = 10 * 1e12
      const fiftyT = 50 * 1e12
      const hundredT = 100 * 1e12

      for (const item of filteredCompanies.value) {
        const cap = item.market_cap_krw
        if (cap < oneT) under1T++
        else if (cap < tenT) oneToTenT++
        else if (cap < fiftyT) tenToFiftyT++
        else if (cap < hundredT) fiftyToHundredT++
        else overHundredT++
      }

      return [under1T, oneToTenT, tenToFiftyT, fiftyToHundredT, overHundredT]
    })

    // Search query result
    const searchResult = computed(() => {
      const q = searchQuery.value.trim().toLowerCase()
      if (!q) return null

      return allCompanies.value.find(c => 
        c.name.toLowerCase().includes(q) || 
        c.code.includes(q)
      ) || null
    })

    // Summary stats based on filtered companies
    const stats = computed(() => {
      if (filteredCompanies.value.length === 0) {
        return { avgClose: 0, totalVolume: 0, maxMarketCap: 0 }
      }

      let sumClose = 0
      let totalVolume = 0
      let maxMarketCap = 0

      for (const c of filteredCompanies.value) {
        sumClose += c.close
        totalVolume += c.volume
        if (c.market_cap_krw > maxMarketCap) {
          maxMarketCap = c.market_cap_krw
        }
      }

      return {
        avgClose: sumClose / filteredCompanies.value.length,
        totalVolume,
        maxMarketCap
      }
    })

    return {
      isLoading,
      searchQuery,
      topN,
      minMarketCap,
      filteredCompanies,
      topNCompanies,
      monthlyTrend,
      marketCapDistribution,
      searchResult,
      stats,
      formatNumber,
      formatVolume,
      formatMarketCap
    }
  }
}
</script>
