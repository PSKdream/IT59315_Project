<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <!-- <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        /> -->
      </div>

      <v-spacer></v-spacer>
    </v-app-bar>

     <form>
    <v-container fluid>
    <v-text-field
      label="Input a plain text"
      required
    ></v-text-field>

    <v-text-field
      name="text_EN"
      label="Input a plain text"
      required
    ></v-text-field> 

      <v-text-field
      name="kvalue"
      label="Input a K value"
      required
    ></v-text-field> 

    <v-textarea
      name="Result"
      filled
      label="Result"
      auto-grow
    ></v-textarea>

    <v-btn
      class="mr-4"
      @click="submit"
    >
      submit
    </v-btn>
    <v-btn @click="clear">
      clear
    </v-btn>
    </v-container>
  </form>
  </v-app>
  
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
