// 1. 从 vue 中引入 createApp
import { createApp } from "vue";
// 2. 从一个单文件组件中导入根组件 App
import App from "./App.vue";
import Header from "./pages/Header.vue";
// 3. 创建一个 app 实例对象
// 4. 一个 Vue 项目当中，有且只有一个 Vue 的实例对象
const app = createApp(App);
// Global Registration, define among const app =  createApp(App) & app.mount('#app')
app.component("Header", Header);
// 5. 将 app 对象挂载到 #app 容器当中
app.mount("#app");
