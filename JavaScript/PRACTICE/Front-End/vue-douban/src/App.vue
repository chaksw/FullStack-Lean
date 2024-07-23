<template>
    <div>
        <div style="width: 250px">
            <title-menu :isActive="select" @active-event="setActive">
                <template #title>发现频道</template>
                <template #icon>&gt;</template>
            </title-menu>
        </div>
    </div>
</template>

<script>
import titleMenu from './components/title-menu.vue';
export default {
    data() {
        return {
            select: false,
        };
    },
    components: {
        titleMenu,
    },
    // provide: {
    //     isActive: '',
    // },

    methods: {
        setActive(e) {
            this.select = !this.select;
            console.log(this.select, e);
        },
    },
};
</script>
<style></style>
