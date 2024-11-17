<template>
	<!-- sidebar header -->
	<el-container class="sidebar-horizontal-header">
		<!-- Title & buttons -->
		<el-container class="sidebar-horizontal-header-content">
			<p>SCGA WorkSpace</p>
			<div style="display: flex; align-items: center">
				<el-button>New</el-button>
				<el-button>Import</el-button>
			</div>
		</el-container>
		<el-divider style="margin-top: 10px; margin-bottom: 0px"></el-divider>
	</el-container>
</template>

<script setup></script>

<style lang="css" scoped>
	.sidebar-horizontal-header {
		display: flex;
		flex-direction: column;
		font-size: 15px;
	}
	.sidebar-horizontal-header-content {
		display: flex;
		justify-content: space-between;
		padding: 0 10px;
		align-items: center;
		font-weight: 600;
	}
	.el-button {
		font-weight: 700;
		font-size: 14px;
	}
</style>
