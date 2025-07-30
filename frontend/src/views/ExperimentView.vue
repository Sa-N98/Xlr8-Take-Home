<template>
  <header class="navbar">
      <router-link  to="/"><div class="logo">Brand Ranker</div></router-link>
      <router-link class="demo-button" to="/dashboard">Experiments Dashboard</router-link>
  </header>
  <div class="experiments">
    <h1>Create New <span>Brand Ranking</span></h1>
    <p>Compare up to {{ maxBrands }} brands across up to {{ maxCategories }} categories using AI analysis</p>
    <form @submit.prevent>
      <div id="Brand form">
        <h1>Brands ({{ brands.filter(brand => brand.trim() !== '').length }}/{{ maxBrands }})</h1>
        <p>Enter the brands you want to compare</p>
        <div v-for="(brand, index) in brands" :key="index" class="brand-input-group">
          <input v-model="brands[index]" type="text" :placeholder="'Brand ' + (index + 1)" required />
          <button type="button" v-if="brands.length > 1" @click="removeBrand(index)">Remove</button>
        </div>
        <button type="button" @click="addBrand" v-if="brands.length <maxBrands"> Add Brand</button>
      </div>
      <div id="Category form">
        <h1>Categories ({{ categories.filter(category => category.trim() !== '').length }}/{{ maxCategories }})</h1>
        <p>Enter the categories you want to compare</p>
        <div v-for="(category, index) in categories" :key="index" class="category-input-group">
          <input v-model="categories[index]" type="text" :placeholder="'Category ' + (index + 1)" required />
          <button type="button" v-if="categories.length > 1" @click="removeCategory(index)">Remove</button>
        </div>
        <button type="button" @click="addCategory" v-if="categories.length < maxCategories"> Add Category</button>
      </div>
    </form>
    <button type="submit" @click="sendData" class="submit-button">Start Ranking</button>
    <br><br>
    <div v-if="Object.keys(aiResults).length" class="ai-results">
      <h2>AI Ranking Results</h2>
      <div v-for="(categoryData, category) in aiResults" :key="category">
        <h3>{{ category }}</h3>
        <ol>
          <li v-for="(entry, rank) in categoryData" :key="rank">
            <strong>#{{ rank }} {{ entry.brand }}</strong>: Reason: {{ entry.reason }}
          </li>
        </ol>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ExperimentView',
  data () {
    return {
      brands: [''],
      maxBrands: 5,
      categories: [''],
      maxCategories: 3,
      aiResults: {}
    }
  },
  methods: {
    addBrand () {
      if (this.brands.length < this.maxBrands) {
        this.brands.push('')
      }
    },
    removeBrand (index) {
      if (this.brands.length > 1) {
        this.brands.splice(index, 1)
      }
    },
    addCategory () {
      if (this.categories.length < this.maxCategories) {
        this.categories.push('')
      }
    },
    removeCategory (index) {
      if (this.categories.length > 1) {
        this.categories.splice(index, 1)
      }
    },
    async sendData () {
      const filledBrands = this.brands.filter(b => b.trim() !== '')
      const filledCategories = this.categories.filter(c => c.trim() !== '')
      // Logic to send data to the backend
      if (filledBrands.length === this.brands.length && filledCategories.length === this.categories.length) {
        // All inputs are valid
        console.log('Brands:', filledBrands)
        console.log('Categories:', filledCategories)
        // Add backend logic here
        try {
          const result = await fetch('http://localhost:5000/api/rank-brands', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              brands: filledBrands,
              category: filledCategories
            })
          })
          const data = await result.json()
          if (result.ok) {
            console.log('AI Results:', data.results)
            this.aiResults = JSON.parse(JSON.stringify(data.results))
            console.log('data vue', this.aiResults)
            console.log(`Results for category "${filledCategories}":`, data)
          } else {
            alert(data.error || 'Something went wrong.')
            throw new Error(`HTTP error! status: ${result.status}`)
          }
        } catch (err) {
          console.error(`Error for category "${filledCategories}":`, err)
        }
      } else {
        alert('Please fill out all brand and category fields before submitting.')
      }
    }
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
/* Navbar */
.navbar {
  background-color: #000;
  color: white;
  padding: 20px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #1f2937;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
  font-family: "Segoe UI", Roboto, Arial, sans-serif;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  color: #ffffff;
}

