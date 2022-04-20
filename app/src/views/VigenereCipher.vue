<template>
  <div class="UnknownChpher mt-4">
    <h1 class="text-center">Vigenere Cipher</h1>
    <v-card elevation="4" max-width="600" class="mx-auto my-4 pa-3">
      <v-textarea
          filled
          auto-grow
          label="Input plain text"
          class="mx-4 mt-4"
          @change="(e) => inputText(e)"
      ></v-textarea>
      <v-textarea
          filled
          auto-grow
          label="Input key value"
          class="mx-4"
          @change="(e) => inputKey(e)"
      ></v-textarea>
      <v-textarea
          filled
          auto-grow
          label="Result"
          class="mx-4"
          readonly
          :value = this.textcipher
      ></v-textarea>
      <v-row class="ml-4 my-auto mb-4">
        <v-btn class="mr-4 white--text encrypt" width="265" height="50" @click="() => postValueEn()">
          Encrypt
        </v-btn>
        <v-btn class="mr-4 white--text decrypt" width="265" height="50" @click="() => postValueDe()">
          Decrypt
        </v-btn>
      </v-row>
    </v-card>
  </div>
</template>

<script>
import PostService from '../Service.js'

export default {
  data() {
    return {
      value: {
        text: "",
        key: ""
      },
      textcipher: ""
    };
  },
  methods: {
    async postValueEn() {
      console.log(this.value);
      try {
        this.textcipher = await PostService.postVigenereEncryp(this.value);
      } catch (err) {
        this.error = err;
        console.log(err);
      }
    },
    inputText(e){
      this.value.text = e
    },
    inputKey(e){
      this.value.key = e
    },
    async postValueDe() {
      console.log(this.value);
      try {
        this.textcipher = await PostService.postVigenereDecryp(this.value);
      } catch (err) {
        this.error = err;
        console.log(err);
      }
    }
  }
};
</script>
