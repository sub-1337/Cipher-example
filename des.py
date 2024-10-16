


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
    # Standard expansion permutation
    expandArr_1 = [
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1
    ]
    # Working expansion
    expandArr_2 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    ]
    expandArr  = expandArr_1
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
    shiftKeyCountArr = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    keyCompressionFinalArr = [14	,17	,11	,24	,1	,5	,3	,28	,15	,6	,21 ,10	,23	,19	,12 ,4, 
                            26	,8	,16	,7	,27	,20	,13	,2	,41	,52	,31 ,37	,47	,55	,30 ,40,
                            51	,45	,33	,48	,44	,49	,39	,56	,34	,53	,46 ,42	,50	,36	,29 ,32]
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
        while len(bytes) % 8 != 0: # Fill until divideble by 64 bits (8 * 4)
            bytes.append(0x0)
        bytes64 = []
        for i in range(0, len( bytes), 8):
            block64 =   bytes[0 + i] 
            block64 +=  bytes[1 + i] << 8
            block64 +=  bytes[2 + i] << 16
            block64 +=  bytes[3 + i] << 24
            block64 +=  bytes[4 + i] << 32
            block64 +=  bytes[5 + i] << 40
            block64 +=  bytes[6 + i] << 48
            block64 +=  bytes[7 + i] << 56
            bytes64.append(block64)
        return bytes64
    def convert_from_block64(self, blocks):
        bytes = bytearray()
        for i in range(0, len(blocks)):
            bytes.append(blocks[i] % 256)
            bytes.append((blocks[i] >> 8) % 256)
            bytes.append((blocks[i] >> 16) % 256)
            bytes.append((blocks[i] >> 24) % 256)
            
            bytes.append((blocks[i] >> 32) % 256)
            bytes.append((blocks[i] >> 40) % 256)
            bytes.append((blocks[i] >> 48) % 256)
            bytes.append((blocks[i] >> 56) % 256)
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
    def split28(self, block):
        return [(block >> 28) & (2 ** 28 - 1), block & (2 ** 28 - 1)]
    def concatenate28(self, blocks):
        return (blocks[0] << 28) | (blocks[1])
    def expand32_to_48(self, block32):
        result = 0
        """for i in range(48):
            bit_to_fetch = self.expandArr[i] - 1
            bit = self.getBit(block32, bit_to_fetch)
            result = self.setBit(result, i, bit)"""
        for i in range(48):
            bit_to_fetch = self.expandArr[i] - 1
            bit = self.getBit(block32, bit_to_fetch)
            result = self.setBit(result, i, bit)
        return result
    def sbox(self, block48):
        sboxRes = 0
        # Делим входное 48-битное число на 8 групп по 6 бит
        sbox_outputs = []
        for i in range(8):
            # Извлекаем 6 бит для каждого S-бокса
            group_6bit = (block48 >> (42 - 6 * i)) & 0b111111
            
            # Определяем строку (первые и последние биты)
            row = ((group_6bit & 0b100000) >> 4) | (group_6bit & 0b000001)
            
            # Определяем столбец (средние 4 бита)
            col = (group_6bit & 0b011110) >> 1
            
            # Получаем 4-битный результат из соответствующего S-бокса
            sbox_output = self.sboxArr[i][row][col]
            
            # Добавляем результат в список
            sbox_outputs.append(sbox_output)
        
        # Объединяем результаты из всех S-боксов в одно 32-битное число
        sboxRes = 0
        for sbox_output in sbox_outputs:
            sboxRes = (sboxRes << 4) | sbox_output
        if (len(str(bin(sboxRes))) - 2) > 32:
            print("error - sbox overflow")
        return sboxRes 
    def ptable(self, block32):
        result = 0 #self.permutate(block32, self.ptableArr) #FIXME
        for i in range(32):
            i_bit_to_Set = self.ptableArr[i] - 1
            bit = self.getBit(block32, i_bit_to_Set)
            result = self.setBit(result, i, bit)
        return result
    def theFFunction(self, block32, key):
        expand = self.expand32_to_48(block32)
        #DEBUG
        if (len(str(bin(expand))) - 2) > 48:
            print("error - xor overflow")

        xor = expand ^ key
        xor = block32 ^ key
        #xor = block32 ^ key
        #print("xor sz " + str(len(str(bin(xor))) - 2))
        #DEBUG
        if (len(str(bin(xor))) - 2) > 48:
            print("error - xor overflow")

        sbox = self.sbox(xor)

        #DEBUG
        if (len(str(bin(sbox))) - 2) > 32:
            print("error - sbox overflow")

        ptable = self.ptable(sbox)
        #DEBUG

        if (len(str(bin(ptable))) - 2) > 32:
            print("error - ptable overflow")

        return ptable # DEBUG
    def round(self, block64, roundKey):
        left, right = self.split32(block64)
        # initial
        #newBLock = self.concatenate32([left, right])
        #print(hex(roundKey))
        theFFunction = self.theFFunction(right, roundKey)
        if (len(str(bin(theFFunction))) - 2) > 32:
            print("error - theFFunction overflow")
        right = left ^ theFFunction 
        newBLock = self.concatenate32([right, left])
        return newBLock
    def finalSwapRound(self, block64):
        left, right = self.split32(block64)
        newBLock = self.concatenate32([right, left])
        return  newBLock
    def parityDropKey(self, block64):
        result = 0
        n = 0
        for i in range(64):
            if i % 8 != 7:
                bit = self.getBit(block64, i)
                result = self.setBit(result, n, bit)
                n += 1
            else:
                next
        return result
    def left_circular_shift(self, value, shift, bit_length):
        shifted = ((value << shift) & ((1 << bit_length) - 1)) | (value >> (bit_length - shift))
        return shifted
    def permChoiceKey(self, key64):
        result = 0
        result = self.parityDropKey(key64)
        return result
    def keyCompressionFinal(self, key56):
        result = 0
        for i in range(48):
            i_bit_to_put = self.keyCompressionFinalArr[i]
            bit = self.getBit(key56, i_bit_to_put)
            result = self.setBit(result, i, bit)
        return result
    def retRoundKeys(self, keyRaw):
        keys = []
        key64 = self.convert_to_block64(keyRaw)[0]
        key56 = self.permChoiceKey(key64)
        key_C28, key_D28 = self.split28(key56)   
        for i in range(16):
            bits_to_shift = self.shiftKeyCountArr[i]                                
            key_C28 = self.left_circular_shift(key_C28,bits_to_shift,28)            
            key_D28 = self.left_circular_shift(key_D28,bits_to_shift,28)
            keyNew56 = self.concatenate28([key_C28, key_D28])
            keyRound48 = self.keyCompressionFinal(keyNew56)
            #key56 = self.left_circular_shift(key56,bits_to_shift,56)
            keys.append(keyRound48)
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
        try:
            return bytesOut.decode("utf-8")
        except:
            return "ERROR"

def tests():
    testDes = DES()
    block = 0x5951f9e310fdfb00
    key = 0x490085ff1d31
    resReal = testDes.round(block, key)
    resReal = testDes.finalSwapRound(resReal)

    blockBack = testDes.round(resReal, key)
    blockBack = testDes.finalSwapRound(blockBack)
    print( "Block same ", str(blockBack == block))
    return

if __name__ == '__main__':
    tests()
    testDes = DES()
    plain = "Hello world!"
    key = "Secret"
    print(plain)
    encr = testDes.encrypt(plain,key)
    print(encr)
    plainBack = testDes.decrypt(encr,key)
    print(plainBack)