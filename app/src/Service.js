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

    static postColumnar() {
        // eslint-disable-next-line no-async-promise-executor
        return new Promise(async (resolve, reject) => {
            try {
                const res = await axios.post(url + "ColumnarTransposition/encrypt", {
                    "text": "buffalo view",
                    "key": "2,3,1"
                },
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