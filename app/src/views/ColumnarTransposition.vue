<template>
  <div class="ColumnarTransposition mt-4">
    <h1 class="text-center">Columnar Transposition</h1>
    <v-card elevation="4" max-width="600" class="mx-auto my-4 pa-3">
      <v-textarea
        filled
        auto-grow
        label="Input plain text"
        class="mx-4 mt-4"
        v-model="this.value.text"
      ></v-textarea>
      <v-textarea
        filled
        auto-grow
        label="Input key value"
        class="mx-4"
        v-model="this.value.key"
      ></v-textarea>
      <v-textarea
        filled
        auto-grow
        label="Result"
        class="mx-4"
        readonly
      ></v-textarea>
      <v-row class="ml-4 my-auto mb-4">
        <v-btn class="mr-4 white--text encrypt" width="265" height="50" @click="() => postValue()">
          Encrypt
        </v-btn>
        <v-btn class="mr-4 white--text decrypt" width="265" height="50">
          Decrypt
        </v-btn>
      </v-row>
    </v-card>
    <img :src="image">
  </div>
</template>

<script>
import {HTTP} from '@/axios.js'
export default {
  data() {
    return {
      image: '',
      value: {      
        text: "",
        key:""
      }
    };
  },
  methods: {
    async postValue() {
      await HTTP.get('api/breeds/image/random')
      .then(res => {
      if (res.data.status == 'success') {
      this.image = res.data.message
      console.log(this.image);
      }
      })
      .catch(e => {
      console.log(e);
      });
      // let getnaja = await HTTP.get("/");
      // let res = await HTTP.post("/ColumnarTransposition/encrypt", this.value);
      // console.log(getnaja);
      // console.log(res);
    },
    PostText(e){
      debugger
      console.log(e.target.value);
    }
  },
};
</script>
