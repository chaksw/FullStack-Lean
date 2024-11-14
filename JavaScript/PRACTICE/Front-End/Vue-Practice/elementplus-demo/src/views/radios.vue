<template>
	<div>
		<!-- 单选框 -->
		<h3>Radios</h3>
		<el-radio v-model="radio" label="" value="1">FrontEnd</el-radio>
		<el-radio v-model="radio" label="" value="2">BackEnd</el-radio>
		<el-radio v-model="radio" label="" value="3">Service</el-radio>

		<!-- 单选框 - 事件绑定 -->
		<h3>Radios - Event Binding</h3>
		<el-radio v-model="radio2" label="" value="a" @change="radioChange"
			>FrontEnd</el-radio
		>
		<el-radio v-model="radio2" label="" value="b" @change="radioChange"
			>BackEnd</el-radio
		>
		<el-radio v-model="radio2" label="" value="c" @change="radioChange"
			>Service</el-radio
		>
		<!-- 单选框组, 对应 radio group, 只需要绑定 el-radio-group 标签并定义该标签的事件 -->
		<!-- 当 group 下的 radio 选中更新，对应的value则会传递给事件，同时更新 v-model 绑定的变量 -->
		<h3>Radio Group</h3>
		<el-radio-group v-model="radio3" @change="radioGroupChange">
			<el-radio value="A">FrontEnd </el-radio>
			<el-radio value="B">BackEnd </el-radio>
			<el-radio value="C">Service </el-radio>
		</el-radio-group>

		<!-- 复选框 -->
		<h3>复选框</h3>
		<el-checkbox-group v-model="checked" @change="checkboxGroupChange">
			<el-checkbox value="1">FrontEnd </el-checkbox>
			<el-checkbox value="2">BackEnd </el-checkbox>
			<el-checkbox value="3">Service </el-checkbox>
		</el-checkbox-group>
	</div>
</template>

<script setup>
	import { ref } from "vue";

	// 单选框
	const radio = ref("3");
	const radio2 = ref("b"); // 双向绑定，当变量绑定多个标签时，变量会随着标签的选中而更改值
	const radio3 = ref("C");
	const checked = ref(["1", "2"]); // 复选框的双向绑定需要用list
	// 单选框事件: 触发事件的回调会传递对应单选框的 value 属性
	const radioChange = (val) => {
		console.log("radioChange", val);
	};

	// 单选框组事件
	const radioGroupChange = (val) => {
		console.log("radioGroupChange", val);
	};

	const checkboxGroupChange = (val) => {
		console.log("checkboxGroupChange", val);
	};
</script>

<style lang="scss" scoped></style>
