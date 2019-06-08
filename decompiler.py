#!/bin/python
import sys

def main():
    if len(sys.argv) < 2:
        print("No firmware provided")
        sys.exit(1)

    fw = open(sys.argv[1], "r")
    bytes = fw.readlines()[0].split(' ')
    output = []
    loop = True
    i = 0
    while loop:
        if i >= len(bytes):
            break
        code = getData(bytes[i])
        print([i, code, bytes[i]])
        if code[1] == 0:
            output.append(code[0] + "\n")
            i += 1
        else:
            output.append(code[0].format(*bytes[i:int(i)+int(code[1])]) + "\n")
            i += code[1] + 1
    toWrite = open("output.asm", "w")
    toWrite.writelines(output)
    toWrite.close()



def getData(byte):
    return byteCodes.get(byte, 'BYTENOTFOUND: ' + byte)


byteCodes = {
    #region 0x24 - 0x2F DD
    "24": ["ADD A, #{}h", 1], # #data 
    "25": ["ADD A, {}h", 1], # direct
    "26": ["ADD A, @R1", 0], # @Ri
    "27": ["ADD A, @R2", 0], # @Ri
    "28": ["ADD A, R0", 0], # R0
    "29": ["ADD A, R1", 0], # R1
    "2A": ["ADD A, R2", 0], # R2
    "2B": ["ADD A, R3", 0], # R3
    "2C": ["ADD A, R4", 0], # R4
    "2D": ["ADD A, R5", 0], # R5
    "2E": ["ADD A, R6", 0], # R6
    "2F": ["ADD A, R7", 0], # R7
    #endregion
    #region 0x38 - 0x3F ADDC
    "34": ["ADDC A, #{}h", 1], # #data
    "35": ["ADDC A, {}h", 1], # direct
    "36": ["ADDC A, @R1", 0], # @Ri
    "37": ["ADDC A, @R2", 0], # @Ri
    "38": ["ADDC A, R0", 0], # R0
    "39": ["ADDC A, R1", 0], # R1
    "3A": ["ADDC A, R2", 0], # R2
    "3B": ["ADDC A, R3", 0], # R3
    "3C": ["ADDC A, R4", 0], # R4
    "3D": ["ADDC A, R5", 0], # R5
    "3E": ["ADDC A, R6", 0], # R6
    "3F": ["ADDC A, R7", 0], # R7
    #endregion
    #region 0x98 - 0x94 SUBB
    "94": ["SUBB A, #{}h", 1], # #data
    "95": ["SUBB A, {}h", 1], # direct
    "96": ["SUBB A, @R1", 0], # @Ri
    "97": ["SUBB A, @R2", 0], # @Ri
    "98": ["SUBB A, R0", 0], # R0
    "99": ["SUBB A, R1", 0], # R1
    "9A": ["SUBB A, R2", 0], # R2
    "9B": ["SUBB A, R3", 0], # R3
    "9C": ["SUBB A, R4", 0], # R4
    "9D": ["SUBB A, R5", 0], # R5
    "9E": ["SUBB A, R6", 0], # R6
    "9F": ["SUBB A, R7", 0], # R7
    #endregion
    #region 0x04 - 0x0F INC
    "04": ["INC A", 0], # inc A
    "05": ["INC {}h", 1], # direct
    "06": ["INC @R1", 0], # @R1
    "07": ["INC @R2", 0], # @R2
    "08": ["INC R0", 0], # R0
    "09": ["INC R1", 0], # R1
    "0A": ["INC R2", 0], # R2
    "0B": ["INC R3", 0], # R3
    "0C": ["INC R4", 0], # R4
    "0D": ["INC R5", 0], # R5
    "0E": ["INC R6", 0], # R6
    "0F": ["INC R7", 0], # R7 
    #endregion
    #region 0x14 - 0x1F DEC
    "14": ["DEC A", 0], # dec A
    "15": ["DEC {}h", 1], # direct
    "16": ["DEC @R1", 0], # @R1
    "17": ["DEC @R2", 0], # @R2
    "18": ["DEC R0", 0], # R0
    "19": ["DEC R1", 0], # R1
    "1A": ["DEC R2", 0], # R2
    "1B": ["DEC R3", 0], # R3
    "1C": ["DEC R4", 0], # R4
    "1D": ["DEC R5", 0], # R5
    "1E": ["DEC R6", 0], # R6
    "1F": ["DEC R7", 0], # R7 
    #endregion
    "A3": ["INC DPTR", 0],
    "A4": ["MUL AB", 0],
    "84": ["DIV AB", 0],
    "D4": ["DA A", 0],
    #region 0x52 - 0x5F ANL
    "52": ["ANL {}h, A", 1], # direct & acc
    "53": ["ANL {}h, {}h", 2], # direct & #data
    "54": ["ANL A", 0], # dec A
    "55": ["ANL {}h", 1], # direct
    "56": ["ANL @R1", 0], # @R1
    "57": ["ANL @R2", 0], # @R2
    "58": ["ANL R0", 0], # R0
    "59": ["ANL R1", 0], # R1
    "5A": ["ANL R2", 0], # R2
    "5B": ["ANL R3", 0], # R3
    "5C": ["ANL R4", 0], # R4
    "5D": ["ANL R5", 0], # R5
    "5E": ["ANL R6", 0], # R6
    "5F": ["ANL R7", 0], # R7 
    #endregion
    #region 0x42 - 0x4F ORL
    "42": ["ORL {}h, A", 1], # direct & acc
    "43": ["ORL {}h, {}h", 2], # direct & #data
    "44": ["ORL A", 0], # dec A
    "45": ["ORL {}h", 1], # direct
    "46": ["ORL @R1", 0], # @R1
    "47": ["ORL @R2", 0], # @R2
    "48": ["ORL R0", 0], # R0
    "49": ["ORL R1", 0], # R1
    "4A": ["ORL R2", 0], # R2
    "4B": ["ORL R3", 0], # R3
    "4C": ["ORL R4", 0], # R4
    "4D": ["ORL R5", 0], # R5
    "4E": ["ORL R6", 0], # R6
    "4F": ["ORL R7", 0], # R7 
    #endregion
    #region 0x62 - 0x6F XRL
    "62": ["XRL {}h, A", 1], # direct & acc
    "63": ["XRL {}h, {}h", 2], # direct & #data
    "64": ["XRL A", 0], # dec A
    "65": ["XRL {}h", 1], # direct
    "66": ["XRL @R1", 0], # @R1
    "67": ["XRL @R2", 0], # @R2
    "68": ["XRL R0", 0], # R0
    "69": ["XRL R1", 0], # R1
    "6A": ["XRL R2", 0], # R2
    "6B": ["XRL R3", 0], # R3
    "6C": ["XRL R4", 0], # R4
    "6D": ["XRL R5", 0], # R5
    "6E": ["XRL R6", 0], # R6
    "6F": ["XRL R7", 0], # R7 
    #endregion
    "E4": ["CLR A", 0],
    "F4": ["CPL A", 0],
    "23": ["RL A", 0],
    "33": ["RLC A", 0],
    "03": ["RR A", 0],
    "13": ["RRC A", 0],
    "C4": ["SWAP A", 0],
    #region 
        #Accumulator -> Others
    "74": ["MOV A, #{}h", 1], # data
    "E5": ["MOV A, {}h", 1], # direct
    "E6": ["MOV A, @R1", 0], # @R1
    "E7": ["MOV A, @R2", 0], # @R2
    "E8": ["MOV A, R0", 0], # R0
    "E9": ["MOV A, R1", 0], # R1
    "EA": ["MOV A, R2", 0], # R2
    "EB": ["MOV A, R3", 0], # R3
    "EC": ["MOV A, R4", 0], # R4
    "ED": ["MOV A, R5", 0], # R5
    "EE": ["MOV A, R6", 0], # R6
    "EF": ["MOV A, R7", 0], # R7 
    #region Rn -> somewhere
        #Rn -> Accumulator
        "F8": ["MOV R0, A", 0], # R0
        "F9": ["MOV R1, A", 0], # R1
        "FA": ["MOV R2, A", 0], # R2
        "FB": ["MOV R3, A", 0], # R3
        "FC": ["MOV R4, A", 0], # R4
        "FD": ["MOV R5, A", 0], # R5
        "FE": ["MOV R6, A", 0], # R6
        "FF": ["MOV R7, A", 0], # R7 
        #Rn -> direct
        "A8": ["MOV R0, {}h", 1], # R0
        "A9": ["MOV R1, {}h", 1], # R1
        "AA": ["MOV R2, {}h", 1], # R2
        "AB": ["MOV R3, {}h", 1], # R3
        "AC": ["MOV R4, {}h", 1], # R4
        "AD": ["MOV R5, {}h", 1], # R5
        "AE": ["MOV R6, {}h", 1], # R6
        "AF": ["MOV R7, {}h", 1], # R7 
        #Rn -> #data
        "78": ["MOV R0, #{}h", 1], # R0
        "79": ["MOV R1, #{}h", 1], # R1
        "7A": ["MOV R2, #{}h", 1], # R2
        "7B": ["MOV R3, #{}h", 1], # R3
        "7C": ["MOV R4, #{}h", 1], # R4
        "7D": ["MOV R5, #{}h", 1], # R5
        "7E": ["MOV R6, #{}h", 1], # R6
        "7F": ["MOV R7, #{}h", 1], # R7 
    #endregion
    #region direct <- somewhere
        #direct <- accumulator
        "F5": ["MOV {}h, A", 1],
        #direct <- Rn
        "88": ["MOV {}h, R0", 1], # R0
        "89": ["MOV {}h, R1", 1], # R1
        "8A": ["MOV {}h, R2", 1], # R2
        "8B": ["MOV {}h, R3", 1], # R3
        "8C": ["MOV {}h, R4", 1], # R4
        "8D": ["MOV {}h, R5", 1], # R5
        "8E": ["MOV {}h, R6", 1], # R6
        "8F": ["MOV {}h, R7", 1], # R7 
        #direct <- direct
        "85": ["MOV {}h, {}h", 2],
        #direct <- @Ri
        "86": ["MOV {}h, @R1", 1],
        "87": ["MOV {}h, @R2", 1],
        "75": ["MOV {}h, #{}h", 2],
    #endregion
    #region @Ri <- something
        "F6": ["MOV @R1, A", 0],
        "F7": ["MOV @R2, A", 0],
        "A6": ["MOV @R1, {}h", 1],
        "A7": ["MOV @R2, {}h", 1],
        "76": ["MOV @R1, #{}h", 1],
        "77": ["MOV @R2, #{}h", 1],
    #endregion
    "90": ["MOV DPTR, #{}{}", 2],
    "93": ["MOVC A, @A+DPTR", 0],
    "83": ["MOVC A, @A+PC", 0],
    "E2": ["MOVX A, @R1", 0],
    "E3": ["MOVX A, @R2", 0],
    "E0": ["MOVX A, @DPTR", 0],
    "F2": ["MOVX @R1, A", 0],
    "F3": ["MOVX @R2, A", 0],
    "F0": ["MOVX @DPTR, A", 0],
    "C0": ["PUSH {}h", 1],
    "D0": ["POP {}h", 1],
    #region 0xC5 - 0xCF XCH
    "C5": ["XCH A, {}h", 1], # direct
    "C6": ["XCH A, @R1", 0], # @Ri
    "C7": ["XCH A, @R2", 0], # @Ri
    "C8": ["XCH A, R0", 0], # R0
    "C9": ["XCH A, R1", 0], # R1
    "CA": ["XCH A, R2", 0], # R2
    "CB": ["XCH A, R3", 0], # R3
    "CC": ["XCH A, R4", 0], # R4
    "CD": ["XCH A, R5", 0], # R5
    "CE": ["XCH A, R6", 0], # R6
    "CF": ["XCH A, R7", 0], # R7
    #endregion
    "D6": ["XCHD A, @R1", 0],
    "D7": ["XCHD A, @R2", 0],
    "11": ["ACALL {}", 1],
    "31": ["ACALL {}", 1],
    "51": ["ACALL {}", 1],
    "71": ["ACALL {}", 1],
    "91": ["ACALL {}", 1],
    "B1": ["ACALL {}", 1],
    "D1": ["ACALL {}", 1],
    "F1": ["ACALL {}", 1],
    "12": ["LCALL {}{}", 2],
    "22": ["RET", 0],
    "32": ["RETI", 0],
    "01": ["AJMP {}", 1],
    "21": ["AJMP {}", 1],
    "41": ["AJMP {}", 1],
    "61": ["AJMP {}", 1],
    "81": ["AJMP {}", 1],
    "A1": ["AJMP {}", 1],
    "C1": ["AJMP {}", 1],
    "E1": ["AJMP {}", 1],
    "02": ["LJMP {}{}", 2],
    "80": ["SJMP {}", 1],
    "73": ["JUMP @A+DPTR", 0],
    "60": ["JZ {}", 1],
    "70": ["JNZ {}", 1],
    "40": ["JC {}", 1],
    "50": ["JNC {}", 1],
    "20": ["JB {}, {}", 2],
    "30": ["JNB {}, {}", 2],
    "10": ["JBC {}, {}", 2],
    "B5": ["CJNE A, {}, {}", 2],
    "B4": ["CJNE A, #{}, {}", 2],
    "B8": ["CJNE R0, #{}, {}", 2], # R0
    "B9": ["CJNE R1, #{}, {}", 2], # R1
    "BA": ["CJNE R2, #{}, {}", 2], # R2
    "BB": ["CJNE R3, #{}, {}", 2], # R3
    "BC": ["CJNE R4, #{}, {}", 2], # R4
    "BD": ["CJNE R5, #{}, {}", 2], # R5
    "BE": ["CJNE R6, #{}, {}", 2], # R6
    "BF": ["CJNE R7, #{}, {}", 2], # R7 
    "B6": ["CJNE @R1, #{}, {}", 2],
    "B7": ["CJNE @R2, #{}, {}", 2],
    "D8": ["DJNZ R0, {}", 1], # R0
    "D9": ["DJNZ R1, {}", 1], # R1
    "DA": ["DJNZ R2, {}", 1], # R2
    "DB": ["DJNZ R3, {}", 1], # R3
    "DC": ["DJNZ R4, {}", 1], # R4
    "DD": ["DJNZ R5, {}", 1], # R5
    "DE": ["DJNZ R6, {}", 1], # R6
    "DF": ["DJNZ R7, {}", 1], # R7 
    "D5": ["DJNZ {}, {}", 2],
    "00": ["NOP", 0],
    "C3": ["CLR C", 0],
    "C2": ["CLR {}", 1],
    "D3": ["SETB C", 0],
    "D2": ["SETB {}", 1],
    "B3": ["CPL C", 0],
    "B2": ["CPL {}", 1],
    "82": ["ANL C, {}", 1],
    "B0": ["ANL C, /{}", 1],
    "72": ["ORL C, {}", 1],
    "A0": ["ORL C, /{}", 1],
    "A2": ["MOV C, {}", 1],
    "92": ["MOV {}, C", 1],
    #endregion
}

main()