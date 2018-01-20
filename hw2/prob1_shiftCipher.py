#!/usr/bin/python3

import letterLib as lb

_cipherText = "XLCJS LOLWT EEWPV PJDSP VPAET ETYPD NCZHL YOPGP CJEST YRESL EXLCJ DLTOE SPQPO DHPCP DFCPE ZVYZH"


print("==================")
print("|=== STEP ONE ===|")
print("==================")
print(" -- Read in Cipher Text:")
print("\t", _cipherText)
print()


print("==================")
print("|=== STEP ONE ===|")
print("==================")
print(" -- Process letter frequency")
letterCounts = lb.letterCounts(_cipherText)
letterFreq = lb.calcFreq(letterCounts, len(_cipherText.strip()))
lb.printStats(letterCounts, letterFreq, len(_cipherText.strip()))
