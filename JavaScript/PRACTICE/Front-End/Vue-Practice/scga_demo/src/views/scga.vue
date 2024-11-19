<template>
	<!-- sidebar & divier & main -->
	<el-container>
		<sidebar :baseline="baseline" :levels="levels"/>
		<!-- divider -->
		<div>
			<el-divider
				direction="vertical"
				style="min-height: 100vh; height: 100%"
			></el-divider>
		</div>
		<!-- main -->
		<el-main>
			<scgaFunctions />
		</el-main>
	</el-container>
</template>

<script setup>
	import scgaFunctions from "@/components/scga/scgaFunctions.vue";
	import sidebar from "@/components/scga/sidebar/sidebar.vue";
	import axios from "axios";
	import { ref, provide, onMounted, onBeforeMount } from "vue";
	// scga list
	const data = ref([]);
	const baseline = ref("")
	const levels = ref([])
	provide('baseline', baseline)
	provide('levels', levels)

	
	const getScgaData = () => {
		let url = "api/scgas";
		// get scga data
		axios
			.get(url)
			.then((response) => {
				data.value = response.data.results;
				console.log(data.value);
				baseline.value = data.value[0].baseline
				levels.value = data.value[0].levels
			})
			.catch((error) => {
				console.log(error);
			});
	};

	onBeforeMount(() => {
		getScgaData();
	});

</script>

<style lang="css" scoped></style>
