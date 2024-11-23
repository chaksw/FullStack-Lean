<template>
	<!-- sidebar header -->
	<el-container class="sidebar-horizontal-header">
		<!-- Title & buttons -->
		<el-container class="sidebar-horizontal-header-content">
			<p>{{ baseline }}</p>
			<!-- configure button -->
			<el-tooltip
				class="box-item"
				effect="dark"
				content="Configure PAS SCGA Dataset"
				placement="bottom"
			>
				<el-button circle text
					><el-icon style="font-size: 20px"
						><Setting /></el-icon></el-button
			></el-tooltip>
		</el-container>
		<!-- import button -->
		<!-- ref 是 Vue 提供的一个指令，用来直接引用 DOM 元素或组件实例，便于在脚本中操作它们。可以理解为一种快捷的方式来访问特定的 DOM 或组件。 -->
		<!-- ref="upload" 会将当前的 el-upload 组件实例引用到 setup 或 data 中定义的 ref 对象上。 -->

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
	import axios from "axios";
	// v-model 和 ref 的核心区别
	// v-model 是用于 双向绑定数据 的。它通常绑定组件的值或者用户输入的值。
	// ref 是为了获取 DOM 或组件实例的引用。
	const upload = ref(); // instance of import
	const isUploading = ref(false);
	const fileName = ref();
	const baseline = ref("SCGA Workspace");

	const handleChange = (uploadFile, uploadFiles) => {
		isUploading.value = uploadFile.name ? true : false;
		fileName.value = ploadFile.name;
		// console.log(
		// 	"upload file",
		// 	upload.value.uploadFiles.map((file) => file.name)
		// );
		console.log("upload file", upload.value);
		// console.log(isUploading.value);
	};

	onMounted(() => {
		isUploading.value = false;
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
			formData.append("file", upload.value.raw); // `raw` 是 ElUpload 文件对象的实际文件数据

			// send to backend
			const response = await axios.post("api/upload-scgas/", formData, {
				headers: {
					"Content-Type": "multipart/form-date", // must have
				},
			});
			// console.log(upload.value);
			isUploading.value = false;
			ElMessage.success(`File ${fileName.value} import successfully!`);
			// get response
			console.log("Response from server: ", response.data);
			// reset status
			upload.value.clearFiles(); //clear upload component
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
	}
	.el-button {
		font-weight: 700;
		font-size: 14px;
	}
</style>
