<template>
    <div class="title-menu">
        <aside-item :isActive="isActive" @active-event="$emit('activeEvent', '456')">
            <div class="inner">
                <div class="left"><slot name="title"></slot></div>
                <div class="right"><slot name="icon"></slot></div>
            </div>
        </aside-item>
    </div>
</template>

<script>
import asideItem from './aside-item.vue';
export default {
    date() {
        return {};
    },
    components: {
        asideItem,
    },
    props: {
        isActive: {
            type: Boolean,
            // required: true,
            default: true,
        },
    },
};
</script>

<style scoped>
.title-menu {
    width: 100%;
    height: 46px;
    line-height: 46px;
}

.inner {
    padding: 0 20px;
}

.left {
    color: 212121;
    float: left;
    font-size: 16px;
    font-weight: 500;
}
.right {
    float: right;
    font-size: 12px;
    color: #999;
}
</style>
