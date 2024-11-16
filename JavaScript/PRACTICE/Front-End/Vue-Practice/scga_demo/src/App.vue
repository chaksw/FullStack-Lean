<template>
	<div class="common-layout">
		<el-container>
			<!-- header -->
			<el-header>
				<navigation />
			</el-header>
			<el-container>
				<el-aside>
					<sidebar />
				</el-aside>
				<el-container>
					<el-main>
						<h3>Test</h3>
					</el-main>
					<router-view />
					<el-footer>Footer</el-footer>
				</el-container>
			</el-container>
		</el-container>
	</div>
</template>

<script setup>
	import navigation from "@/components/navBar.vue";
	import sidebar from "@/components/sidebar.vue";
</script>

<style lang="css" scoped>
	.el-aside {
		width: 70px !important;
	}
</style>
