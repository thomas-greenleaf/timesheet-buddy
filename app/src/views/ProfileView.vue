<template>
  <NavBar />
  <main class="flex-1">
    <section class="flex flex-col grow items-center justify-center">
      <h1 class="text-6xl">Welcome {{ this.$store.state.user.userName }}</h1>
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
  mounted() {
    // const url = new URL("http://localhost:8081");
    fetch(
      `${this.$store.state.fastApiEnd}/user/${this.$store.state.user.userId}`
    ).then((response) => response.json());
    // .then((data) => (this.userInfo = data.userInfo));
  },
});
</script>
