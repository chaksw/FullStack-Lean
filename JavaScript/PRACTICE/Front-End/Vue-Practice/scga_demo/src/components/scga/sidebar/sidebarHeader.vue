<template>
	<!-- sidebar header -->
	<el-container class="sidebar-horizontal-header">
		<!-- Title & buttons -->
		<el-container class="sidebar-horizontal-header-content">
			<p>{{ baseline }}</p>

			<el-tooltip
				class="box-item"
				effect="dark"
				content="Configure Previous SCGA"
				placement="bottom"
			>
				<el-button circle text
					><el-icon><Setting /></el-icon></el-button
			></el-tooltip>
		</el-container>
		<el-container class="import-area">
			<el-upload
				ref="upload"
				style="display: flex; width: 90%"
				:before-remove="beforeRemove"
				:on-change="handleChange"
				:limit="1"
				:on-exceed="handleExceed"
				:auto-upload="false"
			>
				<el-button>Import</el-button>
			</el-upload>
			<el-button v-if="isUploading" @click="submitUpload"
				><el-icon><Select /></el-icon
			></el-button>
		</el-container>
		<el-divider style="margin-top: 10px; margin-bottom: 0px"></el-divider>
	</el-container>
</template>

<script setup>
	import { ref, inject, onMounted } from "vue";
	import { ElMessage, ElMessageBox, genFileId } from "element-plus";

	const upload = ref();
	const scgaFile = ref({});
	const isUploading = ref(false);

	const baseline = inject("baseline");

	// const handleRemove = (file, uploadFiles) => {
	// 	console.log(file, uploadFiles);
	// };

	// const handlePreview = (uploadFile) => {
	// 	console.log(uploadFile);
	// };

	const handleChange = (uploadFile, uploadFiles) => {
		isUploading.value = uploadFile.name ? true : false;
		scgaFile.value = uploadFile
		console.log(scgaFile.value);
		console.log(isUploading.value);
	};

	onMounted(() =>{
		isUploading.value = false;
	})

	const handleExceed = (files) => {
		upload.value.clearFiles();
		const file = files[0];
		file.uid = genFileId();
		upload.value.handleStart(file);
	};

	const submitUpload = () => {
		return ElMessageBox.confirm(
			`Confirm the import of ${scgaFile.value.name} ?`
		).then(
			() => {
				// console.log("gggg");
				isUploading.value = false;
				upload.value.submit();
				console.log(upload.value);
				return true;
			},
			() => {
				// console.log("asdasd");
				return false;
			}
		);
	};

	const beforeRemove = (uploadFile, uploadFiles) => {
		return ElMessageBox.confirm(
			`Cancel the import of ${uploadFile.name} ?`
		).then(
			() => {
				isUploading.value = false;
				scgaFile.value = null
				true;
			},
			() => false
		);
	};
	// const header = ref("EDSGGF_GS_GCOM_00_016");
</script>

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
	.import-area {
		justify-content: space-between;
		align-items: center;
		padding: 0 10px;
	}
	.el-button {
		font-weight: 700;
		font-size: 14px;
	}
</style>
