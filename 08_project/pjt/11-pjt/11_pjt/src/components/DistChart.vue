<template>
  <div class="dashboard-card">
    <div class="card-header">
      <h2>시가총액 규모별 기업 수 분포</h2>
      <span class="req-badge">F309</span>
    </div>
    <div class="card-body">
      <div v-if="!distributionData || distributionData.length === 0" style="display: flex; justify-content: center; align-items: center; height: 100%;">
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
  name: 'DistChart',
  props: {
    distributionData: {
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

      chartInstance = new Chart(chartCanvas.value, {
        type: 'bar',
        data: {
          labels: [
            '1조 원 미만',
            '1조 ~ 10조 원',
            '10조 ~ 50조 원',
            '50조 ~ 100조 원',
            '100조 원 이상'
          ],
          datasets: [
            {
              label: '기업 수 (개)',
              data: props.distributionData,
              backgroundColor: '#34d399', // accent-green
              borderColor: '#34d399',
              borderWidth: 1,
              barPercentage: 0.6
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false // only one dataset, legend is redundant
            },
            tooltip: {
              callbacks: {
                label: function(context) {
                  return `기업 수: ${context.parsed.y.toLocaleString()} 개`
                }
              }
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
            y: {
              grid: {
                color: '#334155'
              },
              ticks: {
                color: '#94a3b8',
                callback: function(value) {
                  return value.toLocaleString() + ' 개'
                }
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

    watch(() => props.distributionData, () => {
      createChart()
    }, { deep: true })

    return {
      chartCanvas
    }
  }
}
</script>
