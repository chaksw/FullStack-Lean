import {
    createRouter,
    createWebHashHistory,
    createWebHistory,
} from "vue-router";

// 存储路由
const routes = [
    {
        path: "/",
        component: () => import("../views/index.vue"),
    },
    {
        path: "/content",
        component: () => import("../views/content.vue"),
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
