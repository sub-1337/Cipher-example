


class DES:
    def encrypt(self, plain_text):
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