<template>
<nav>
  <v-app>
    <v-app-bar class="d-flax align-center" app color="primary">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" color="black"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-toolbar-title>Cryptography Project</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app absolutem bottom temporary>
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-orange--text text--accent-1"
        >
          <v-list-item>
            <v-list-item-title>Columnar Transposition</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Vigenere Cipher</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Unknown Cipher</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>RSA</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
  </nav>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    drawer: false
  }),
};
</script>
