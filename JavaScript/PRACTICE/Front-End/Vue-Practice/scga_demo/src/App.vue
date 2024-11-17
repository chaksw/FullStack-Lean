<template>
	<div>
		<el-container>
			<!-- header -->
			<el-header>
				<navigation />
			</el-header>
			<!-- sidebar & divier & main -->
			<el-container>
				<sidebar />
				<!-- divider -->
				<div>
					<el-divider
						direction="vertical"
						style="min-height: 100vh; height: 100%"
					></el-divider>
				</div>
				<!-- main -->
				<el-main>
					<file-functions />
					<router-view />
				</el-main>
			</el-container>
		</el-container>
		<el-footer>Footer</el-footer>
	</div>
</template>

<script setup>
	import navigation from "@/components/navBar.vue";
	import sidebar from "@/components/sidebar/sidebar.vue";
	import fileFunctions from "@/views/scga/fileFunctions.vue";
</script>

<style lang="css" scoped></style>
