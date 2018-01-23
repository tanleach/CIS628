#!/usr/bin/python3

#could also use:
#>>> from sympy.core.numbers import igcdex
#>>> igcdex(5,26)[0]%26
def findMultInv(a, mod):
    count = 0
    found = 0
    modCheckVal = mod + 1

    while not found:
        quotient = modCheckVal / a
        if not (quotient % 1):
            found = 1
            print("***Multiplicative inverse of %s is %d***" % (a, quotient % mod))
            return int(quotient % 26)
        else:
            modCheckVal += mod
            count += 1

        if count == 100000:
            return -1
        

#findMultInv(5, 26)
