import math
import random, sys, os, sympy
from Crypto.Cipher import PKCS1_OAEP
import binascii
import Crypto

def main():
    makeKeyFiles('RSA_demo', 32)


def generateLargePrime(keysize=32):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if sympy.isprime(num):
            return num


def generateKey(keySize):
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    print('Generating p prime...')
    p = generateLargePrime(keySize)
    print('Generating q prime...')
    q = generateLargePrime(keySize)
    n = p * q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if sympy.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e.
    print('Calculating d that is mod inverse of e...')
    d = pow(e, -1, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    return (publicKey, privateKey)

def encrypt(key, plain_text):
    e, n = key
    cipherText = ""
    for i in range(len(plain_text)):
        cipherText += chr((math.pow(ord(plain_text[i]), e) % n))
    return cipherText

def makeKeyFiles(name, keySize):
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit(
            'WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (
                name, name))
    publicKey, privateKey = generateKey(keySize)
    # encryption
    msg = 'A message for encryption'
    encryptor = PKCS1_OAEP.new(publicKey)
    encrypted = encryptor.encrypt(msg)
    print("Encrypted:", binascii.hexlify(encrypted))

# If makeRsaKeys.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
