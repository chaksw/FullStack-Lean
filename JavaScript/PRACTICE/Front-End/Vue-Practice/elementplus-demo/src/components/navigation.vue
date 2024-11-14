<template>
	<h3 class="ml-2">Horizontal Navigation</h3>
	<!-- 默认是垂直导航，mode="horizontal" 表示水平导航 -->

	<el-menu
		mode="horizontal"
		:default-active="selectedIndex"
		@select="selected"
	>
		<el-menu-item index="1">Item 1</el-menu-item>
		<el-menu-item index="2">
			<el-sub-menu>
				<template #title>My workspace</template>
				<el-menu-item index="2-1">Option 1</el-menu-item>
				<el-menu-item index="2-2">Option 2</el-menu-item>
				<el-menu-item index="2-3">Option 3</el-menu-item>
			</el-sub-menu>
		</el-menu-item>
		<el-menu-item index="3">Item 3</el-menu-item>
		<el-menu-item index="4">Item 4</el-menu-item>
	</el-menu>

	<h3 class="ml-2">Customized Horizontal Navigation</h3>
	<!-- 默认是垂直导航，mode="horizontal" 表示水平导航 -->

	<el-menu
		mode="horizontal"
		:default-active="selectedIndex"
		@select="selected"
		background-color="#545c64"
		text-color="#fff"
		active-text-color="#ffd04b"
		style="height: 40px"
	>
		<el-menu-item index="1">Item 1</el-menu-item>
		<el-menu-item index="2">
			<el-sub-menu>
				<template #title>My workspace</template>
				<el-menu-item index="2-1">Option 1</el-menu-item>
				<el-menu-item index="2-2">Option 2</el-menu-item>
				<el-menu-item index="2-3">Option 3</el-menu-item>
			</el-sub-menu>
		</el-menu-item>
		<el-menu-item index="3">Item 3</el-menu-item>
		<el-menu-item index="4">Item 4</el-menu-item>
	</el-menu>

	<!-- <h3 class="ml-2">Customized Navigation</h3>
	<el-menu
		:default-active="selectedIndex"
		@select="selected"
		background-color="#545c64"
		text-color="#fff"
		active-text-color="#ffd04b"
		style="width: 200px"
	>
		<el-menu-item index="1">Item 1</el-menu-item>
		<el-menu-item index="2">
			<el-sub-menu>
				<template #title>My workspace</template>
				<el-menu-item index="2-1">Option 1</el-menu-item>
				<el-menu-item index="2-2">Option 2</el-menu-item>
				<el-menu-item index="2-3">Option 3</el-menu-item>
			</el-sub-menu>
		</el-menu-item>
		<el-menu-item index="3">Item 3</el-menu-item>
		<el-menu-item index="4">Item 4</el-menu-item>
	</el-menu> -->

	<h3>Bread crumb</h3>
	<el-breadcrumb separator="/">
		<el-breadcrumb-item><a href="#">Home</a></el-breadcrumb-item>
		<el-breadcrumb-item>Buttons</el-breadcrumb-item>
		<el-breadcrumb-item>Message</el-breadcrumb-item>
	</el-breadcrumb>

	<h3>Dropdown Menu</h3>

	<!-- 通过定义 @command 对应的回调函数来获取下拉菜单被选中时返回的 command 值 -->
	<el-dropdown @command="userCommand">
		<span>
			Person
			<el-icon>
				<user />
			</el-icon>
		</span>
		<template #dropdown>
			<el-dropdown-item command="order">Order</el-dropdown-item>
			<el-dropdown-item command="logout">Logout</el-dropdown-item>
		</template>
	</el-dropdown>
</template>

<script setup>
	import { reactive, ref } from "vue";

	// 默认选中的菜单索引
	const selectedIndex = ref("2");
	// 选中菜单触发的回调
	const selected = (index, indexPath) => {
		console.log("index", index, "indexPath", indexPath);
	};

	const userCommand = (command) => {
		console.log(command);
	};
</script>

<style lang="scss" scoped></style>
