import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
      themes: {
        light: {
          primary: '#FF9E45',
          secondary: '#b0bec5',
          decrypt: '#FF4D4D',
          encrypt: '#0061BB',
          sidebar: '#45413B',
        },
      },
    },
  })
