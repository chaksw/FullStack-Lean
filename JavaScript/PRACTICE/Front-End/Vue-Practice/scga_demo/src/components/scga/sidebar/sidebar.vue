<template>
	<el-aside>
		<sidebarHeader />
		<sidebarContainer @send-module="onSendModule"/>
	</el-aside>
</template>

<script setup>
	import sidebarHeader from "./sidebarHeader.vue";
	import sidebarContainer from "./sidedbarContainer.vue";
	// const selectedModule = ref();
	const emit = defineEmits(['sendModule'])

	// send to scga.vue
	const onSendModule = (module) => {
		// console.log("on sidebar", module);
		emit("sendModule", module)
	};
</script>

<style lang="css" scoped>
	.el-aside {
		margin-top: 15px;
		width: 25% !important;
		max-width: 30%;
	}
</style>
