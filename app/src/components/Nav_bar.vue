<template>
    <v-app>
      <v-app-bar app class="align-center" color="primary" clipped-left>
        <v-spacer></v-spacer>
        <v-toolbar-title>Cryptography Project</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-app-bar>

      <v-navigation-drawer app class="sidebar" clipped>
        <v-list>
          <v-list-item v-for="link in links" :key="link" link router :to="link.route" >
            <v-list-item-content>
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
      { text: "Columnar Transposition", route: "/" },
      { text: "Vigenere Cipher", route: "/VigenereCipher" },
      { text: "Rail Fence Cipher", route: "/UnknownChpher" },
      { text: "RSA", route: "/RSA" },
    ],
  }),
};
</script>
