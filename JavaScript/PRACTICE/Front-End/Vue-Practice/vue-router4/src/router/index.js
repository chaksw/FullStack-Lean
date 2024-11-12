// 用于配置路由资源以及路由规则
import {
	createRouter,
	createWebHistory,
	createWebHashHistory,
} from "vue-router";

// 路由资源对象
const routes = [
	{
		path: "/",
		component: () => import("@/views/index.vue"),
	},
	{
		path: "/content",
		component: () => import("@/views/content.vue"),
	},
	{
		// 传递参数用 $route.params 获取
		// :id 表示传递的参数
		// :name？ 表示该传递参数不是必须在url中设置的
		path: "/user/:id/name/:name?",
		component: () => import("@/views/user.vue"),
	},
];

// 路由规则
const router = createRouter({
	// 使用 createWebHashHistory 会让 url自动符号，
	// 使用 url 的 # 符号之后的部分模拟 url 路径的变化，因为不会触发页面的刷新，所以不需要服务端的支持
	// history: createWebHashHistory(),
	history: createWebHistory(),
	routes,
});

export default router;
