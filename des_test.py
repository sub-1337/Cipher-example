


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
    expandArr = [32, 1 ,2  ,3  ,4 , 5,
                4 , 5 ,6  ,7  ,8  ,9,
                8 , 9 ,10 ,11 ,12 ,13,
                12, 13, 14, 15, 16, 17,
                16, 17, 18, 19, 20, 21,
                20, 21, 22, 23, 24, 25,
                24, 25, 26, 27, 28, 29,
                28, 29, 30, 31, 32, 1]
    ptableArr = [16, 7, 20, 21,
                    29, 12, 28, 17,
                    1 , 15, 23, 26,
                    5 , 18, 31, 10,
                    2 , 8 ,24 ,14,
                    32, 27, 3 ,9,
                    19, 13, 30, 6,
                    22, 11, 4 ,25]
    sboxArr = [	
# 1
[
	[14	,4	,13	,1	,2	,15	,11	,8	,3	,10	,6	,12	,5	,9	,0	,7],
	[0	,15	,7	,4	,14	,2	,13	,1	,10	,6	,12	,11	,9	,5	,3	,8],
	[4	,1	,14	,8	,13	,6	,2	,11	,15	,12	,9	,7	,3	,10	,5	,0],
	[15	,12	,8	,2	,4	,9	,1	,7	,5	,11	,3	,14	,10	,0	,6	,13]
],
# 2,[,,,,,,,,,,,,,,,
[
	[15	,1	,8	,14	,6	,11	,3	,4	,9	,7	,2	,13	,12	,0	,5	,10],
	[3	,13	,4	,7	,15	,2	,8	,14	,12	,0	,1	,10	,6	,9	,11	,5],
	[0	,14	,7	,11	,10	,4	,13	,1	,5	,8	,12	,6	,9	,3	,2	,15],
	[13	,8	,10	,1	,3	,15	,4	,2	,11	,6	,7	,12	,0	,5	,14	,9]
],
# 3,[,,,,,,,,,,,,,,,
[
	[10	,0	,9	,14	,6	,3	,15	,5	,1	,13	,12	,7	,11	,4	,2	,8],
	[13	,7	,0	,9	,3	,4	,6	,10	,2	,8	,5	,14	,12	,11	,15	,1],
	[13	,6	,4	,9	,8	,15	,3	,0	,11	,1	,2	,12	,5	,10	,14	,7],
	[1	,10	,13	,0	,6	,9	,8	,7	,4	,15	,14	,3	,11	,5	,2	,12]
],
# 4,[,,,,,,,,,,,,,,,
[
	[7	,13	,14	,3	,0	,6	,9	,10	,1	,2	,8	,5	,11	,12	,4	,15],
	[13	,8	,11	,5	,6	,15	,0	,3	,4	,7	,2	,12	,1	,10	,14	,9],
	[10	,6	,9	,0	,12	,11	,7	,13	,15	,1	,3	,14	,5	,2	,8	,4],
	[3	,15	,0	,6	,10	,1	,13	,8	,9	,4	,5	,11	,12	,7	,2	,14]
],
# 5,[,,,,,,,,,,,,,,,
[
	[2	,12	,4	,1	,7	,10	,11	,6	,8	,5	,3	,15	,13	,0	,14	,9],
	[14	,11	,2	,12	,4	,7	,13	,1	,5	,0	,15	,10	,3	,9	,8	,6],
	[4	,2	,1	,11	,10	,13	,7	,8	,15	,9	,12	,5	,6	,3	,0	,14],
	[11	,8	,12	,7	,1	,14	,2	,13	,6	,15	,0	,9	,10	,4	,5	,3]
],
# 6,[,,,,,,,,,,,,,,,
[
	[12	,1	,10	,15	,9	,2	,6	,8	,0	,13	,3	,4	,14	,7	,5	,11],
	[10	,15	,4	,2	,7	,12	,9	,5	,6	,1	,13	,14	,0	,11	,3	,8],
	[9	,14	,15	,5	,2	,8	,12	,3	,7	,0	,4	,10	,1	,13	,11	,6],
	[4	,3	,2	,12	,9	,5	,15	,10	,11	,14	,1	,7	,6	,0	,8	,13]
],
#7,,[,,,,,,,,,,,,,,
[
	[4	,11	,2	,14	,15	,0	,8	,13	,3	,12	,9	,7	,5	,10	,6	,1],
	[13	,0	,11	,7	,4	,9	,1	,10	,14	,3	,5	,12	,2	,15	,8	,6],
	[1	,4	,11	,13	,12	,3	,7	,14	,10	,15	,6	,8	,0	,5	,9	,2],
	[6	,11	,13	,8	,1	,4	,10	,7	,9	,5	,0	,15	,14	,2	,3	,12]
],
#8
[
[13	,2	,8	,4,	6	,15	,11	,1	,10	,9	,3	,14	,5	,0	,12	,7],
[1	,15	,13	,8,	10	,3	,7	,4	,12	,5	,6	,11	,0	,14	,9	,2],
[7	,11	,4	,1,	9	,12	,14	,2	,0	,6	,10	,13	,15	,3	,5	,8],
[2	,1	,14	,7,	4	,10	,8	,13	,15	,12	,9	,0	,3	,5	,6	,11] 
]
]
    def __init__(self):
        pass
    def getBit(self, number, i):
            return (number >> i) & 1
    def setBit(self, number, i, value):            
            if value == 1:
                # Устанавливаем бит в 1
                return number | (1 << i)
            else:
                # Устанавливаем бит в 0
                return number & ~(1 << i)
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
        blockNew = 0
        for i in range(len(permArr)):
            bit = self.getBit(block64, i)
            blockNew = self.setBit(blockNew, permArr[i] - 1, bit)
        
        return blockNew

    def permutationStart(self, block64):
        blockNew = self.permutate(block64, self.permStartArr)
        return blockNew
    def permutationEnd(self, block64):
        blockNew = self.permutate(block64, self.permEndArr)
        return blockNew
    def split32(self, block):
        return [(block >> 32) & (2 ** 32 - 1), block & (2 ** 32 - 1)]
    def concatenate32(sekf, blocks):
        return (blocks[0] << 32) | (blocks[1])
    def expand32_to_48(self, block32):
        result = 0
        for i in range(48):
            bitToFetch = self.expandArr[i] -1
            bit = self.getBit(block32, bitToFetch)
            result = self.setBit(result, i, bit)
        return result
    def sboxPart(self, block6, sboxNumber):
        smaller_axis = (self.getBit(block6, 5) << 1 ) | (self.getBit(block6, 0))
        greater_axis = (self.getBit(block6, 1) << 0 ) | (self.getBit(block6, 2) << 1) | \
                       (self.getBit(block6, 3) << 2 ) | (self.getBit(block6, 4) << 3 )
        res = self.sboxArr[sboxNumber][smaller_axis][greater_axis]
        return res
    def sbox(self, block48):
        sboxRes = 0
        for i in range(0,48,6):
            block6 = (self.getBit(block48, 0 + i) << 0 ) | (self.getBit(block48,  1 + i) << 1) | \
                    (self.getBit(block48,  2 + i) << 2 )  | (self.getBit(block48, 3 + i) << 3 ) | \
                    (self.getBit(block48,  4 + i) << 4 )  | (self.getBit(block48, 5 + i) << 5 )
            sboxNumber = (i // 6)
            sboxRes = sboxRes << 4
            sboxRes |= self.sboxPart(block6, sboxNumber)
        return sboxRes 
    def ptable(self, block32):
        return block32
    def theFFunction(self, block32, key):
        expand = self.expand32_to_48(block32)
        xor = expand ^ key
        sbox = self.sbox(xor)
        ptable = self.ptable(sbox)
        return ptable
    def round(self, block64, roundKey):
        left, right = self.split32(block64)
        # initial
        #newBLock = self.concatenate32([left, right])
        right = left ^ self.theFFunction(right, roundKey)
        newBLock = self.concatenate32([right, left])
        return newBLock
    def finalSwapRound(self, block64):
        left, right = self.split32(block64)
        newBLock = self.concatenate32([right, left])
        return  newBLock
    def retRoundKeys(self, keyRaw): # DEBUG
        keys = []
        for i in range(16):
            keys.append(i + 3)
        return keys
    def encrypt(self, plain_text, keyRaw):
        plainBytes = bytearray(plain_text, "utf-8")
        keyBytes = bytearray(keyRaw, "utf-8")
        bytes64 = self.convert_to_block64(plainBytes)

        for i in range(len(bytes64)):
            bytes64[i] = self.permutationStart(bytes64[i])

        for i in range(len(bytes64)):
            keyRound = self.retRoundKeys(keyBytes)
            for round_i in range(0,16):                
                #print("bytes64[i]" + " i " + str(round_i) + " " + hex(bytes64[i]))
                bytes64[i] = self.round(bytes64[i], keyRound[round_i])
            bytes64[i] = self.finalSwapRound(bytes64[i])

        for i in range(len(bytes64)):
            bytes64[i] = self.permutationEnd(bytes64[i])

        bytesOut = self.convert_from_block64(bytes64)
        return bytes(bytesOut)
    def decrypt(self, cypher_text, keyRaw):
        bytes64 = self.convert_to_block64(cypher_text)
        keyBytes = bytearray(keyRaw, "utf-8")

        for i in range(len(bytes64)):
            bytes64[i] = self.permutationStart(bytes64[i])

        for i in range(len(bytes64)):
            keyRound = self.retRoundKeys(keyBytes)
            for round_i in reversed(range(16)):                
                bytes64[i] = self.round(bytes64[i], keyRound[round_i])
            bytes64[i] = self.finalSwapRound(bytes64[i])

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
    #print(bin(testDes.expand32_to_48(0b1111_1111_1111_0000_1111_1111_1111_0000)))
    #print(bin(testDes.expand32_to_48(0b1111_0000_1111_0000_1111)))
    return

if __name__ == '__main__':
    tests()
    testDes = DES()
    plain = "Hello world!"
    key = "1234"
    print(plain)
    encr = testDes.encrypt(plain,key)
    print(encr)
    plainBack = testDes.decrypt(encr,key)
    print(plainBack)