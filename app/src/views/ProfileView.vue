<template>
  <NavBar />
  <main class="flex-1">
    <section class="flex flex-col grow items-center justify-center">
      <h1 class="text-6xl">This is the Profile View</h1>
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
