<template>
	<div>
		<h3>Tabs</h3>
		<!-- v-model: 绑定值，选中选项卡的 name，默认值是第一个 tab 的 name -->
		<el-tabs
			v-model="selectedName"
			@tab-click="tabClick"
			type="border-card"
		>
			<!-- label 表示 Tab 的标题 -->
			<el-tab-pane label="Tab 1" name="1">Tab Content 1</el-tab-pane>
			<el-tab-pane label="Tab 2" name="2">Tab Content 2</el-tab-pane>
			<el-tab-pane label="Tab 3" name="3">Tab Content 3</el-tab-pane>
		</el-tabs>

		<h3>Dynamic Generated Tabs</h3>
		<el-button @click="tabAdd">Add</el-button>

		<el-tabs
			v-model="selectedName"
			@tab-remove="tabRemove"
			closable
			type="card"
		>
			<el-tab-pane
				v-for="(value, key) in tab.arr"
				:key="value.name"
				:label="value.title"
				:name="value.name"
				>{{ value.content }}
			</el-tab-pane>
		</el-tabs>
	</div>
</template>

<script setup>
	import { ref, reactive } from "vue";

	// 默认选中的标签名称
	const selectedName = ref("2");

	// 选中标签触发的回调
	const tabClick = (tab, event) => {
		console.log("tab", tab.props, "event", event);
	};
    // tabs 对象
	const tab = reactive({
		arr: [
			{ name: "1", title: "Tab 1", content: "Content 1" },
			{ name: "2", title: "Tab 2", content: "Content 2" },
			{ name: "3", title: "Tab 3", content: "Content 3" },
		],
	});

    // 添加 Tab
    const tabAdd = () =>{
        let index =tab.arr.length;
        index++

        tab.arr.push({
            name: index,
            title: "Tab " + index,
            content: "Content " + index
        })
    }
    // 删除 Tab
    const tabRemove = (name) =>{
        // name 为触发删除事件的元素的 name 属性
        console.log("name", name)
        // 在 tab.arr list中找到 name 对应的对象的index
        const index = tab.arr.findIndex((value) =>{
            return value.name === name
        })
        tab.arr.splice(index, 1) //移除元素
    }
</script>

<style lang="scss" scoped></style>
