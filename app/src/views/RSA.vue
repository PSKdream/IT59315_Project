<template>
  <div class="RSA">
    <v-container>
      <h1 class="text-center my-4">RSA Cipher</h1>
      <v-card
        rounded="lg"
        elevation="12"
        max-width="600"
        class="mx-auto mb-4 pa-4"
      >
        <h2 class="my-3">Select Key Size (Bit)</h2>
        <v-select
          :items="items"
          outlined
          placeholder="Key Size (Bit)"
          v-model="item"
        ></v-select>
        <v-btn class="white--text font-weight-black gnrkey mb-3" height="50" @click="() => ChoosItem()" :loading="loading">
          Generate Key Pair
        </v-btn>
        <v-row class="mx-auto my-1">
          <h2 class="my-2">Public Key</h2>
          <v-spacer></v-spacer>
          <v-btn icon class="mt-2" @click="copyPublic">
            <v-icon>mdi-content-copy</v-icon>
          </v-btn>
        </v-row>
        <v-textarea
          outlined
          auto-grow
          placeholder="Public key will appear here."
          :value = this.genkey.public_key
          readonly
        ></v-textarea>
        <v-row class="mx-auto my-1">
          <h2 class="mb-2">Private Key</h2>
          <v-spacer></v-spacer>
          <v-btn icon @click="copyPrivate">
            <v-icon>mdi-content-copy</v-icon>
          </v-btn>
        </v-row>
        <v-textarea
          outlined
          auto-grow
          placeholder="Private key will appear here."
          :value = this.genkey.private_key
          readonly
        ></v-textarea>
        <v-divider class="grey mt-2 mb-6"></v-divider>
        <h2 class="mb-3">Enter Plain/Cipher Text</h2>
        <v-textarea
          outlined
          auto-grow
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
          :value=this.textcipher
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
import PostService from "../Service.js";
export default {
  data() {
    return {
      value: {
        text: "",
        key: "",
      },
      textcipher: "",
      genkey: "",
      items: ["512", "1024", "2048", "4096"],
      item: "",
      loading: false,
    };
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
    inputText(e) {
      this.value.text = e;
    },
    inputKey(e) {
      this.value.key = e;
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
    // async ChoosItem() {
    //   console.log(this.item);
    //   let genkey = await PostService.postRSAGen({ keySize: this.item });
    //   console.log(genkey);
    // },
    async ChoosItem() {
      console.log(this.genkey);
      this.loading = true;
      try {
        this.genkey = await PostService.postRSAGen({ keySize: this.item });
        this.loading = false;
      } catch (err) {
        this.error = err;
        console.log(err);
        this.loading = false;
      }
    },
    copyResult() {
      navigator.clipboard.writeText(this.textcipher);
    },
    copyPrivate() {
      navigator.clipboard.writeText(this.genkey.private_key);
    },
    copyPublic() {
      navigator.clipboard.writeText(this.genkey.public_key);
    }
  },
};
</script>
