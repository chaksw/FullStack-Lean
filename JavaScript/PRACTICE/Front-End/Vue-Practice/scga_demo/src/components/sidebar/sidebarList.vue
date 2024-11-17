<template>
	<el-menu :default-active="selectedIndex" class="uncpllapsed-sidebar-list">
		<el-menu-item index="0" class="menu-item">
			<el-icon><Location /></el-icon>
		</el-menu-item>
		<el-menu-item index="1" class="menu-item">
			<el-icon><Menu /></el-icon> </el-menu-item
		><el-menu-item index="2" class="menu-item">
			<el-icon><Setting /></el-icon> </el-menu-item
		><el-menu-item index="3" class="menu-item">
			<el-icon><Document /></el-icon>
		</el-menu-item>
	</el-menu>
</template>

<script setup></script>

<style lang="css" scoped>
	.uncpllapsed-sidebar-list {
		display: flex;
		flex-direction: column;
		justify-content: top;
		align-items: center;
		width: 20%;
		min-height: 100vh;
	}
</style>
