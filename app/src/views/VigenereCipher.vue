<template>
  <div class="VigenereCipher mt-4">
    <h1 class="text-center">Vigenere Cipher</h1>
    <v-card elevation="4" max-width="600" class="mx-auto my-4 pa-3">
      <v-textarea
        filled
        auto-grow
        label="Input plain text"
        class="mx-4 mt-4"
      ></v-textarea>
      <v-textarea
        filled
        auto-grow
        label="Input key value"
        class="mx-4"
      ></v-textarea>
      <v-textarea
        filled
        auto-grow
        label="Result"
        class="mx-4"
        disabled
      ></v-textarea>
      <!-- <v-text-field
        v-model="name"
        :rules="nameRules"
        label="Input plain text"
        class="mx-4"
        required
      ></v-text-field>
      <v-text-field
        label="Input key value"
        class="mx-4"
        required
      ></v-text-field>
      <v-text-field
        label="Result"
        class="mx-4"
        filled
        disabled
      ></v-text-field> -->
      <v-row class="ml-4 my-auto mb-4">
        <v-btn 
          color="#0061BB" 
          class="mr-4 white--text"
          width="265"
          height="50"
        >
        Encrypt
        </v-btn>
        <v-btn
          color="#FF4D4D"
          class="mr-4 white--text"
          width="265"
          height="50"
        >
        Decrypt
        </v-btn>
      </v-row>
    </v-card>
  </div>
</template>

<script>
  export default {
  }
</script>