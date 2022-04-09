class OneTimePad:
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self,):
        pass

    def encode(self, plan_text:str, key:str):
        if plan_text is None and key is None:
            raise Exception('Data is None')
        elif len(plan_text) != len(key):
            raise Exception('Length data not match')


    def decode(self, cipher_text, key='1,2,3'):
        pass


otp = OneTimePad()