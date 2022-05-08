import numpy as np
import math


class ColumnarTransposition:

    def __init__(self):
        pass

    def get_key(self, key):
        return np.array([int(i) for i in key.split(',')])

    def encrypt(self, plan_text: str, key: str = '1,2,3'):
        key = self.get_key(key) - 1  # num of col
        # print(key)
        p = list(plan_text)

        n = len(key)
        while len(p) % n != 0:
            p.append('')

        p = np.reshape(p, (-1, n))

        p = p[:, key]
        # print(p, '------------')
        c = p.T.flatten()

        return ''.join(c)

    def decrypt(self, cipher_text: str, key: str = '1,2,3'):
        key_ = self.get_key(key)  # num of col

        msg_len = len(cipher_text)
        msg_indx = 0

        col = len(key_)
        row = math.ceil(msg_len / col)

        arr = np.full((row, len(key_)), '')

        msg_frac = msg_len % col

        for curr_key in key_:
            curr_idx = curr_key - 1
            for j in range(row):
                if msg_frac != 0 and j == row - 1 and curr_key > msg_frac:
                    continue
                arr[j, curr_idx] = cipher_text[msg_indx]
                msg_indx += 1

        return ''.join(arr.flatten())


# obj = ColumnarTransposition()
# key = '1,3,2'  # '2,3,1'
# en = obj.encrypt('pongsakorn', key)
# print(obj.decrypt(en, key))
