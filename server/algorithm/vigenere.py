class Vigenere:

    def encrypt(self, plan_text: str, key: str):
        if plan_text is None and key is None:
            raise Exception('Data is None')
        c = ''
        for index, p in enumerate(plan_text.upper()):
            if p == ' ':
                c += ' '
                continue
            p, k = ord(p) - 65, ord(key[index % len(key)].upper()) - 65
            c += chr(((p + k) % 26) + 65)
        return c

    def decrypt(self, cipher_text: str, key: str):
        if cipher_text is None and key is None:
            raise Exception('Data is None')
        c = ''
        for index, p in enumerate(cipher_text.upper()):
            if p == ' ':
                c += ' '
                continue
            p, k = ord(p) - 65, ord(key[index % len(key)].upper()) - 65
            c += chr(((p - k) % 26) + 65)
        return c
