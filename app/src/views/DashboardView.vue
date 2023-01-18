<template>
  <NavBar />
  <main class="flex bg-blue-800">
    <section class="flex flex-row grow bg-red-500">
      <div class="w-1/4 bg-blue-500">
        <p>SIDEBAR</p>
      </div>
      <div class="flex-1 bg-green-500">
        <p>MAIN DASHBOARD</p>
        <tr>
          <td>JOB</td>
          <td>MONDAY</td>
          <td>TUESDAY</td>
          <td>WEDNESDAY</td>
          <td>THURSDAY</td>
          <td>FRIDAY</td>
          <td>SATURDAY</td>
          <td>SUNDAY</td>
        </tr>
        <tr v-for="(row, index1) in timesheet" :key="index1">
          <td>{{ index1 }}</td>
          <td v-for="(item, index2) in row" :key="index2">{{ item }}</td>
        </tr>
      </div>
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
  data() {
    return {
      timesheet: null,
    };
  },
  mounted() {
    fetch(this.$store.state.fastApiEnd + "/faketimesheet")
      .then((response) => response.json())
      .then((data) => (this.timesheet = data.timesheet));
  },
});
</script>
