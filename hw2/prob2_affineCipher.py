#!/usr/bin/python3

import letterLib as lb
import numberLib as nl

#Note, capital letters are ASCII vals 0-26 + 65
_cipherText = "FPFKR NEHAF LJHZH KRPHY EVURH HDVSF MHAFL JYRVY MR"
_mod = 26
_L1 = "T"
_L2 = "E"

def run(_cipher, _mod, _L1, _L2):

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
    print(" -- Determine highest frequency and assume it is the letter '%s'" % _L1)
    highestFreqIndx = 0
    for i in range(1, len(letterFreq)):
        if letterFreq[i] > letterFreq[highestFreqIndx]:
            highestFreqIndx = i

    encrypted1 = chr(highestFreqIndx + 65)
    print("With a frequency of %.2f, we assume '%s' represents the encryption of '%s'" % (letterFreq[highestFreqIndx], encrypted1, _L1))
    #set it to zero to get second highest frequency
    letterFreq[highestFreqIndx] = 0.0

    print(); print()
    print("===================")
    print("|=== STEP FOUR ===|")
    print("===================")
    print(" -- Determine 2nd highest frequency and assume it is the letter '%s'" % _L2)
    highestFreqIndx = 0
    for i in range(1, len(letterFreq)):
        if letterFreq[i] > letterFreq[highestFreqIndx]:
            highestFreqIndx = i

    encrypted2 = chr(highestFreqIndx + 65)
    print("With a frequency of %.2f, we assume '%s' represents the encryption of '%s'" % (letterFreq[highestFreqIndx], encrypted2, _L2))

    print(); print()
    print("===================")
    print("|=== STEP FIVE ===|")
    print("===================")
    print(" -- Determine our two equations")
    print("\tf('%s')= '%s'" % (encrypted1, _L1))
    print("\t\t%2s * a + b = %2s (mod %s)" % (ord(_L1) - 65, ord(encrypted1) - 65, _mod))
    print("\tf('%s')= '%s'" % (encrypted2, _L2))
    print("\t\t%2s * a + b = %2s (mod %s)" % (ord(_L2) - 65, ord(encrypted2) - 65, _mod))

    print(); print()
    print("=================")
    print("|=== STEP SIX ===|")
    print("=================")
    print(" -- Eliminate 'b' from euqations. Solve for 'a'. Solve for 'b'.")
    print("\t%2s * a + b = %2s (mod %s)" % (ord(_L1) - 65, ord(encrypted1) - 65, _mod))
    print("\t%2s * a + b = %2s (mod %s)" % (ord(_L2) - 65, ord(encrypted2) - 65, _mod))
    print("\t------------------------")
    temp = (ord(_L2) - 65) - (ord(_L1) - 65)
    diff = (ord(encrypted2) - 65) - (ord(encrypted1) - 65)
    if temp < 0:
        temp = (ord(_L1) - 65) - (ord(_L2) - 65)
        diff = (ord(encrypted1) - 65) - (ord(encrypted2) - 65)

    if diff < 0:
        diff = diff % _mod

    print("\t%2s * temp     = %2s (mod %s)" % (temp , diff, _mod))

    print();print("(Its Euclid time!!!!!!! Only I was cheap and made my own, less efficient way. O(n))")
    a = nl.findMultInv(temp,_mod)
    if a == -1:
        print("FAILURE.  MULTIPLICATIVE INVESE NOT FOUND")
        exit(-9)
    print("\ta = %s" % a)

    b = ord("E") - 65 - a
    if b < 0:
        b = b % _mod
    print("\tb = %s" % b)

    print("====================")
    print("|=== STEP SEVEN ===|")
    print("====================")
    print(" -- Utilizing our decription key (%s, %s), decrypt the message!" % (a, b))
    print(_cipherText)
    print(lb.affineCipherDecrypt(_cipherText, a, b, _mod, 4))

#Note, capital letters are ASCII vals 0-26 + 65
_cipherText = "FPFKR NEHAF LJHZH KRPHY EVURH HDVSF MHAFL JYRVY MR"
_cipherText = "CTOOXT"
_mod = 26
_L1 = "L"
_L2 = "E"

run(_cipherText, _mod, _L1, _L2)

