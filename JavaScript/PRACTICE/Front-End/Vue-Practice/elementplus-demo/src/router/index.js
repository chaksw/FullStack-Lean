import { createRouter, createWebHistory } from "vue-router";

const routes = [
	{
		path: "/button-icon",
		component: () => import("@/views/buttonIcon.vue"),
	},
	{
		path: "/message",
		component: () => import("@/views/message.vue"),
	},
	{
		path: "/tabs",
		component: () => import("@/views/tabs.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
