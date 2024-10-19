import { createApp } from "vue"; // 用于创建应用
import App from "./App.vue"; // 根页面
import router from "./router"; // 路由
import store from "./store"; // 保存预设，历史信息
import "./assets/css/tailwind.css";

createApp(App).use(store).use(router).mount("#app");
