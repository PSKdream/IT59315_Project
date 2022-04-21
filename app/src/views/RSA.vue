<template>
  <div class="RSA pa-3">
    <h1 class="text-center my-5">RSA</h1>
    <v-card rounded="lg" elevation="4" max-width="600" class="mx-auto pa-4">
      <v-textarea
        filled
        auto-grow
        :counter="200"
        :rules="inputRules"
        label="Input plain text"
        @change="(e) => inputText(e)"
      ></v-textarea>
      <v-select
        :items="items"
        filled
        label="Key Size (Bits)"
        v-model="item"
        @change="() => ChoosItem()"
      ></v-select>
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
      ></v-textarea>
      <v-row class="mx-auto pb-4 justify-space-between">
        <v-btn class="white--text encrypt" width="48.5%" height="50">
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
      textcipher: "",
      inputRules: [
          v => (v || '' ).length <= 200 || 'Plain text must be 200 characters or less.'
      ],
      items: ['512', '1024', '2048', '4096'],
      item: ""
    }
  },
  methods: {
    async postValueEn() {
      console.log(this.value);
      try {
        this.textcipher = await PostService.postRSAEncryp(this.value);
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
        this.textcipher = await PostService.postRSADecryp(this.value);
      } catch (err) {
        this.error = err;
        console.log(err);
      }
    },
    async ChoosItem(){
      console.log(this.item);
      let genkey = await PostService.postRSAGen({"keySize":this.item});
      console.log(genkey);
    }
  }
};
</script>
