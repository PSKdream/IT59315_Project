import random
import math
import sympy


class RSA:
    primeNumber = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                   67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                   157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
                   251, 257]

    def __init__(self):
        pass

    def getPrime(self, start, end):
        arr = []
        for i in range(start, end):
            if sympy.isprime(i):
                arr.append(i)
        return arr

    def verify(self, public_key, private_key):
        text = 'Test key 1234'
        enc = rsa.encrypt(public_key, text)
        dec = rsa.decrypt(private_key, enc)
        if text == dec:
            return True
        return False

    def generateKey(self):
        # ref : https://th.wikipedia.org/wiki/%E0%B8%AD%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%AD%E0%B8%AA%E0%B9%80%E0%B8%AD
        # ref : https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation
        p, q = random.sample(self.primeNumber, 2)
        n = p * q
        # ϕ(n) = ( p -1) x (q -1)
        phi = (p - 1) * (q - 1)

        prime_e = self.getPrime(2, phi)
        e = random.choice(prime_e)
        while math.gcd(phi, e) != 1:
            e = random.choice(prime_e)

        # e * d ≡ 1 mod ϕ(n)
        d = pow(e, -1, phi)
        if self.verify((e, n), (d, n)):
            return (e, n), (d, n)
        else:
            return self.generateKey()

    def encrypt(self, key, plain_text):
        e, n = key
        cipherText = ""
        for i in range(len(plain_text)):
            cipherText += chr(((ord(plain_text[i]) ** e) % n))
        return cipherText

    def decrypt(self, key, cipher_text):
        plainText = self.encrypt(key, cipher_text)
        return plainText


rsa = RSA()
correct = 0
for _ in range(100):
    text = "wertyuio;kjhgfxc vblkjfdw345 67iop;l,bvgyu"
    publicKey, privateKey = rsa.generateKey()
    # print("publicKey ", publicKey)
    # print("privateKey ", privateKey)
    en = rsa.encrypt(publicKey, text)
    de = rsa.decrypt(privateKey, en)
    if text == de:
        correct += 1
    else:
        print("publicKey ", publicKey)
        print("privateKey ", privateKey)

print('Acc: ', correct / 100)
