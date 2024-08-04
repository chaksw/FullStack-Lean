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
    // 嵌套式路由（子路由）结合共享组件
    {
        // 1.嵌套路由
        path: "/vip", // http://localhost:5173/vip
        component: () => import("@/views/vip.vue"),
        // 定义子路由，path不需要带‘/’
        // 要访问子路由，需要在对应的父页面（vip.vue）中添加<router-view></router-view>
        children: [
            {
                // 定义默认页面，将path定义为空 path: ""
                path: "", // http://localhost:5173/vip/
                component: () => import("@/views/vip/default.vue"),
            },
            {
                path: "order", // http://localhost:5173/vip/order
                component: () => import("@/views/vip/order.vue"),
            },
            {
                path: "info", // http://localhost:5173/vip/info
                component: () => import("@/views/vip/info.vue"),
            },
        ],
        // 2. 共享组件: 共享组件是每个视图公用的，不需要进行路由嵌套，只需要在父组件视图中导入并在template中调用即可
    },
    // 重定向：定义 redirect 参数，当访问/svip时，网页会自动跳转至 redirect 定义的路由位置
    {
        path: "/svip", // http://localhost:5173/vip
        // redirect: "vip",
        // redirect 也可以实现编程式导航 （类似 <router-link></router-link> 和 router.push 所接受的参数）, 这里svip会重定向到 user 页面并传递参数 { id: 300, name: "chaksw" }
        redirect: { name: "member", params: { id: 300, name: "chaksw" } },
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
