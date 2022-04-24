<template>
    <v-app>
      <v-app-bar app color="primary" clipped-left  height="64">
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
        <v-toolbar-title class="font-weight-bold">Cryptography Project</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-app-bar>

      <v-navigation-drawer app class="sidebar" clipped v-model="drawer"
        temporary width="296" height="100%">
        <v-list shaped>
          <v-list-item class="mb-2">
            <v-icon class="primary--text" @click="drawer = false">mdi-chevron-left</v-icon>
            <v-toolbar-title class="primary--text font-weight-bold ml-8">Cryptography Project</v-toolbar-title>
          </v-list-item>
          <v-divider class="my-2 mx-4 primary"></v-divider>
          <v-list-item v-for="link in links" :key="link" link router :to="link.route" active-class="primary--text text--accent-4 mx-4">
            <v-list-item-content >
              <v-list-item-title class="white--text">{{ link.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main>
        <router-view />
      </v-main>
    </v-app>
</template>

<script>
export default {
  data: () => ({
    links: [
      { text: "Columnar Transposition", route: "/app/ColumnarTransposition" },
      { text: "Vigenere Cipher", route: "/app/VigenereCipher" },
      { text: "Rail Fence Cipher", route: "/app/RailFence" },
      { text: "RSA", route: "/app/RSA" },
    ],
    drawer: false,
  }),
};
</script>
