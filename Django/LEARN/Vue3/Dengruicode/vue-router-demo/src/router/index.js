import {
    createRouter,
    createWebHashHistory,
    createWebHistory,
} from "vue-router";

// 存储路由
const routes = [
    {
        path: "/",
        // 定义别名使用 alias 属性
        // alias: "/home",
        // 也可以通过数组定义多个别名
        alias: ["/home", "/index"],
        // component: () => import("../views/index.vue"),
        component: () => import("@/views/index.vue"),
    },
    {
        path: "/content",
        // 字符串传参 ?: 内容保存在 $route.query 中
        // 使用查询字符 ? 传递参数 http://localhost:5173/content?id=100&title=邓瑞编程
        // ？后的内容会保存在 $route.query中
        component: () => import("@/views/content.vue"),
    },
    {
        // 路径传参 : 内容保存在 $route.params 中
        // note: 使用路径传参， 必须保证对应的url跟路径规则一致
        // path: "/user/:id/name/:name",
        // 如果希望:name不是必须出现在url中，可以在后面追加 ?
        path: "/user/:id/name/:name?",
        name: "member",
        // 使用查询字符 ? 传递参数 http://localhost:5173/user/007/name/邓瑞
        // ？后的内容会保存在 $route.query中
        component: () => import("@/views/user.vue"),
    },
];

// 路由器
const router = createRouter({
    // # 使用 createWebHashHistory 之后，对应的url会在前方多一个#符号，这种方式多用于模拟url路径的变化，因为不会触发页面刷新，所以不需要服务端支持
    // history:createWebHashHistory(),
    history: createWebHistory(),
    routes,
});

export default router;
