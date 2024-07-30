<template>
    <h3>Component Event</h3>
    <!-- line component event (some-event)(kebab-case) to listener  -->
    <Child @some-event="getHandle" />
    <p>{{ message }}</p>
</template>
<script>
import Child from "./Child.vue";
export default {
    data() {
        return {
            message: "",
        };
    },
    components: {
        Child,
    },
    methods: {
        // define logic for listener event, here argument link to data from this.$emit
        getHandle(data) {
            console.log("triggle child event", data);
            this.message = data;
        },
    },
};
</script>
