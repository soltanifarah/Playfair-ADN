from CorrectP import lost, CipherText, key,Added,ListOfRNA

print("Key in decipher: ", key)
print("CipherText in decipher: ", CipherText)
print("Lost RNA Amino in decipher: ", lost)
print("Added: ", Added)



## playfair ###

def toLowerCase(text):
    return text.lower()

def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText

def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
 
        group = i
    Diagraph.append(text[group:])
    return Diagraph

def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word
 
 
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)
 
    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)
 
    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]
 
    return matrix

def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j

def decrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 0:
        char1 = matr[e1r][4]
    else:
        char1 = matr[e1r][e1c-1]
 
    char2 = ''
    if e2c == 0:
        char2 = matr[e2r][4]
    else:
        char2 = matr[e2r][e2c-1]
 
    return char1, char2

def decrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 0:
        char1 = matr[4][e1c]
    else:
        char1 = matr[e1r-1][e1c]
 
    char2 = ''
    if e2r == 0:
        char2 = matr[4][e2c]
    else:
        char2 = matr[e2r-1][e2c]
 
    return char1, char2


def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]
 
    char2 = ''
    char2 = matr[e2r][e1c]
 
    return char1, char2

def decryptByPlayfairCipher(Matrix, CipherList):
    PlainText = []
    for i in range(0, len(CipherList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, CipherList[i][0])
        ele2_x, ele2_y = search(Matrix, CipherList[i][1])
 
        if ele1_x == ele2_x:
            c1, c2 = decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            # Get 2 letter cipherText
        elif ele1_y == ele2_y:
            c1, c2 = decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
 
        cipher = c1 + c2
        PlainText.append(cipher)
    return PlainText


def dec_playfair(AC,key):
    AC = removeSpaces(toLowerCase(AC))
    PlainTextList = Diagraph(FillerLetter(AC))
    if len(PlainTextList[-1]) != 2:
        PlainTextList[-1] = PlainTextList[-1]+'z'
    key = removeSpaces(toLowerCase(key))
    Matrix = generateKeyTable(key, list1)
    
    print("Cipherd Text: ", AC)
    CipherList = decryptByPlayfairCipher(Matrix, PlainTextList)
    
    AP = ""
    for i in CipherList:
        AP += i
    return AP

decryptedPlayFair=dec_playfair(CipherText,key)
if Added==True:
    decryptedPlayFair = decryptedPlayFair[:-1]
decryptedPlayFair=decryptedPlayFair.upper()
print("Decrypted text in Uppercase is: "+decryptedPlayFair)
RNACodons = {
    "A1" : "GCU",
    "A2" : "GCC",
    "A3" : "GCA",
    "A4" : "GCG",
    "B1" : "UAA",
    "B2" : "UAG",
    "B3" : "UGA",
    "C1" : "UGU",
    "C2" : "UGC",
    "D1" : "GAU",
    "D2" : "GAC",
    "E1" : "GAA",
    "E2" : "GAG",
    "F1" : "UUU",
    "F2" : "UUC",
    "G1" : "GGU",
    "G2" : "GGC",
    "G3" : "GGA",
    "G4" : "GGG",
    "H1" : "CAU",
    "H2" : "CAC",
    "I1" : "AUU",
    "I2" : "AUC",
    "I3" : "AUA",
    "K1" : "AAA",
    "K2" : "AAG",
    "L1" : "CUU",
    "L2" : "CUC",
    "L3" : "CUA",
    "L4" : "CUG",
    "M1" : "AUG",
    "N1" : "AAU",
    "N2" : "AAC",
    "O1" : "UUA",
    "O2" : "UUG",
    "P1" : "CCU",
    "P2" : "CCC",
    "P3" : "CCA",
    "P4" : "CCG",
    "Q1" : "CAA",
    "Q2" : "CAG",
    "R1" : "CGU",
    "R2" : "CGC",
    "R3" : "CGA",
    "R4" : "CGG",
    "S1" : "UCU",
    "S2" : "UCC",
    "S3" : "UCA",
    "S4" : "UCG",
    "T1" : "ACU",
    "T2" : "ACC",
    "T3" : "ACA",
    "T4" : "ACG",
    "U1" : "AGA",
    "U2" : "AGG",
    "V1" : "GUU",
    "V2" : "GUC",
    "V3" : "GUA",
    "V4" : "GUG",
    "W1" : "UGG",
    "X1" : "AGU",
    "X2" : "AGC",
    "Y1" : "UAU",
    "Z1" : "UAC",
}

protein=""
for i in range(0, len(decryptedPlayFair)):
    codon = decryptedPlayFair[i:i+1]
    if len(codon)==1:
        codon+=ListOfRNA[i]
        protein += RNACodons[codon]
        current=RNACodons[codon]

protein+=lost
print("Decrypted Aminos Acid is: "+protein)


protein1=protein.maketrans("UACG", "ATGC")
dna=protein.translate(protein1)

print("Decrypted DNA is: "+dna)


def DnaToBinary(string):


    DNACod = {
     'A':'00',
     'C':'01',
     'G':'10',
     'T':'11'
     } 
    
    pieces = []
    for i in range( 0, len(string)):
        piece =  string[i:i+1]
        # pieces.append()
        pieces.append( DNACod[piece] )

    return "".join(pieces)

Binary=DnaToBinary(dna)
print("Decrypted Binary is: "+Binary)



test=''.join(chr(int(Binary[i*8:i*8+8],2)) for i in range(len(Binary)//8))
print("Decrypted Text is: "+test)







