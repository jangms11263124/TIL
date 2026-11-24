<template>
  <div class="dashboard-card">
    <div class="card-header">
      <h2>데이터 조회 및 구조 분석</h2>
      <span class="req-badge">F307</span>
    </div>
    
    <p class="card-text">
      선택한 데이터셋: <strong class="text-highlight">finance_economy.jsonl</strong> (10,000건)
    </p>
    <p class="card-text">
      <strong>선택 이유:</strong> 10,000개의 고유 종목별 1일 주가 정보(시가, 종가, 고가, 저가, 거래량, 시가총액)가 포함된 정형 데이터셋으로, 기업들의 시가총액 대비 거래량 비교, 시장 전반의 가격대별 분포(Distribution), 월별 거래 트렌드(Trend) 등 거시적 금융 데이터를 시각화하고 인사이트를 도출하기에 매우 적합하여 선정하였습니다.
    </p>

    <div style="overflow-x: auto; margin-top: 12px;">
      <table class="schema-table">
        <thead>
          <tr>
            <th>필드명</th>
            <th>타입</th>
            <th>설명</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="code-badge">name</span></td>
            <td>String</td>
            <td>금융/경제 상품 또는 기업의 이름</td>
          </tr>
          <tr>
            <td><span class="code-badge">code</span></td>
            <td>String</td>
            <td>종목을 식별하는 6자리 고유 번호</td>
          </tr>
          <tr>
            <td><span class="code-badge">date</span></td>
            <td>String</td>
            <td>주가 데이터가 기록된 거래일 (YYYY-MM-DD)</td>
          </tr>
          <tr>
            <td><span class="code-badge">open / close</span></td>
            <td>Number</td>
            <td>해당 거래일의 시가(Open) 및 종가(Close)</td>
          </tr>
          <tr>
            <td><span class="code-badge">high / low</span></td>
            <td>Number</td>
            <td>해당 거래일의 최고가(High) 및 최저가(Low)</td>
          </tr>
          <tr>
            <td><span class="code-badge">volume</span></td>
            <td>Number</td>
            <td>해당 거래일의 총 주식 거래량</td>
          </tr>
          <tr>
            <td><span class="code-badge">market_cap_krw</span></td>
            <td>Number</td>
            <td>해당 기업의 시가총액 (원화 기준)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DataInfo'
}
</script>
