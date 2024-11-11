<script setup lang="js">
import { Button } from '@/components/ui/button';
import NavMenu from '@/components/NavMenu.vue'

</script>

<template>
    <div>
		<!-- <NavMenu/> -->
        <router-view />
        <Button class="m-4">Click me</Button>
    </div>
</template>
