<template>
	<el-container class="treeview">
		<el-input
			style="width: 100%"
			v-model="filterText"
			placeholder="Search file"
			:prefix-icon="Search"
			clearable
		/>
		<el-tree
			ref="treeRef"
			style="max-width: 600px"
			class="filter-tree"
			:data="data"
			:props="defaultProps"
			:filter-node-method="filterNode"
			default-expand-all
		/>
	</el-container>
</template>

<script setup>
	import { Search } from "@element-plus/icons-vue";
</script>

<style lang="css" scoped>
	.treeview {
		display: flex;
		flex-direction: column;
		justify-content: top;
		padding: 10px;
	}
</style>
