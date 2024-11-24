<template>
	<!-- sidebar header -->
	<el-container class="sidebar-horizontal-header">
		<!-- Title & buttons -->
		<el-container class="sidebar-horizontal-header-content">
			<p>{{ baseline }}</p>
			<!-- configure button -->
			<!-- 这里加三个点 -->
			<el-dropdown trigger="click" v-if="isImported">
				<span class="el-dropdown-link">
					<el-icon><MoreFilled /></el-icon>
				</span>
				<template #dropdown>
					<el-dropdown-menu>
						<el-dropdown-item
							class="dropdown-item"
							style="
								width: 150px;
								display: flex;
								justify-content: space-between;
							"
							>Configure
							<el-icon style="font-size: 20px"
								><Setting /></el-icon
						></el-dropdown-item>
						<el-dropdown-item
							style="
								width: 150px;
								display: flex;
								justify-content: space-between;
							"
						>
							Delete
							<el-icon style="font-size: 20px"
								><DocumentDelete
							/></el-icon>
						</el-dropdown-item>
					</el-dropdown-menu>
				</template>
			</el-dropdown>

			<!-- <el-tooltip
				class="box-item"
				effect="dark"
				content="Configure PAS SCGA Dataset"
				placement="bottom"
			>
				<el-button text>Configure</el-button></el-tooltip
			> -->
		</el-container>
		<!-- import button -->
		<!-- ref 是 Vue 提供的一个指令，用来直接引用 DOM 元素或组件实例，便于在脚本中操作它们。可以理解为一种快捷的方式来访问特定的 DOM 或组件。 -->
		<!-- ref="upload" 会将当前的 el-upload 组件实例引用到 setup 或 data 中定义的 ref 对象上。 -->
		<el-container class="import-area" v-if="!isImported">
			<el-upload
				ref="upload"
				style="display: flex; width: 90%"
				:on-change="handleChange"
				:on-exceed="handleExceed"
				:before-remove="beforeRemove"
				:limit="1"
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
	import axios from "axios";
	import { ref, inject, onMounted, watch } from "vue";
	import { ElMessage, ElMessageBox, genFileId } from "element-plus";
	// v-model 和 ref 的核心区别
	// v-model 是用于 双向绑定数据 的。它通常绑定组件的值或者用户输入的值。
	// ref 是为了获取 DOM 或组件实例的引用。
	// 这里的upload只作为组件实例，只包含一些clearFiles(), submit()等方法，不能用于发送请求
	const upload = ref(null); // instance of import
	let importFile = null; // 存储选中的文件
	const isUploading = ref(false);
	const fileName = ref(null);
	const baseline = inject("baseline");
	const isImported = ref(false);
	// scga import result

	const handleChange = (uploadFile, uploadFiles) => {
		isUploading.value = uploadFile.name ? true : false;
		importFile = uploadFile.raw;
		fileName.value = uploadFile.name;
		console.log(importFile);
	};

	onMounted(() => {
		isUploading.value = false;
		isImported.value = false;
	});

	watch(() => {
		isImported.value = baseline.value === "SCGA Workspace" ? false : true;
	});

	const handleExceed = (files) => {
		upload.value.clearFiles();
		const file = files[0];
		file.uid = genFileId();
		upload.value.handleStart(file);
	};

	const submitUpload = async () => {
		try {
			await ElMessageBox.confirm(
				`Confirm the import of ${fileName.value} ?`
			);

			// create form
			const formData = new FormData();
			console.log(importFile);
			formData.append("file", importFile); // `raw` 是 ElUpload 文件对象的实际文件数据

			// send to backend
			const response = await axios.post("api/upload-scgas/", formData, {
				headers: {
					"Content-Type": "multipart/form-data", // must have
				},
			});
			// console.log(upload.value);
			isUploading.value = false;
			ElMessage.success(`File ${fileName.value} import successfully!`);
			// get response
			console.log("Response from server: ", response.data);
			location.reload();
			// upload.clearFiles(); //clear upload component
			// reset status
		} catch (error) {
			// handle cancel or fail of import
			if (axios.isCancel(error) || error === "cancel") {
				ElMessage.info("File upload canceled");
			} else {
				console.error("Upload error: ", error);
				ElMessage.error("Fail to upload file.", error);
			}
		}
	};

	const beforeRemove = (uploadFile, uploadFiles) => {
		return ElMessageBox.confirm(
			`Cancel the import of ${uploadFile.name} ?`
		).then(
			() => {
				isUploading.value = false;
				upload.value.clearFiles();
				ElMessage.info("File upload canceled");
				true;
			},
			() => false
		);
	};
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
		padding-top: 10px;
	}

	.dropdown-item {
		width: 150px;
		color: red;
		display: flex;
		justify-content: space-between;
	}
	.el-button {
		font-weight: 500;
		font-size: 14px;
	}
</style>
