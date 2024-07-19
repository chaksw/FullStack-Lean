<template>
    <h3>Main</h3>
    <SearchComponent @search-event="getSearch" />
    <p>Search Result: {{ search }}</p>
</template>
<script>
import SearchComponent from "./SearchComponent.vue";
export default {
    data() {
        return { search: "" };
    },
    components: {
        SearchComponent,
    },
    methods: {
        getSearch(data) {
            this.search = data;
        },
    },
};
</script>
