import numpy as np
import math


class ColumnarTransposition:

    def getKey(self, key):
        return np.array([int(i) for i in key.split(',')])

    def encrypt(self, plan_text: str, key: str = '1,2,3'):
        # print(type(self))
        key = self.getKey(key) - 1  # num of col
        # print(key)
        p = list(plan_text)

        n = len(key)
        while len(p) % n != 0:
            p.append('')

        p = np.reshape(p, (-1, n))
        p = p[:, key]
        c = p.T.flatten()

        return ''.join(c)

    def decrypt(self, cipher_text: str, key: str = '1,2,3'):
        key = self.getKey(key) - 1  # num of col
        c = list(cipher_text)
        n = len(key)
        m = math.ceil(len(c) / n)

        c_n = len(c)
        for ind, index in enumerate(reversed(key)):
            if index > (c_n % n) - 1:
                c.insert(((n - ind) * m) - 1, '')

        c = np.reshape(c, (-1, n), order='F')
        p = c[:, key].flatten()

        return ''.join(p)

