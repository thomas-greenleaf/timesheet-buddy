<template>
  <button :class="['px-6', 'border-solid border-2', 'rounded-lg', color]">
    {{ text }}
  </button>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "StdButton",
  props: {
    text: String,
    color: String,
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
