<template>
    <div class="about">
        <Header />

        <h1 class="bg-gray-500 text-3xl font-bold">This is an about page</h1>
        <Footer />
    </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";
export default {
    name: "About",
    components: {
        Header,
        Footer,
    },
};
</script>
