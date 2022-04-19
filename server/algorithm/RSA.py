import random
import math
import sympy
import hashlib


class RSA:
    primeNumber = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                   61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
                   131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
                   193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
                   263, 269, 271]

    def __init__(self):
        pass

    def getPrime(self, start, end):
        arr = []
        for i in range(start, end):
            if sympy.isprime(i):
                arr.append(i)
        return arr

    def verify(self, publicKey, privateKey):
        try:
            text = 'text 123'
            n = self.encrypt(text, publicKey)
            dec = self.decrypt(n, privateKey)
            if text == dec:
                return True
            return False
        except:
            return False

    def generateLargePrime(self, keysize=32):
        while True:
            num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
            if sympy.isprime(num):
                return num

    def generateKey(self, keySize):
        # ref : https://th.wikipedia.org/wiki/%E0%B8%AD%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%AD%E0%B8%AA%E0%B9%80%E0%B8%AD
        # ref : https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation
        # p, q = random.sample(self.primeNumber, 2)
        p = self.generateLargePrime(keySize)
        q = self.generateLargePrime(keySize)
        n = p * q
        # ϕ(n) = ( p -1) x (q -1)
        phi = (p - 1) * (q - 1)
        # prime_e = self.getPrime(2, phi)
        e = None
        while e == None or math.gcd(phi, e) != 1:
            e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))

        # e * d ≡ 1 mod ϕ(n)
        d = pow(e, -1, phi)
        public_key, private_key = {'e': e, "n": n}, {"d": d, 'n': n}
        if self.verify(public_key, private_key):
            return public_key, private_key
        else:
            return self.generateKey(keySize)
        return public_key, private_key

    def encrypt(self, plain_text, key):
        if 'e' in key.keys():
            e, n = key['e'], key['n']
        elif 'd' in key.keys():
            e, n = key['d'], key['n']
        int_str = ''
        for i in plain_text:
            int_str += str(ord(i))
        return pow(int(int_str), e, n)

    def decrypt(self, cipher_text, key):
        if 'e' in key.keys():
            e, n = key['e'], key['n']
        elif 'd' in key.keys():
            e, n = key['d'], key['n']
        int_str = pow(cipher_text, e, n)
        int_str = list(str(int_str))
        int_str.reverse()
        plainText = ''
        while int_str != []:
            unicode = ''
            if int_str[-1] == '1':
                for _ in range(3):
                    unicode += int_str.pop()
            else:
                for _ in range(2):
                    unicode += int_str.pop()
            plainText += chr(int(unicode))
        return plainText

# rsa = RSA()
# publicKey, privateKey = rsa.generateKey(1024)
# print(publicKey, privateKey)
# text = 'From the augmentation, a total of 1,225 images were obtained and were divided into 858 training sets, 245 valid sets, and 122 test sets. The images training set are used to train YOLO-X and YOLO-R mod'
# n = rsa.encrypt(text, publicKey)
# n = rsa.decrypt(n, privateKey)
# print(n==text)
# x = rsa.verify(publicKey, privateKey)
# print(str(publicKey[0]), int(str(publicKey[0]), 16))
# correct = 0
# for _ in range(100):
#     text = "wertyuio;kjhgfxc vblkjfdw345 67iop;l,bvgyu"
#     publicKey, privateKey = rsa.generateKey()
#     # print("publicKey ", publicKey)
#     # print("privateKey ", privateKey)
#     en = rsa.encrypt(publicKey, text)
#     de = rsa.decrypt(privateKey, en)
#     if text == de:
#         correct += 1
#     else:
#         print("publicKey ", publicKey)
#         print("privateKey ", privateKey)
#
# print('Acc: ', correct / 100)
