import axios from 'axios';
export const HTTP = axios.create({
  baseURL: 'https://dog.ceo',
  headers: {
    "Access-Control-Allow-Origin": "*",
    'Content-Type': 'application/json; charset=utf-8'
  },
  responseType: 'json'
});