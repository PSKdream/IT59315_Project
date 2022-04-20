<template>
  <div class="UnknownChpher pa-3">
    <h1 class="text-center my-5">Rail Fence Cipher</h1>
    <v-card rounded="lg" elevation="4" max-width="600" class="mx-auto pa-4">
      <v-textarea
        filled
        auto-grow
        label="Input plain text"
        @change="(e) => inputText(e)"
      ></v-textarea>
      <v-textarea
        filled
        auto-grow
        label="Input key value"
        @change="(e) => inputKey(e)"
      ></v-textarea>
      <v-textarea
        filled
        auto-grow
        label="Result"
        readonly
        :value = this.textcipher
      ></v-textarea>
      <v-row class="mx-auto pb-4 justify-space-between">
        <v-btn class="white--text encrypt" width="48.5%" height="50" @click="() => postValue()">
          Encrypt
        </v-btn>
        <v-btn class="white--text decrypt" width="48.5%" height="50">
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
    async postValue() {
      console.log(this.value);
      try {
        debugger
        this.textcipher = await PostService.postColumnarEncryp(this.value);
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
    }
  }
};
</script>
