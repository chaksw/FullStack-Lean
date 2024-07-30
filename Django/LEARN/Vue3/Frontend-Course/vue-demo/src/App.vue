<script>
// 1. import component
import ArrtibBinding from "./components/ArrtibBinding.vue";
import IfDemo from "./components/ifDemo.vue";
import ListDemo from "./components/listDemo.vue";
import KeyDemo from "./components/keyDemo.vue";
import EventDemo1 from "./components/eventDemo1.vue";
import EventDemo2 from "./components/eventDemo2.vue";
import EventDemo3 from "./components/eventDemo3.vue";
import EventDemo4 from "./components/eventDemo4.vue";
import EventDemo5 from "./components/eventDemo5.vue";
import EventDemo6 from "./components/eventDemo6.vue";
import ArrayList from "./components/ArrayList.vue";
import ComputedDemo from "./components/ComputedDemo.vue";
import ClassDemo from "./components/ClassDemo.vue";
import StyleDemo from "./components/StyleDemo.vue";
import WatchersDemo from "./components/WatchersDemo.vue";
import ModelBinding from "./components/ModelBinding.vue";
import TemplateRefs from "./components/TemplateRefs.vue";
import ComponentBasic from "./components/ComponentBasic.vue";

export default {
    // 2. injection of component
    components: {
        ComponentBasic
    }
}

</script>

<template>
    <!-- 3. display component -->
    <!-- <ArrtibBinding /> -->
    <!-- <IfDemo /> -->
    <!-- <ListDemo /> -->
    <!-- <KeyDemo /> -->
    <!-- <EventDemo1 /> -->
    <!-- <EventDemo2 /> -->
    <!-- <EventDemo3 /> -->
    <!-- <EventDemo4 /> -->
    <!-- <EventDemo5 /> -->
    <!-- <EventDemo6 /> -->
    <!-- <ArrayList /> -->
    <!-- <ComputedDemo /> -->
    <!-- <ClassDemo /> -->
    <!-- <StyleDemo /> -->
    <!-- <WatchersDemo /> -->
    <!-- <ModelBinding /> -->
    <!-- <TemplateRefs/> -->
    <!-- <ComponentBasic/> -->
    <!-- this format also work -->
    <component-basic/>
</template>
