import "./assets/main.css";
import router from "./router";
import { createApp } from "vue";
import App from "./App.vue";

// .use(router), 将vue-router实例注册到vue中
// createApp(App).use(router).mount("#app");

const app = createApp(App);
app.use(router);
// 全局前置守卫 ｜ 前置中间件
// 作用：对请求进行基于权限判断的拦截，如用户希望访问某个信息页面（url-A），但该页面访问前提是用户已经登陆，这时就需要服务端通过前置守卫对访问请求进行拦截并跳转到登录页面
// 还有全局解析守卫和全局后置钩子
// PS: 在前端很少进行权限判断的实现，一般都是在后端实现。
router.beforeEach((to, from, next) => {
    console.log("to: ", to); // to: 即将进入的路由信息
    console.log("from: ", from); // from: 当前将离开的路由信息

    // next(); // 只有 next() 执行，路由才算成功被访问
    // 拦截测试: 当即将进入的路由 route.name 为 "member" 时，执行 next(false) 进行拦截
    if (to.name == "name") {
        next(false); // 拦截
    } else {
        next(); // 继续
    }
});
app.mount("#app");
