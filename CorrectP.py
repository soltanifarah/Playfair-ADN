
##cipher
import aminocode
test_str = input("Write a message: ")
  
# printing original string 
print("The original string is : " + str(test_str))
  
# using join() + ord() + format()
# Converting String to binary
res = ''.join(format(ord(i), '08b') for i in test_str)
  
# printing result 
print("The binary string is : " + str(res))

## A 00  C 01 G 10 T 11
BinaryMessage = str(res)

DNA = {
 '00':'A',
 '01':'C',
 '10':'G',
 '11':'T'
}

def EncryptFromBinaryToDNA( string ):

    pieces = []
    for i in range( 0, len(string), 2 ):
        piece =  string[i:i+2]
        # pieces.append()
        pieces.append( DNA[piece] )

    return "".join(pieces)


print("The DNA cipher is: "+EncryptFromBinaryToDNA(BinaryMessage))

DNAmessage = EncryptFromBinaryToDNA(BinaryMessage).replace("\n", "")


'''
def translate(seq):  
   table = {  
      'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',  
      'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',  
      'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',  
      'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',   
      'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',  
      'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',  
      'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',  
      'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',  
      'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',  
      'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',  
      'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',  
      'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',  
      'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',  
      'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',  
      'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',  
      'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',  
      }  
   protein =""
   boolean=True
   lostchar=""
   while(boolean==True):
    if len(seq)%3 == 0:  
       for i in range(0, len(seq), 3): 
          codon = seq[i:i + 3]  
          protein+= table[codon]
          boolean=False
    else:
        lostchar+=seq[-1]
        seq = seq[:-1]
   return protein
'''
Protein=DNAmessage.maketrans("ATGC", "UACG")

rna=DNAmessage.translate(Protein)

print("AMINO ACID IS: "+rna)



RNA_Codons = {
    "GCU" : "A1",
    "GCC" : "A2",
    "GCA" : "A3",
    "GCG" : "A4",
    "UAA" : "B1",
    "UAG" : "B2",
    "UGA" : "B3",
    "UGU" : "C1",
    "UGC" : "C2",
    "GAU" : "D1",
    "GAC" : "D2",
    "GAA" : "E1",
    "GAG" : "E2",
    "UUU" : "F1",
    "UUC" : "F2",
    "GGU" : "G1",
    "GGC" : "G2",
    "GGA" : "G3",
    "GGG" : "G4",
    "CAU" : "H1",
    "CAC" : "H2",
    "AUU" : "I1",
    "AUC" : "I2",
    "AUA" : "I3",
    "AAA" : "K1",
    "AAG" : "K2",
    "CUU" : "L1",
    "CUC" : "L2",
    "CUA" : "L3",
    "CUG" : "L4",
    "AUG" : "M1",
    "AAU" : "N1",
    "AAC" : "N2",
    "UUA" : "O1",
    "UUG" : "O2",
    "CCU" : "P1",
    "CCC" : "P2",
    "CCA" : "P3",
    "CCG" : "P4",
    "CAA" : "Q1",
    "CAG" : "Q2",
    "CGU" : "R1",
    "CGC" : "R2",
    "CGA" : "R3",
    "CGG" : "R4",
    "UCU" : "S1",
    "UCC" : "S2",
    "UCA" : "S3",
    "UCG" : "S4",
    "ACU" : "T1",
    "ACC" : "T2",
    "ACA" : "T3",
    "ACG" : "T4",
    "AGA" : "U1",
    "AGG" : "U2",
    "GUU" : "V1",
    "GUC" : "V2",
    "GUA" : "V3",
    "GUG" : "V4",
    "UGG" : "W1",
    "AGU" : "X1",
    "AGC" : "X2",
    "UAU" : "Y1",
    "UAC" : "Z1",
}



lost=""
protein = ""
ListOfRNA=[]
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    if len(codon)==3:
        protein += RNA_Codons[codon][:-1]
        current=RNA_Codons[codon]
        ListOfRNA.append(current[-1])
    else:
        lost=codon



print(f"\nThe protein sequence is: {protein}")
print("Lost this: "+lost)


############## PLAYFAIR ###############################


def toLowerCase(text):
    return text.lower()
 
# Function to remove all spaces in a string
 


def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText
 
# Function to group 2 elements of a string
# as a list element
 
 
def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
 
        group = i
    Diagraph.append(text[group:])
    return Diagraph
 
# Function to fill a letter in a string element
# If 2 letters in the same string matches
 
 
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
 
# Function to generate the 5x5 key square matrix
 
 
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
 
 
def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]
 
    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]
 
    return char1, char2
 
 
def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]
 
    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]
 
    return char1, char2
 
 
def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]
 
    char2 = ''
    char2 = matr[e2r][e1c]
 
    return char1, char2
 
 
def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])
 
        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            # Get 2 letter cipherText
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
 
        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText
### 7 letters 2 2 2 1
Added=False
text_Plain = protein
text_Plain = removeSpaces(toLowerCase(text_Plain))
PlainTextList = Diagraph(FillerLetter(text_Plain))
if len(PlainTextList[-1]) != 2:
    PlainTextList[-1] = PlainTextList[-1]+'z'
    Added=True
 
key = input("Assign a key: ")
print("Key text:", key)
key = toLowerCase(key)
Matrix = generateKeyTable(key, list1)
 
print("Plain Text:", text_Plain)
CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)
 
CipherText = ""
for i in CipherList:
    CipherText += i
print("CipherText:", CipherText)