.demo-button {
  padding: 10px 20px;
  background-color: transparent;
  border: 1px solid #ffffff;
  border-radius: 8px;
  color: #fafafa;
  font-weight: bold;
  text-decoration: none;
  transition: all 0.3s ease;
}

.demo-button:hover {
  background-color: #ffffff;
  color: black;
}

.experiments {
  min-height: 100vh;
  background-color: #000;
  color: #fff;
  font-family: "Segoe UI", Roboto, Arial, sans-serif;
  padding: 40px 20px;
  text-align: center;
}

.experiments h1 {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 10px;
}

.experiments h1 span,
.experiments h1 strong {
  background: linear-gradient(90deg, #a855f7, #9495fd);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.experiments > p {
  font-size: 16px;
  color: #ccc;
  margin-bottom: 40px;
}

/* Form layout */
form {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 40px;
}

#Brand\ form,
#Category\ form {
  background-color: #111827;
  padding: 30px;
  border-radius: 10px;
  width: 100%;
  max-width: 400px;
  text-align: left;
  box-shadow: 0 0 0 1px #1f2937;
}

#Brand\ form h1,
#Category\ form h1 {
  font-size: 20px;
  color: #fff;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

#Brand\ form p,
#Category\ form p {
  font-size: 14px;
  color: #9ca3af;
  margin-bottom: 20px;
}

.brand-input-group,
.category-input-group {
  display: flex;
  align-items: center;
  margin-bottom: 12px;
}

.brand-input-group input,
.category-input-group input {
  flex: 1;
  padding: 12px 16px;
  background-color: #1f2937;
  border: 1px solid #374151;
  border-radius: 6px;
  color: #fff;
  outline: none;
  font-size: 14px;
  transition: border-color 0.3s;
}

input::placeholder {
  color: #6b7280;
}

.brand-input-group button,
.category-input-group button {
  background: none;
  border: none;
  color: #f87171;
  margin-left: 10px;
  font-size: 16px;
  cursor: pointer;
  transition: color 0.2s;
}

.brand-input-group button:hover,
.category-input-group button:hover {
  color: #f43f5e;
}

button[type="button"] {
  width: 100%;
  background-color: transparent;
  border: 1px solid #a855f7;
  color: #a855f7;
  padding: 10px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}

button[type="button"]:hover {
  background: #a855f7;
  color: black;
}

/* Submit Button */
.submit-button {
  margin-top: 40px;
  background: #a855f7;
  color: white;
  padding: 12px 30px;
  border: none;
  font-size: 16px;
  font-weight: bold;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.submit-button:hover {
  background: #9333ea;
}
/* Results */

.ai-results {
  background-color: #111827;
  padding: 1.5rem;
  border-radius: 12px;
  margin-top: 2rem;
  color: #f0f0f0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  width: 80%;
  display: inline-grid
}

.ai-results h2 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: #9f7aea; /* Purple accent */
}

.ai-results h3 {
  font-size: 1.3rem;
  margin-top: 1.2rem;
  color: #63b3ed; /* Blue accent */
  border-bottom: 1px solid #333;
  padding-bottom: 0.3rem;
}

.ai-results ol {
  margin-left: 1.2rem;
  margin-top: 0.5rem;
  padding-left: 1rem;
}

.ai-results li {
  background-color: #2d2d44;
  padding: 0.7rem 1rem;
  margin: 0.4rem 0;
  border-radius: 8px;
  line-height: 1.5;
  list-style: decimal;
  border-left: 4px solid #9f7aea;
  transition: background 0.3s ease;
}

.ai-results li:hover {
  background-color: #3b3b5c;
}

.ai-results strong {
  color: #fbd38d; /* Gold accent for ranking */
}

</style>
