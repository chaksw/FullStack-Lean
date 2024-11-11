import { createApp } from 'vue'
// import './style.css'
import './assets/index.css'

import router from "./router";
import App from './App.vue'
const app = createApp(App)
app.use(router)
createApp(App).mount('#app')
