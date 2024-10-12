


class DES:
    permStartArr = [58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9 ,1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]
    permEndArr = [40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9,  49, 17, 57, 25]
    def __init__(self):
        """for i in range(64):
            self.permStartArr.append(i)"""
        pass
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
            bytes.append(blocks[i] % 256)
            bytes.append((blocks[i] >> 8) % 256)
            bytes.append((blocks[i] >> 16) % 256)
            bytes.append((blocks[i] >> 24) % 256)
        return bytes
    def permutate(self, block64, permArr):
        def getBit(number, i):
            return (number >> i) & 1
        def setBit(number, i, value):            
            if value == 1:
                # Устанавливаем бит в 1
                return number | (1 << i)
            else:
                # Устанавливаем бит в 0
                return number & ~(1 << i)
        blockNew = 0
        for i in range(64):
            bit = getBit(block64, i)
            blockNew = setBit(blockNew, permArr[i] - 1, bit)
        
        return blockNew

    def permutationStart(self, block64):
        blockNew = self.permutate(block64, self.permStartArr)
        return blockNew
    def permutationEnd(self, block64):
        blockNew = self.permutate(block64, self.permEndArr)
        return blockNew
    def round(self, block64, roundKey):
        pass 
    def finalSwap(self, block64):
        pass
    def encrypt(self, plain_text):
        plainBytes = bytearray(plain_text, "utf-8")
        bytes64 = self.convert_to_block64(plainBytes)

        for i in range(len(bytes64)):
            bytes64[i] = self.permutationStart(bytes64[i])

        for i in range(len(bytes64)):
            bytes64[i] = self.permutationEnd(bytes64[i])

        bytesOut = self.convert_from_block64(bytes64)
        return bytes(bytesOut)
    def decrypt(self, cypher_text):
        bytes64 = self.convert_to_block64(cypher_text)

        for i in range(len(bytes64)):
            bytes64[i] = self.permutationStart(bytes64[i])

        for i in range(len(bytes64)):
            bytes64[i] = self.permutationEnd(bytes64[i])

        bytesOut = self.convert_from_block64(bytes64)
        return bytesOut.decode("utf-8")

def tests():
    testDes = DES()
    """res = testDes.perm(0b1010, [0, 2,1,3])
    if (res != 0b1100):
        print("error 1")

    res = testDes.perm(0b1111, [0,1,2,3])
    if (res != 0b1111):
        print("error 2")

    res = testDes.perm(0b1000, [3,2,1,0])
    if (res != 0b0001):
        print("error 3")

    res = testDes.perm(0b1100, [3,2,1,0])
    if (res != 0b0011):
        print("error 3")
"""
    """t1 = [  1, 3, 2, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0]
    
    res = testDes.perm(0b110, t1)
    if (res != 0b1010):
        print("error 4")"""
    #print(bin(testDes.perm(0b111, testDes.permStartArr)))
    #print(bin(testDes.perm(0b111 << 64 - 3, testDes.permStartArr)))
    return

if __name__ == '__main__':
    tests()
    testDes = DES()
    plain = "Hello world!"
    print(plain)
    encr = testDes.encrypt(plain)
    print(encr)
    plainBack = testDes.decrypt(encr)
    print(plainBack)