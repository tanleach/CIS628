#!/usr/bin/python3

import letterLib as lb

#Note, capital letters are ASCII vals 0-26 + 65
_cipherText = "XLCJS LOLWT EEWPV PJDSP VPAET ETYPD NCZHL YOPGP CJEST YRESL EXLCJ DLTOE SPQPO DHPCP DFCPE ZVYZH"

print("==================")
print("|=== STEP ONE ===|")
print("==================")
print(" -- Read in Cipher Text:")
print("\t", _cipherText)
print(); print()


print("==================")
print("|=== STEP TWO ===|")
print("==================")
print(" -- Process letter frequency")
letterCounts = lb.letterCounts(_cipherText)
letterFreq = lb.calcFreq(letterCounts, len(_cipherText.strip()))
lb.printStats(letterCounts, letterFreq, len(_cipherText.strip()))

print(); print()
print("===================")
print("|=== STEP THREE ===|")
print("===================")
print(" -- Determine highest frequency and assume it is the letter 'E'")
highestFreqIndx = 0
for i in range(1, len(letterFreq)):
    if letterFreq[i] > letterFreq[highestFreqIndx]:
        highestFreqIndx = i

encryptedE = chr(highestFreqIndx + 65)
print("With a frequency of %.2f, we assume '%s' represents the encryption of 'E'" % (letterFreq[highestFreqIndx], encryptedE))

print(); print()
print("===================")
print("|=== STEP FOUR ===|")
print("===================")
print(" -- Determine the offset for the shift from '%s' to 'E'" % encryptedE)
print("\t'%s' is index %d" % (encryptedE, highestFreqIndx))
print("\t'E' is index %d" % (ord("E") - 65))
print("\tOffset equals (<encrypted_index> + 15) % 26")

print(); print()
print("===================")
print("|=== STEP FIVE ===|")
print("===================")
print(" -- Usuing the offset we use our encrypted string and try to decrypt it")
print("\t", _cipherText)
print("\t",lb.shiftCipherDecrypt(_cipherText, 15, 4))
print("\t(MARY HAD A LITTLE KEY SHE KEPT IT IN ESCROW AND EVERYTHING THAT MARY SAID THE FEDS WERE SURE TO KNOW)")

print(); print()
print("===========================")
print("|~~~ SHIFT CIPHER KEY: ~~~|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|   (<index> + 15) % 26   |")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("===========================")

