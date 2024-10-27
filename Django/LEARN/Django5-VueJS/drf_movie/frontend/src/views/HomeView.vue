<template>
    <div
        id="container"
        class="text-white text-sm bg-primary-300 min-h-screen pb-4">
        <Header />
        <MoiveList />
        <Footer />
    </div>
    <!-- <div class="home">This is home page</div> -->
</template>

<script>
// @ is an alias to /src
import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";
import MoiveList from "@/components/MoiveList.vue";
export default {
    name: "HomeView",
    components: {
        Header,
        MoiveList,
        Footer,
    },
};
</script>
