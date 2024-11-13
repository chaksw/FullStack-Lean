<template>
	<div>
		<el-button @click="openMsg">success</el-button>
		<el-button @click="openConfirm">confirm</el-button>
		<el-button @click="openNotifiy">通知</el-button>
		<el-button @click="openNotifiy2">通知2</el-button>
	</div>
</template>

<script setup>
// 消息，确认框，通知
import { ElMessage, ElMessageBox, ElNotification } from "element-plus";

// 消息
const openMsg = () => {
	ElMessage({
		type: "success", // success | warning | info | error
		message: "This is a success message",
		showClose: true,
	});
};
// 确认框
const openConfirm = () => {
	const content = "This is a warning message ?";
	const title = "Title";
	ElMessageBox.confirm(content, title, {
		type: "warning",
		confirmButtonText: "OK",
		cancelButtonText: "Cancel",
	})
		.then(() => {
			// in case OK is pressed
			console.log("confirm");
		})
		.catch(() => {
			// in case cancel is pressed
			console.log("cancel");
		});
};

// 通知
const openNotifiy = () => {
	ElNotification({
		title: "Title",
		message: "This is a message dure 1.5s",
		duration: 1500, // ms
	});
};

const openNotifiy2 = () => {
	ElNotification({
		type: "error",
		title: "Title",
		message: "This is a error message dure 1.5s",
		duration: 1500, // ms
		position: "bottom-right", // default is top-right
	});
};
</script>

<style lang="scss" scoped></style>
