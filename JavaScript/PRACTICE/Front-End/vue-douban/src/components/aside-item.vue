<template>
    <div class="item" :class="{ active: isActive }" @click="handleClick">
        <slot></slot>
    </div>
</template>

<script>
export default {
    props: {
        isActive: {
            type: Boolean,
            // required: true,
            default: true,
        },
    },
    // inject: ['isActive'],
    methods: {
        handleClick() {
            this.$emit('activeEvent', 123);
        },
    },
};
</script>

<style scoped>
.item {
    cursor: pointer;
    transition: 0.2s;
}
.active {
    background: #e7e7e7;
}

.item:hover {
    background: red;
}
</style>
