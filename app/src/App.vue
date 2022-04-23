<template>
  <v-app>
    <Navbar/>
    <particleBG/>
  </v-app>
</template>

<script>
import Navbar from './components/Nav_bar.vue';


export default {
  components: { Navbar },
  name: "App",
  data: () => ({
  }),
};
</script>
