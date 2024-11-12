<script setup></script>

<template>
	内容页
	<hr />
	<!-- 获取 url 的查询字符串参数 -->
	id: {{ $route.query.id }}
	<hr />
	id: {{ $route.query.title }}
</template>

<style scoped></style>
