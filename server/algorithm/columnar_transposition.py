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
        print(p)
        c = p.T.flatten()

        return ''.join(c)

    def decrypt(self, cipher_text: str, key: str = '1,2,3'):
        key = self.get_key(key)  # num of col
        c = list(cipher_text)
        n = len(key)
        m = math.ceil(len(c) / n)
        c_n = len(c)
        arr = np.full((m, len(key)), '')
        start, end = 0, 0
        for ind, text in enumerate(key):
            if text-1 >= c_n % (m - 1):
                end = m-1
                temp = c[start:end]
                c = c[end:]
            else:
                end = m
                temp = c[start:end]
                c = c[end:]
            arr[:len(temp), ind] = temp

        p = arr[:, np.argsort(key)].flatten()
        return ''.join(p)


# obj = ColumnarTransposition()
# key = '2,1,3'
# en = obj.encrypt('PanyapiwatInstitute', key)
# print(obj.decrypt(en, key))
