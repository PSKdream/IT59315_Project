<template>
  <v-app>
    <hello-world/>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  components: { HelloWorld },
  name: "App",
  data: () => ({
  }),
};
</script>
