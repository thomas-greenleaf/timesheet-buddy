<template>
  <div class="relative">
    <button
      class="profile border-solid w-12 h-12 rounded-[50%] bg-green-500 flex items-center justify-center"
      @click="dropdown"
    >
      <h1 class="text-4xl">{{ user.userName[0].toUpperCase() }}</h1>
    </button>
    <div
      class="absolute top-full right-0 w-[300px] bg-blue-500 flex flex-col items-center justify-center"
      v-if="dropdownActive"
    >
      <h1>{{ user.userName }}</h1>
      <div
        class="border-solid w-20 h-20 rounded-[50%] bg-green-500 flex items-center justify-center"
      >
        <h1 class="text-4xl">{{ user.userName[0].toUpperCase() }}</h1>
      </div>
      <router-link :to="'/user/' + user.userId">Go To Profile</router-link>
      <button @click="logout">Log Out</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
// import { mapMutations } from "vuex";

export default defineComponent({
  name: "ProfileWidget",
  data() {
    return {
      dropdownActive: false,
    };
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
  },
  methods: {
    // ...mapMutations(["logout"]),
    dropdown() {
      this.dropdownActive = !this.dropdownActive;
    },
    logout() {
      this.$store.commit("logout");
    },
  },
});
</script>

<style scoped></style>
