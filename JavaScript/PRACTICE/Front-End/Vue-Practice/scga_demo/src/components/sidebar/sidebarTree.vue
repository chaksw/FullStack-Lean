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
	import { ref, watch } from "vue";

	const filterText = ref("");
	const treeRef = ref();

	const defaultProps = {
		children: "children",
		label: "label",
	};

	watch(filterText, (val) => {
		treeRef.value.filter(val);
	});

	const filterNode = (value, data) => {
		if (!value) return true;
		return data.label.includes(value);
	};

	const data = [
		{
			id: 1,
			label: "Level A",
			children: [
				{
					id: 4,
					label: "Test Plan",
					children: [
						{
							id: 10,
							label: "PfdDioASCB.cpp",
						},
						{
							id: 11,
							label: "PfdGioAtt.cpp",
						},
					],
				},
				{
					id: 5,
					label: "Test Exception",
					children: [

					]
				},
			],
		},
		{
			id: 2,
			label: "Level B",
			children: [
				{
					id: 6,
					label: "Test Plan",
				},
				{
					id: 7,
					label: "Test Exception",
				},
			],
		},
		{
			id: 3,
			label: "Level C",
			children: [
				{
					id: 8,
					label: "Test Plan",
				},
				{
					id: 9,
					label: "Test Exception",
				},
			],
		},
	];
</script>

<style lang="css" scoped>
	.treeview {
		display: flex;
		flex-direction: column;
		justify-content: top;
		padding: 10px;
	}
</style>
