<template>
    <div>
        <div style="width: 100px; height: 30px; border: 1px solid">
            <!-- transfer a dynamic data using ':' -->
            <aside-item :isActive="curActive === 'dongman'" @active-event="curActive = 'dongman'"> 动漫 </aside-item>
        </div>
        <div style="width: 100px; height: 30px; border: 1px solid">
            <!-- transfer a dynamic data using ':' -->
            <aside-item :isActive="curActive === 'dianjing'" @active-event="curActive = 'dianjing'"> 电竞 </aside-item>
        </div>
    </div>
</template>

<script>
import asideItem from './components/aside-item.vue';
export default {
    data() {
        return {
            curActive: '',
        };
    },
    components: {
        asideItem,
    },

    methods: {},
};
</script>
<style scoped></style>
