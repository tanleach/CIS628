#!/usr/bin/python3

import letterLib as lb
import numberLib as nl
from string import ascii_uppercase as UPPERS

#Note, capital letters are ASCII vals 0-26 + 65
_cipherText = "FPFKR NEHAF LJHZH KRPHY EVURH HDVSF MHAFL JYRVY MR"
_mod = 26
_L1 = "L"
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
    print(" -- Choose a value and assume it is the letter '%s'" % _L1)
    highestFreqIndx = 0
    for i in range(1, len(letterFreq)):
        if letterFreq[i] > letterFreq[highestFreqIndx]:
            highestFreqIndx = i

    encrypted1 = chr(highestFreqIndx + 65)
    encrypted1 = chr(5 + 65)
    print("With a frequency of %.2f, we assume '%s' represents the encryption of '%s'" % (letterFreq[highestFreqIndx], encrypted1, _L1))
    #set it to zero to get second highest frequency
    letterFreq[highestFreqIndx] = 0.0

    print(); print()
    print("===================")
    print("|=== STEP FOUR ===|")
    print("===================")
    print(" -- Choose another value and assume it is the letter '%s'" % _L2)
    highestFreqIndx = 0
    for i in range(1, len(letterFreq)):
        if letterFreq[i] > letterFreq[highestFreqIndx]:
            highestFreqIndx = i

    
    encrypted2 = chr(highestFreqIndx + 65)
    encrypted2 = chr(17 + 65)
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

    print("\t%2s * a     = %2s (mod %s)" % (temp , diff, _mod))
    if not ((diff/temp) % 1):
        temp = diff/temp
        a = int(temp)
    else:
#       print("TEMP: --%s--" % temp)
#       print("DIFF: --%s--" % diff)
        print();print("(Its Euclid time!!!!!!! Only I was cheap and made my own, less efficient way. O(n))")
        temp_inv = nl.findMultInv(int(temp),_mod)
        if temp_inv == -1:
            print("FAILURE.  MULTIPLICATIVE INVERSE NOT FOUND")
            return 1
            exit(-9)
        else:
            a = int(diff * temp_inv) % _mod
    if not a % 2:
        #print("CANT BE EVEN")
        return 1
        exit(-9)

    print("\ta = %s" % a)
    
    b = (ord(encrypted2) - 65) - ((ord(_L2) - 65) * a)
    if b < 0:
        b = b % _mod

    print("\tb = %s" % b)

    print("====================")
    print("|=== STEP SEVEN ===|")
    print("====================")
    print(" -- Utilizing our encryption key (%s, %s), decrypt the message!" % (a, b))
    print(" -- d(x) = a^-1(<PLAIN_LETTER> -b) ( % 26)")
    print(_cipherText)
    print(lb.affineCipherDecrypt(_cipherText, a, b, _mod, 4))
    print("(A MATEUR SHACK SYSTEMS PROFESSIONAL SHACK PEOPLE)")

#Note, capital letters are ASCII vals 0-26 + 65
_cipherText = "FPFKR NEHAF LJHZH KRPHY EVURH HDVSF MHAFL JYRVY MR"
_mod = 26
_L1 = "A"
_L2 = "E"

run(_cipherText, _mod, _L1, _L2)

