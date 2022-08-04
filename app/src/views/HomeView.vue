<template>
  <NavBar />
  <main class="flex">
    <section class="flex flex-col grow items-center justify-center">
      <h1 class="text-6xl">Manage your time more effectively</h1>
      <p class="text-2xl py-8">
        Track how you spend your time to better plan for the future
      </p>
    </section>
  </main>
  <FooterStd />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import NavBar from "@/components/Navigation.vue";
import FooterStd from "@/components/Footer.vue";

export default defineComponent({
  name: "HomeView",
  components: {
    NavBar,
    FooterStd,
  },
});
</script>
