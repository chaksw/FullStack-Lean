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
			highlight-current
			ref="treeRef"
			style="max-width: 600px"
			class="filter-tree"
			:data="data"
			:props="defaultProps"
			:filter-node-method="filterNode"
		/>
	</el-container>
</template>

<script setup>
	import { Search } from "@element-plus/icons-vue";
	import { ref, inject, watch } from "vue";
	const filterText = ref("");
	const treeRef = ref();
	const levels = inject("levels");
	const data = ref();
	const functions = ref([]);
	const processLevelData = (levels) => {
		let data = [];
		// for each level data
		for (let idx = 0; idx < levels.value.length; idx++) {
			let level = {};
			let testPlan = {};
			let testException = {};
			level.id = levels.value[idx].id;
			level.label = "Level " + levels.value[idx].level;
			level.children = [];

			// test plan
			if (levels.value[idx].test_plan) {
				testPlan = precessTestPlanData(levels.value[idx].test_plan);
				level.children.push(testPlan);
			}
			// test exception
			if (levels.value[idx].test_exception) {
				testException = precessTesExceptionData(
					levels.value[idx].test_exception
				);
				level.children.push(testException);
			}
			if (level.children.length !== 0) {
				data.push(level);
			}
		}
		// console.log(data);
		return data;
	};
	const precessTestPlanData = (testPlanData) => {
		// console.log(testPlanData);
		let testPlan = {};
		testPlan.id = testPlanData.id;
		testPlan.label = testPlanData.sheet_name;
		testPlan.lv_total_coverage = testPlanData.lv_total_coverage
		console.log(testPlan.lv_total_coverage);
		testPlan.children = processModulesData(testPlanData.modules);
		return testPlan;
	};
	const precessTesExceptionData = (testExceptionData) => {
		let testException = {};
		testException.id = testExceptionData.id;
		testException.label = testExceptionData.sheet_name;
		testException.children = processModulesData(testExceptionData.modules);
		return testException;
	};

	const processModulesData = (modulesData) => {
		let modules = [];
		
		for (let idx = 0; idx < modulesData.length; idx++) {
			let module = {};
			module.id = modulesData[idx].id;
			module.label = modulesData[idx].module_name;
			module.functions = modulesData[idx].functions
			modules.push(module);
		}
		return modules;
	};

	watch(() => {
		if (levels.value) {
			console.log(levels.value);
			data.value = processLevelData(levels);
		}
	});

	const defaultProps = {
		label: "label",
		children: "children",
	};

	watch(filterText, (val) => {
		treeRef.value.filter(val);
	});

	const filterNode = (value, data) => {
		if (!value) return true;
		return data.label.toLowerCase().includes(value.toLowerCase());
	};
</script>

<style lang="css" scoped>
	.treeview {
		display: flex;
		flex-direction: column;
		justify-content: top;
		padding: 10px;
	}
</style>
