import numpy as np
import math


class ColumnarTransposition:

    def getKey(self, key):
        return np.array([int(i) for i in key.split(',')])

    def encode(self, plan_text, key='1,2,3'):
        key = self.getKey(key) - 1  # num of col
        p = list(plan_text)

        n = len(key)
        while len(p) % n != 0:
            p.append('')

        p = np.reshape(p, (-1, n))
        p = p[:, key]
        c = p.T.flatten()

        return ''.join(c)

    def decode(self, cipher_text, key='1,2,3'):
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


x = ColumnarTransposition()
key = '2,1,3,4'
ans = x.encode('abcdefj', key)
print('encode : ', ans)
ans = x.decode(ans, key)
print('decode : ', ans)
