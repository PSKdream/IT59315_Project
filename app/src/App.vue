<template>
  <v-app>
    <v-app-bar class="d-flax align-center" app color="primary">
      <v-app-bar-nav-icon color="black"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-toolbar-title >Cryptography Project</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
