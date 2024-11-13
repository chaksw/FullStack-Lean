import { createApp } from "vue";
import "./assets/css/main.css";
import ElementPlus from "element-plus"; // 导入 ElementPlus 组件库的所有模块和功能
import "element-plus/dist/index.css"; // 导入 ElementPlus 组件库所需的全局 CSS 样式
import * as ElementPlusIconsVue from "@element-plus/icons-vue" // 导入 ElementPlus 组件库的所有图标
import router from "./router";
import App from "./App.vue";

const app = createApp(App);

for (const [key, component] of Object.entries(ElementPlusIconsVue)){
    app.component(key, component)
}

app.use(ElementPlus);
app.use(router)
app.mount("#app");
