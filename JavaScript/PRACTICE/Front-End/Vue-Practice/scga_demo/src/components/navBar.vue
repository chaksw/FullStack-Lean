<template>
	<div>
		<el-menu
			mode="horizontal"
			:default-active="selectedIndex"
			@select="selected"
			style="font-size: 50px;"
		>
			<el-menu-item index="0" alt="logo"
				><a href="/"><arrow-down-left-icon /><el-icon><Menu /></el-icon> </a
			></el-menu-item>
			<el-menu-item index="1">
				<el-sub-menu>
					<template #title>SCGA</template>
					<el-menu-item index="2-1">Option 1</el-menu-item>
					<el-menu-item index="2-2">Option 2</el-menu-item>
					<el-menu-item index="2-3">Option 3</el-menu-item>
				</el-sub-menu>
			</el-menu-item>
			<el-menu-item index="2">TRS</el-menu-item>

			<el-menu-item index="3">RA</el-menu-item>
		</el-menu>
	</div>
</template>

<script setup>
</script>

<style lang="scss" scoped></style>
