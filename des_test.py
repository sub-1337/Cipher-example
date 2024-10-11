


class DES:
    def convert_to_block64(self, bytes):
        while len(bytes) % 4 != 0: # Fill until divideble by 64 bits (8 * 4)
            bytes.append(0x0)
        bytes64 = []
        for i in range(0, len( bytes), 4):
            block64 =  bytes[0 + i] 
            block64 +=  bytes[1 + i] << 8
            block64 +=  bytes[2 + i] << 16
            block64 +=  bytes[3 + i] << 24
            bytes64.append(block64)
        return bytes64
    def permutationStart(self, block64):
        pass
    def round(self, block64, roundKey):
        pass 
    def encrypt(self, plain_text):
        plainBytes = bytearray(plain_text, "utf-8")
        bytes64 = self.convert_to_block64(plainBytes)
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