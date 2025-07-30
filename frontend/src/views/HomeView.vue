<template>
  <div class="homepage">
    <!-- Top Navbar -->
    <header class="navbar">
      <div class="logo">Brand Ranker</div>
      <router-link class="demo-button" to="/">Start Ranking</router-link>
    </header>

    <!-- Hero Section -->
    <main class="hero">
      <h1>
        Get Your Brand Ranked by<br />
        <span class="highlight">AI Intelligence</span>
      </h1>
      <p class="subtext">
        Compare up to 5 brands across 3 categories
        using advanced AI analysis. <br />
        Get data-driven insights to understand your competitive position.
      </p>

      <!-- Icon Section -->
      <div class="icon-bar">
        <div class="icon-circle">
          <font-awesome-icon :icon="['fas', 'bolt']" />
        </div>
        <div class="icon-circle">
          <font-awesome-icon :icon="['fas', 'chart-line']" />
        </div>
        <div class="icon-circle">
          <font-awesome-icon :icon="['fas', 'chart-bar']" />
        </div>
        <div class="icon-circle">
          <font-awesome-icon :icon="['fas', 'users']" />
        </div>
      </div>

      <!-- CTA -->
      <router-link to="/experiment" class="cta">Start Ranking →</router-link>
    </main>
  </div>
</template>

<script>
export default {
  name: 'HomeView'
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.homepage {
  background-color: #000;
  color: #fff;
  min-height: 100vh;
  font-family: "Segoe UI", Roboto, Arial, sans-serif;
}

/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  border-bottom: 1px solid #222;
}

.logo {
  font-size: 24px;
  font-weight: bold;
}

.demo-button {
  padding: 8px 16px;
  border: 1px solid #fff;
  border-radius: 6px;
  text-decoration: none;
  color: white;
  font-weight: bold;
  transition: background 0.3s ease;
}

.demo-button:hover {
  background: white;
  color: black;
}

/* Hero Section */
.hero {
  max-width: 800px;
  margin: 100px auto 0 auto;
  text-align: center;
  padding: 0 20px;
}

.hero h1 {
  font-size: 86px;
  line-height: 1.1;
  margin-bottom: 20px;
}

.highlight {
  background: linear-gradient(90deg, #a855f7, #9495fd);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.subtext {
  font-size: 18px;
  color: #dbdbdb;
  margin-bottom: 40px;
  line-height: 1.6;
}

/* Icon Row */
.icon-bar {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-bottom: 50px;
}

.icon-circle {
  width: 60px;
  height: 60px;
  margin-left: 20px;
  margin-right: 20px;
  border-radius: 50%;
  background-color: #1f2937;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  color: #c084fc;
  transition: background 0.3s ease;
}

.icon-circle:hover {
  background-color: #374151;
}

/* CTA Button */
.cta {
  padding: 12px 28px;
  border: 2px solid white;
  border-radius: 8px;
  text-decoration: none;
  color: white;
  font-weight: bold;
  font-size: 24px;
  transition: all 0.3s ease;
}

.cta:hover {
  background: white;
  color: black;
}
</style>
