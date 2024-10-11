


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
    def convert_from_block64(self, blocks):
        bytes = bytearray()
        for i in range(0, len(blocks)):
            """bytes.append(blocks[i] & ((1 << 8) - 1))
            bytes.append(blocks[i] & ((1 << 16) - 1))
            bytes.append(blocks[i] & ((1 << 24) - 1))
            bytes.append(blocks[i] & ((1 << 32) - 1))"""
            bytes.append(blocks[i] % 256)
            bytes.append((blocks[i] >> 8) % 256)
            bytes.append((blocks[i] >> 16) % 256)
            bytes.append((blocks[i] >> 24) % 256)
        return bytes
    def permutationStart(self, block64):
        pass
    def round(self, block64, roundKey):
        pass 
    def encrypt(self, plain_text):
        plainBytes = bytearray(plain_text, "utf-8")
        bytes64 = self.convert_to_block64(plainBytes)

        bytesOut = self.convert_from_block64(bytes64)
        return bytes(bytesOut)
    def decrypt(self, cypher_text):
        bytes64 = self.convert_to_block64(cypher_text)

        bytesOut = self.convert_from_block64(bytes64)
        return bytesOut.decode("utf-8")



if __name__ == '__main__':
    testDes = DES()
    plain = "Hello world!"
    print(plain)
    encr = testDes.encrypt(plain)
    print(encr)
    plainBack = testDes.decrypt(encr)
    print(plainBack)