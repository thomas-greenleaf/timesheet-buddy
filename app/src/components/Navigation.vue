<template>
  <header>
    <nav class="py-8 flex">
      <div class="px-8 flex grow flex-row">
        <router-link to="/" class="pl-8">
          <h1 class="text-4xl">Brand Logo</h1>
        </router-link>
      </div>
      <div class="px-8 flex space-x-4 justify-items-right">
        <StdButton
          v-if="!$auth0.isAuthenticated"
          text="SIGN IN"
          color="bg-blue-400"
          :func="login"
        />
        <ProfileWidget userName="tgreenleaf" />
      </div>
    </nav>
  </header>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import StdButton from "@/components/StandardButton.vue";
import ProfileWidget from "@/components/ProfileWidget.vue";
import { useAuth0 } from "@auth0/auth0-vue";

export default defineComponent({
  name: "NavBar",
  props: {
    loggedIn: Boolean,
  },
  components: {
    StdButton,
    ProfileWidget,
  },
  setup() {
    const auth0 = useAuth0();
    return {
      login: () => {
        auth0.loginWithPopup();
      },
    };
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
