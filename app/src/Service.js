import axios from "axios";

const url = "/api/";

class PostService {
    static getHello() {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.get(url, {useCredentails: true});
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }
    static postColumnarEncryp(temdata) {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "ColumnarTransposition/encrypt", temdata
                // axiosConfig
                );
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }

    static postColumnarDecryp(temdata) {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "ColumnarTransposition/decrypt", temdata
                // axiosConfig
                );
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }

    static postVigenereEncryp(temdata) {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "Vigenere/encrypt", temdata
                // axiosConfig
                );
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }

    static postVigenereDecryp(temdata) {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "Vigenere/decrypt", temdata
                // axiosConfig
                );
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }

    static postRailFenceEncryp(temdata) {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "RailFence/encrypt", temdata
                // axiosConfig
                );
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }

    static postRailFenceDecryp(temdata) {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "RailFence/decrypt", temdata
                // axiosConfig
                );
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }

    static postRSAGen(temdata) {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "RSA/GenerateKey", temdata
                // axiosConfig
                );
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }

    static postRSAEncryp(temdata) {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "RSA/encrypt", temdata
                // axiosConfig
                );
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }

    static postRSADecryp(temdata) {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "RSA/decrypt", temdata
                // axiosConfig
                );
                const data = res.data;
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
    }
}

export default PostService;