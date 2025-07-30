<template>
  <div class="dashboard">
    <header class="navbar">
      <router-link to="/"><div class="logo">XLR8<span class="logo-accent">ai</span></div></router-link>
      <router-link class="experiment-button" to="/experiment">+ New Experiment</router-link>
    </header>

    <main class="cards-container">
      <div v-for="(exp, id) in aiResults" :key="id" class="experiment-card">
        <h2 class="card-title">{{ exp.experiment_name }}</h2>
        <p class="card-subtitle">{{ exp.experiment_time }}</p>

        <div class="card-content">
          <div class="chart-section">
            <canvas :id="'chart-' + id"></canvas>
          </div>
          <div class="reasons-section">
            <h4>Reasons for Rankings</h4>
            <ul>
              <li v-for="(categories, brand) in exp.results" :key="brand">
                <strong>{{ brand }}:</strong>
                <ul>
                  <li v-for="(rank, category) in categories" :key="category">
                    {{ category }} → Rank {{ rank }}
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'

export default {
  name: 'DashboardView',
  data () {
    return {
      aiResults: {},
      charts: {}
    }
  },
  async mounted () {
    await this.getData()
    this.$nextTick(() => {
      this.renderCharts()
    })
  },
  methods: {
    async getData () {
      try {
        const response = await fetch('https://xlr8-take-home.onrender.com/api/dashbord-card')
        if (!response.ok) {
          throw new Error('Network error')
        }
        const data = await response.json()
        this.aiResults = data
      } catch (error) {
        console.error('Fetch error:', error)
      }
    },
    renderCharts () {
      for (const [id, exp] of Object.entries(this.aiResults)) {
        const brands = Object.keys(exp.results)
        const avgRanks = brands.map(b => {
          const vals = Object.values(exp.results[b])
          const sum = vals.reduce((a, b) => a + b, 0)
          return (sum / vals.length).toFixed(2)
        })

        const ctx = document.getElementById(`chart-${id}`)
        if (ctx) {
          this.charts[id] = new Chart(ctx, {
            type: 'bar',
            data: {
              labels: brands,
              datasets: [{
                label: 'Avg Rank (lower = better)',
                data: avgRanks,
                backgroundColor: ['#c084fc', '#60a5fa', '#34d399']
              }]
            },
            options: {
              responsive: true,
              plugins: {
                legend: { display: false },
                title: {
                  display: false
                }
              },
              scales: {
                y: {
                  beginAtZero: true,
                  reverse: false,
                  title: {
                    display: true,
                    text: 'Avg. Rank',
                    color: '#aaa'
                  }
                },
                x: {
                  ticks: { color: '#ccc' }
                }
              }
            }
          })
        }
      }
    }
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body, html, .dashboard {
  background-color: #000;
  color: #f1f1f1;
  font-family: 'Inter', 'Segoe UI', sans-serif;
  min-height: 100vh;
}

.navbar {
  background: #0d0d0d;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #222;
}

.logo {
  font-size: 1.8rem;
  font-weight: bold;
  color: white;
}

.logo-accent {
  color: #c084fc;
}

.experiment-button {
  background: transparent;
  border: 1px solid #c084fc;
  color: #c084fc;
  text-decoration: none;
  padding: 0.6rem 1rem;
  border-radius: 6px;
  font-weight: 500;
  transition: background 0.3s ease;
}

.experiment-button:hover {
  background: #c084fc;
  color: #000;
}

.cards-container {
  padding: 2rem;
  display: grid;
  gap: 2rem;
  grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
}

.experiment-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid #222;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 0 20px rgba(192, 132, 252, 0.1);
  backdrop-filter: blur(8px);
  transition: 0.3s ease;
}

.experiment-card:hover {
  border-color: #c084fc;
  box-shadow: 0 0 25px rgba(192, 132, 252, 0.3);
}

.card-title {
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 0.3rem;
}

.card-subtitle {
  font-size: 0.85rem;
  color: #999;
  margin-bottom: 1.2rem;
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.chart-section canvas {
  width: 100%;
  height: 300px !important;
}

.reasons-section {
  font-size: 0.92rem;
}

.reasons-section h4 {
  margin-bottom: 0.5rem;
  color: #c084fc;
}

.reasons-section ul {
  list-style: none;
  padding-left: 0;
}

.reasons-section li {
  margin-bottom: 0.5rem;
  color: #ccc;
}
</style>
