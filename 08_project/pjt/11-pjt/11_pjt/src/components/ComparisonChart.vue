<template>
  <div class="dashboard-card">
    <div class="card-header">
      <h2>시가(Open) vs 종가(Close) 지표 비교</h2>
      <span class="req-badge">F308</span>
    </div>
    <div class="card-body">
      <div v-if="!companies || companies.length === 0" style="display: flex; justify-content: center; align-items: center; height: 100%;">
        데이터를 불러오는 중입니다...
      </div>
      <canvas v-else ref="chartCanvas"></canvas>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import Chart from 'chart.js/auto'

export default {
  name: 'ComparisonChart',
  props: {
    companies: {
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

      const labels = props.companies.map(c => c.name)
      const openPrices = props.companies.map(c => c.open)
      const closePrices = props.companies.map(c => c.close)

      chartInstance = new Chart(chartCanvas.value, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              label: '시가 (Open)',
              data: openPrices,
              backgroundColor: '#38bdf8', // accent-blue
              borderColor: '#38bdf8',
              borderWidth: 1,
              barPercentage: 0.6,
              categoryPercentage: 0.8
            },
            {
              label: '종가 (Close)',
              data: closePrices,
              backgroundColor: '#fb7185', // accent-rose
              borderColor: '#fb7185',
              borderWidth: 1,
              barPercentage: 0.6,
              categoryPercentage: 0.8
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
                color: '#f8fafc',
                font: {
                  family: 'Inter, sans-serif'
                }
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
                color: '#94a3b8',
                font: {
                  size: 10
                }
              }
            },
            y: {
              grid: {
                color: '#334155'
              },
              ticks: {
                color: '#94a3b8',
                callback: function(value) {
                  return value.toLocaleString() + ' 원'
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

    watch(() => props.companies, () => {
      createChart()
    }, { deep: true })

    return {
      chartCanvas
    }
  }
}
</script>
