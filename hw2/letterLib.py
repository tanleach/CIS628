#!/usr/bin/python3

from __future__ import division
import numberLib as nl

_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def calcFreq(letterCounts, total):

    letterFreq = [0]*26

    for i in range(0,len(letterCounts)):
        letterFreq[i] = round(letterCounts[i]/total,3)
    
    return letterFreq
    

def letterCounts(cipher):
    
    letterCounts = [0]*26

    for l in cipher.replace(" ",'').upper():
        asciiVal = ord(l) - 65
        letterCounts[asciiVal] = letterCounts[asciiVal] + 1

    return letterCounts

def shiftCipherDecrypt(cipher, offset, space=0):
    plainText = ""
    count = 1
    for l in cipher:
        print
        if l == " ":
            plainText += l
            continue
        
        plainLetter = ((ord(l) - 65) + offset) % 26
        
        plainText += chr(plainLetter + 65)

    return plainText
    
def affineCipherDecrypt(cipher, a, b, mod, space=0):
    
    a_inv = nl.findMultInv(a, mod)
    plainText = ""
    count = 1
    for l in cipher:
        if l == " ":
            plainText += l
            continue
        
        temp = "P"
        plain = ((ord(l) - 65) - b) * a_inv
        plain = plain % 26
        plainText += _alphabet[plain]
    
    return plainText


def printStats(counts, freq, total):
    print("     ", ''.join(['{:6}'.format(item) for item in _alphabet]), sep="")
    print(''.join(['{:6}'.format(item) for item in counts]))
    print(''.join(['{:6}'.format(item) for item in freq]))

