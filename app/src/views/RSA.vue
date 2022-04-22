<template>
  <div class="RSA">
    <v-container>
      <h1 class="text-center my-4">RSA Encryption</h1>
      <v-card rounded="lg" elevation="4" max-width="600" class="mx-auto mb-4 pa-4">
        <v-row class="mx-auto my-1">
          <h2 class="my-2">Public Key</h2>
          <v-spacer></v-spacer>
          <v-btn icon class="mt-2">
            <v-icon>mdi-content-copy</v-icon>
          </v-btn>
        </v-row>
        <v-textarea
          outlined
          auto-grow
          placeholder="Public key will appear here."
          readonly
        ></v-textarea>
        <v-row class="mx-auto my-1">
          <h2 class="mb-2">Private Key</h2>
          <v-spacer></v-spacer>
          <v-btn icon>
            <v-icon>mdi-content-copy</v-icon>
          </v-btn>
        </v-row>
        <v-textarea
          outlined
          auto-grow
          placeholder="Private key will appear here."
          readonly
        ></v-textarea>
        <h2 class="mb-2">Select Key Size (Bit)</h2>
        <v-select
          :items="items"
          outlined
          placeholder="Key Size (Bit)"
          v-model="item"
          @change="() => ChoosItem()"
        ></v-select>
        <v-btn class="white--text gnrkey" height="50">
          Generate Key Pair
        </v-btn>
        <v-divider class="grey my-6"></v-divider>
        <h2 class="mb-3">Enter Plain/Cipher Text</h2>
        <v-textarea
          outlined
          auto-grow
          :counter="200"
          :rules="inputRules"
          placeholder="Enter text here."
          @change="(e) => inputText(e)"
        ></v-textarea>
        <h2 class="mb-3">Enter Public/Private Key</h2>
        <v-textarea
          outlined
          auto-grow 
          placeholder="Paste key here."
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
        <!-- <v-textarea
          outlined
          auto-grow
          label="Input key value"
          @change="(e) => inputKey(e)"
        ></v-textarea>
        <v-textarea
          outlined
          auto-grow
          label="Result"
          readonly
          class="mb-3"
        ></v-textarea> -->
        <v-row-flex class="mx-auto">
          <v-btn class="white--text encrypt" height="50">
            Encrypt
          </v-btn>
          <v-btn class="white--text decrypt mx-2" height="50">
            Decrypt
          </v-btn>
        </v-row-flex>
      </v-card>
    </v-container>
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
          v => (v || '' ).length <= 200 || 'Text must be 200 characters or less.'
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
    },
    copyResult() {
      navigator.clipboard.writeText(this.textcipher);
    }
  }
};
</script>
