<template>
	<!-- sidebar & divier & main -->
	<el-container>
		<sidebar
			@send-module="onSendModule"
		/>
		<!-- divider -->
		<div>
			<el-divider
				direction="vertical"
				style="min-height: 100vh; height: 100%"
			></el-divider>
		</div>
		<!-- main -->
		<el-main>
			<div>
				<testPlan v-if="isTestPlan" />
				<testException v-else />
			</div>
		</el-main>
	</el-container>
</template>

<script setup>
	import testPlan from "@/components/scga/testPlan.vue";
	import testException from "@/components/scga/testException.vue";
	import sidebar from "@/components/scga/sidebar/sidebar.vue";
	import axios from "axios";
	import { ref, provide, onMounted } from "vue";
	// scga list
	const data = ref([]);
	const baseline = ref("SCGA Workspace");
	const levels = ref(null);
	const selectedModule = ref();
	const isTestPlan = ref(true);
	// receive from sidebar treeview
	const onSendModule = (module) => {
		selectedModule.value = module.value;
		// console.log("on scga", selectedModule.value.root);
		// check it's test plan or test exception
		isTestPlan.value = selectedModule.value.root.name.includes("Test Plan") ? true : false;
	};

	onMounted(async () => {
		await fetchScga();
	});

	const fetchScga = async () => {
		let url = "api/scgas";
		// get scga data
		await axios
			.get(url)
			.then((response) => {
				data.value = response.data.results;
				// console.log(data.value);
				baseline.value = data.value[0].baseline;
				levels.value = data.value[0].levels;
				levels.value.baseline = baseline.value;
			})
			.catch((error) => {
				console.log(error);
			});
	};

	provide("baseline", baseline);
	provide("levels", levels);
	provide("selectedModule", selectedModule)
</script>

<style lang="css" scoped></style>
