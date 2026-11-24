<template>
  <div class="dashboard-card">
    <div class="card-header">
      <h2>월별 시장 추이 (평균 종가 & 거래량)</h2>
      <span class="req-badge">F309</span>
    </div>
    <div class="card-body">
      <div v-if="!trendData || trendData.length === 0" style="display: flex; justify-content: center; align-items: center; height: 100%;">
        데이터를 계산하는 중입니다...
      </div>
      <canvas v-else ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import Chart from 'chart.js/auto'

export default {
  name: 'TrendChart',
  props: {
    trendData: {
      type: Array,
      required: true
    }
  },
  setup(props) {
    const chartCanvas = ref(null)
    let chartInstance = null

    const createChart = () => {
      if (!chartCanvas.value) return

      if (chartInstance) {
        chartInstance.destroy()
      }

      const labels = props.trendData.map(d => d.month)
      const avgPrices = props.trendData.map(d => d.avgClose)
      const totalVolumes = props.trendData.map(d => d.totalVolume)

      chartInstance = new Chart(chartCanvas.value, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: '평균 종가 (원)',
              data: avgPrices,
              borderColor: '#fb7185', // rose
              backgroundColor: '#fb7185',
              yAxisID: 'yPrice',
              tension: 0.3,
              borderWidth: 2,
              pointRadius: 4,
              pointBackgroundColor: '#fb7185'
            },
            {
              label: '총 거래량 (주)',
              data: totalVolumes,
              borderColor: 'rgba(56, 189, 248, 0.4)', // transparent blue
              backgroundColor: 'rgba(56, 189, 248, 0.15)',
              yAxisID: 'yVolume',
              tension: 0.3,
              fill: true,
              borderWidth: 1.5,
              pointRadius: 2
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'top',
              labels: {
                color: '#f8fafc'
              }
            },
            tooltip: {
              mode: 'index',
              intersect: false
            }
          },
          scales: {
            x: {
              grid: {
                color: '#334155'
              },
              ticks: {
                color: '#94a3b8'
              }
            },
            yPrice: {
              type: 'linear',
              position: 'left',
              grid: {
                color: '#334155'
              },
              ticks: {
                color: '#94a3b8',
                callback: function(value) {
                  return value.toLocaleString() + ' 원'
                }
              },
              title: {
                display: true,
                text: '평균 종가',
                color: '#f8fafc'
              }
            },
            yVolume: {
              type: 'linear',
              position: 'right',
              grid: {
                drawOnChartArea: false // prevent grid lines overlap
              },
              ticks: {
                color: '#94a3b8',
                callback: function(value) {
                  if (value >= 1e9) return (value / 1e9).toFixed(1) + 'B'
                  if (value >= 1e6) return (value / 1e6).toFixed(1) + 'M'
                  if (value >= 1e3) return (value / 1e3).toFixed(1) + 'K'
                  return value.toLocaleString()
                }
              },
              title: {
                display: true,
                text: '총 거래량',
                color: '#f8fafc'
              }
            }
          }
        }
      })
    }

    onMounted(() => {
      createChart()
    })

    onBeforeUnmount(() => {
      if (chartInstance) {
        chartInstance.destroy()
      }
    })

    watch(() => props.trendData, () => {
      createChart()
    }, { deep: true })

    return {
      chartCanvas
    }
  }
}
</script>
