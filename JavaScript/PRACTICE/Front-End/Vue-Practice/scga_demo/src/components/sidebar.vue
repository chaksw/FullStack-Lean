<template>
	<div>
		<el-col>
			<el-menu
				:default-active="selectedIndex"
				class="el-menu-vertical-demo"
			>
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
		</el-col>
	</div>
</template>

<script setup></script>

<style lang="css" scoped>
	.el-menu-vertical-demo {
		width: 100%;
		min-height: 100vh;
	}
</style>
