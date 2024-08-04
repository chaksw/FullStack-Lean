<template>
    <div>
        <Header />
        <!-- <router-view></router-view> -->
        <router-view />
        <Footer />
    </div>
</template>

<script setup>
// 2. 共享组件: 共享组件是每个视图公用的，不需要进行路由嵌套，只需要在父组件视图中导入并在template中调用即可
import Header from "../components/header.vue";
import Footer from "../components/footer.vue";
</script>

<style lang="scss" scoped></style>
