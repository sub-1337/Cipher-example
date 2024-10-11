


class DES:
    def permutationStart(self, block64):
        pass
    def round(self, block64, roundKey):
        pass 
    def encrypt(self, plain_text):
        plainBytes = bytearray(plain_text, "utf-8")
        while len(plainBytes) % 4 != 0: # Fill until divideble by 64 bits (8 * 4)
            plainBytes.append(0x0)

        plainBytes64 = []
        for i in range(0, len(plainBytes), 4):
            plainBytes64.append()
        pass
    def decrypt(self, cypher_text):
        pass



if __name__ == '__main__':
    testDes = DES()
    plain = "Hello world!"
    print(plain)
    encr = testDes.encrypt(plain)
    print(encr)
    plainBack = testDes.decrypt(encr)
    print(plainBack)