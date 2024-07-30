import "./assets/main.css";
import router from "./router";
import { createApp } from "vue";
import App from "./App.vue";

// .use(router), 将vue-router实例注册到vue中
createApp(App).use(router).mount("#app");
