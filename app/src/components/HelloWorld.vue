<template>
  <nav>
    <v-app>
      <v-app-bar class="d-flax align-center" app color="primary">
        <v-spacer></v-spacer>
        <v-toolbar-title>Cryptography Project</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-app-bar>

      <v-navigation-drawer app class="sidebar">
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
  </nav>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    links: [
      { text: "Columnar Transposition", route: "/" },
      { text: "Vigenere Cipher", route: "/VigenereCipher" },
      { text: "Unknown Cipher", route: "/UnknownChpher" },
      { text: "RSA", route: "/RSA" },
    ],
    items: [
      ["mdi-email", "Inbox"],
      ["mdi-account-supervisor-circle", "Supervisors"],
      ["mdi-clock-start", "Clock-in"],
    ],
  }),
};
</script>
