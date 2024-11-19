<template>
	<el-table :data="Functions" style="width: 100%" max-height="800">
		<el-table-column prop="process" label="Process" width="180" fixed/>
		<el-table-column
			fixed
			prop="function_name"
			label="Function Name"
			width="180"
		/>
		<el-table-column prop="analyst" label="Analyst" width="180" />
		<el-table-column prop="site" label="Site" width="180" />
		<el-table-column prop="start_date" label="Start Date" width="180" />
		<el-table-column prop="coverage" label="Coverage" width="180">
			<el-table-column
				prop="coverage.percent_coverage_MCDC"
				label="Percent MC/DC"
			/>
			<el-table-column
				prop="coverage.percent_coverage_Analysis"
				label="Percent Analysis"
			/>
			<el-table-column prop="coverage.total_coverage" label="Total by SC Tool" />
		</el-table-column>
		<el-table-column
			prop="moduleStrucData"
			label="Module Structure Data (Conditions, Decisions and statements)"
		>
			<el-table-column prop="moduleStrucData.covered" label="Covered">
				<el-table-column prop="moduleStrucData.covered.branches" label="Branches" />
				<el-table-column prop="moduleStrucData.covered.pairs" label="Pairs" />
				<el-table-column prop="moduleStrucData.covered.statement" label="Statements" />
			</el-table-column>
			<el-table-column prop="moduleStrucData.total" label="Total">
				<el-table-column prop="moduleStrucData.total.branches" label="Branches" />
				<el-table-column prop="moduleStrucData.total.pairs" label="Pairs" />
				<el-table-column prop="moduleStrucData.total.statement" label="Statements" />
			</el-table-column>
		</el-table-column>
		<el-table-column prop="oversight" label="Oversight" />
		<el-table-column prop="defect_classification" label="Defect Classification">
			<el-table-column prop="defect_classification.tech" label="Tech" />
			<el-table-column prop="defect_classification.non_tech" label="No-Tech" />
			<el-table-column prop="defect_classification.process" label="Process" />
		</el-table-column>
	</el-table>
</template>

<script setup>
	const Functions = [
		{
			function_name: "GlosTerm::Consume_20Hz",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 1.0,
					pairs: 0.0,
					statement: 210.0,
				},
				total: {
					branches: 1.0,
					pairs: 0.0,
					statement: 210.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::FirstInitGlossary",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
				total: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::FirstInitGlossary",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
				total: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::FirstInitGlossary",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
				total: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::FirstInitGlossary",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
				total: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::FirstInitGlossary",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
				total: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::FirstInitGlossary",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
				total: {
					branches: 1.0,
					pairs: 0.0,
					statement: 115.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::Loader_FcsCoupledSideFdModeSource",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 31.0,
					pairs: 12.0,
					statement: 3.0,
				},
				total: {
					branches: 31.0,
					pairs: 12.0,
					statement: 3.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::Loader_NavDataFmsSelect",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 13.0,
					pairs: 3.0,
					statement: 3.0,
				},
				total: {
					branches: 13.0,
					pairs: 3.0,
					statement: 3.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::Loader_SelectedPfdDataCopilot",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 1.0,
					pairs: 0.0,
					statement: 8.0,
				},
				total: {
					branches: 1.0,
					pairs: 0.0,
					statement: 8.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::Loader_SelectedPfdDataPilot",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 1.0,
					pairs: 0.0,
					statement: 8.0,
				},
				total: {
					branches: 1.0,
					pairs: 0.0,
					statement: 8.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
		{
			function_name: "GlosTerm::Loader_DcSourceSideSelect",
			analyst: "Ye Lin",
			site: "Shanghai (EDS)",
			start_date: "2021-10-22",
			coverage: {
				percent_coverage_MCDC: 1.0,
				percent_coverage_Analysis: 0.0,
				total_coverage: 1.0,
			},
			moduleStrucData: {
				covered: {
					branches: 9.0,
					pairs: 2.0,
					statement: 2.0,
				},
				total: {
					branches: 9.0,
					pairs: 2.0,
					statement: 2.0,
				},
			},
			oversight: null,
			defect_classification: {
				tech: null,
				non_tech: null,
				process: null,
			},
		},
	];
</script>

<style lang="scss" scoped></style>
