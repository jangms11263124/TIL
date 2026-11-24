<template>
  <div class="dashboard-card" style="grid-column: span 2;">
    <div class="card-header">
      <h2>시각화 결과 해석 및 인사이트</h2>
      <span class="req-badge">F310</span>
    </div>
    
    <div class="insights-section">
      <div class="insight-block">
        <h3>차트 설계 의도 (Chart Design Intention)</h3>
        <p>
          주식 시장 데이터 분석을 위해 각기 다른 세 가지 관점의 차트를 설계했습니다.
          첫째, <strong>시가 vs 종가 비교 차트 (F308)</strong>는 특정 기업들의 하루 동안의 가격 변동성과 방향성(음봉/양봉)을 한눈에 비교할 수 있도록 그룹화된 막대형(Grouped Bar)으로 구성했습니다.
          둘째, <strong>월별 시장 추이 차트 (F309)</strong>는 개별 기업이 아닌 전체 10,000개 종목을 월별로 집계하여 시장 전반의 평균 가격대와 전체 거래량의 거시적인 계절성 및 흐름을 보여주고자 선형(Line) 및 면적형(Area) 차트를 복합 구성했습니다.
          셋째, <strong>시가총액 분포 차트 (F309)</strong>는 기업들의 규모별 비중을 5가지 범주로 구간화하여 대다수 기업들의 분포 상태(중소형주 비중 등)를 직관적으로 파악할 수 있는 빈도 분포 막대형 차트로 설계했습니다.
        </p>
      </div>

      <div class="insight-block">
        <h3>데이터 가공 방식 (Data Preprocessing)</h3>
        <p>
          원시 데이터 <code>finance_economy.jsonl</code>을 동적으로 Fetch하여 개별 라인을 JSON 객체로 파싱하고, 텍스트 형태의 수치들을 정수 및 실수형으로 타입 변환했습니다.
          시가총액 비교를 위해 기업들을 시가총액 기준으로 내림차순 정렬하여 상위 N개 기업을 선택하고 시가와 종가 데이터를 연결했습니다.
          월별 추이를 위해 각 행의 <code>date</code> 필드에서 연-월을 추출하여 월별로 그룹화한 뒤, 각 월에 해당하는 종가의 평균과 거래량의 총합을 연산했습니다.
          시가총액 분포를 위해 원화 기준 시가총액(<code>market_cap_krw</code>)을 1조 원 미만, 1조~10조 원, 10조~50조 원, 50조~100조 원, 100조 원 이상의 5개 구간으로 분류하는 빈도 카운팅 로직을 구현했습니다.
        </p>
      </div>

      <div class="insight-block">
        <h3>시각화 결과 해석 및 인사이트 (Interpretation & Insights)</h3>
        <p>
          <strong>1) 시가 vs 종가 분석:</strong> 대형주 위주의 시가 대비 종가 변동은 비교적 안정적인 흐름을 보입니다. 대규모 시가총액을 지닌 종목일수록 시가와 종가의 갭이 적어 하루 중 급등락 폭이 상대적으로 제한적임을 알 수 있습니다.<br>
          <strong>2) 월별 거래량과 평균 가격의 반비례 관계:</strong> 월별 추이 분석 결과, 특정 월에 평균 종가가 상승할 때 거래량은 수렴하거나 감소하는 경향을 보여, 시장의 고점 부근에서는 거래가 둔화되고 저점에서 거래가 활발해지는 일반적인 시장의 특성을 간접적으로 반영하고 있습니다.<br>
          <strong>3) 시장 분포의 양극화:</strong> 시가총액 분포 분석을 통해 전체 10,000개 기업 중 대부분의 기업이 1조 원 ~ 10조 원 구간에 밀집해 있는 반면, 100조 원 이상의 초대형주는 극소수에 불과해 시장의 시가총액 규모가 전형적인 롱테일(Long-tail) 형태를 띠며 양극화가 뚜렷함을 확인할 수 있습니다.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResultInterpretation'
}
</script>
