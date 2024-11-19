<template>
	<el-aside>
		<sidebarHeader />
		<sidebarContainer />
	</el-aside>
</template>

<script setup>
	import sidebarHeader from "./sidebarHeader.vue";
	import sidebarContainer from "./sidedbarContainer.vue";
	
</script>

<style lang="css" scoped>
	.el-aside {
		margin-top: 15px;
		width: 25% !important;
		max-width: 30%;
	}
</style>
