<template>
  <div class="UnknownChpher">
    <particleBG></particleBG>
    <v-container>
      <v-card rounded="lg" elevation="12" max-width="600" class="mx-auto mb-4 pa-4">
        <h1 class="text-center my-4">Vigenere Cipher</h1>
        <v-divider class="grey mt-2 mb-6"></v-divider>
        <h2 class="my-3">Enter Plain/Cipher Text</h2>
        <v-textarea
          outlined
          auto-grow
          placeholder="Enter text here."
          @change="(e) => inputText(e)"
        ></v-textarea>
        <h2 class="mb-3">Enter Key</h2>
        <v-textarea
          outlined
          auto-grow
          placeholder="Enter key here."
          @change="(e) => inputKey(e)"
        ></v-textarea>
        <v-row class="mx-auto my-1">
          <h2 class="mb-2">Result</h2>
          <v-spacer></v-spacer>
          <v-btn icon @click="copyResult">
            <v-icon>mdi-content-copy</v-icon>
          </v-btn>
        </v-row>
        <v-textarea
          outlined
          auto-grow 
          placeholder="Result will appear here."
          :value = this.textcipher
          readonly
        ></v-textarea>
        <v-row-flex class="mx-auto">
          <v-btn class="white--text font-weight-black encrypt" height="50" @click="() => postValueEn()">
            Encrypt
          </v-btn>
          <v-btn class="white--text font-weight-black decrypt mx-2" height="50" @click="() => postValueDe()">
            Decrypt
          </v-btn>
        </v-row-flex>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import PostService from '../Service.js'
import particleBG from "../components/particleBG.vue";

export default {
  components: {particleBG},
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
    },
    copyResult() {
      navigator.clipboard.writeText(this.textcipher);
    }
  }
};
</script>
