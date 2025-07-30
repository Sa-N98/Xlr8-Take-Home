import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

/* Font Awesome Setup */
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// Choose icons you need
import { faBolt, faChartLine, faChartBar, faUsers } from '@fortawesome/free-solid-svg-icons'
import { faGithub, faGoogle } from '@fortawesome/free-brands-svg-icons' // if needed

// Add icons to the library
library.add(faBolt, faChartLine, faChartBar, faUsers, faGithub, faGoogle)

// Register FontAwesomeIcon globally
const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.use(store)
app.mount('#app')
