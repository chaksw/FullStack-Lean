<template>
	<div>
		<h2>Input</h2>
		<div style="width: 300px">
			<h3>Input</h3>
			<el-input v-model="name" clearable placeholder="请输入用户名" />

			<h3>PassWord</h3>
			<el-input
				v-model="password"
				show-password
				placeholder="请输入密码"
			/>

			<h3>Text Area</h3>
			<!-- rows 表示默认显示多少行 -->
			<el-input type="textarea" v-model="content" rows="2" />

			<h3>Limit Input</h3>
			<!-- maxlength="10" 表示文本最大长度 show-word-limit 表示显示当前文本最大长度比 -->
			<el-input v-model="name" maxlength="10" show-word-limit />

			<h3>Limit Text</h3>
			<el-input
				type="textarea"
				v-model="content"
				maxlength="20"
				rows="3"
				show-word-limit
			/>

			<h3>Define Size</h3>
			<el-input size="large" />
			<el-input size="small" />

            <h3>Prepostion</h3>
			<el-input v-model="url">
                <template #prepend>https://</template>
            </el-input>

			<h3>Postposition</h3>
			<el-input v-model="email">
                <template #append>@outlook.com</template>
            </el-input>

            <h3>Prepostion & Postposition</h3>
			<el-input v-model="url2">
                <template #prepend>https://</template>
                <template #append>@outlook.com</template>
            </el-input>
            
            <!-- 结合下拉选择框的输入搜索框，实现利用下拉框文本来限制搜索条件 -->
            <h3>Extension of Prepostion & Postposition</h3>
            <el-input place-holder="请输入课程名称">
                <template #prepend>
                    <el-select v-model="selected" placeholder="请选择" style="width: 100px;">
                        <el-option label="frontend" value="1"></el-option>
                        <el-option label="backend" value="2"></el-option>
                        <el-option label="service" value="3"></el-option>
                    </el-select>
                </template>
                <template #append>
                    <el-button>
                        <el-icon><Search/></el-icon>
                    </el-button>
                </template>
            </el-input>
            
		</div>
	</div>
</template>

<script setup>
	import { ref } from "vue";
	const name = ref("");
	const password = ref("");
	const content = ref("Content");
    const url = ref('runsheng.wu@outlook.com')
    const url2 = ref('chaksw')
    const email = ref('runsheng.wu')

    const selected = ref('2')
</script>


<style lang="scss" scoped></style>
