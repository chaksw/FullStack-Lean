<template>
    <div class="container">{{ message }}</div>
</template>
<script>
export default {
    data() {
        return {
            message: 'message',
        }
    }
}
</script>
<!-- scope: 让当前样式只在当前组件中生效 -->
<style>
.container{
    font-size: 30px;
    color: #569856
}
</style>