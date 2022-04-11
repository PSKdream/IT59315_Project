import numpy as np
class RailFence:
    def encrypt(self, cipher_text, k):
        c = np.full((k,len(cipher_text)),'')
        row = 0
        tig = False
        for i, text in enumerate(cipher_text):
            if row == 0 or row == k-1:
                tig = not tig
            c[row, i] = text
            if tig:
                row += 1
            else:
                row -= 1
        return ''.join(c.flatten())

    def decrypt(self,cipher, key):
        # create the matrix to cipher
        # plain text key = rows ,
        # length(text) = columns
        # filling the rail matrix to
        # distinguish filled spaces
        # from blank ones
        rail = np.full((key, len(cipher)), '')
        # to find the direction
        dir_down = None
        row, col = 0, 0

        # mark the places with '*'
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            # place the marker
            rail[row][col] = '*'
            col += 1

            # find the next row
            # using direction flag
            if dir_down:
                row += 1
            else:
                row -= 1

        index = 0
        ind = np.where(rail == '*')
        for i,j in zip(ind[0],ind[1]):
            # print(i)
            if index < len(cipher):
                rail[i][j] = cipher[index]
            index += 1
        return "".join(rail.T.flatten())
