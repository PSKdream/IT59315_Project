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
      ></v-textarea>
      <v-select
        :items="items"
        filled
        label="Key Size (Bits)"
      ></v-select>
      <v-textarea
        filled
        auto-grow
        label="Input key value"
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
export default {
  data() {
    return {
      inputRules: [
          v => (v || '' ).length <= 200 || 'Plain text must be 200 characters or less.'
      ],
      items: ['512', '1024', '2048', '4096'],
    }
  },
};
</script>
