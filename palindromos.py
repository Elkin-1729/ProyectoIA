# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 18:01:04 2023

@author: elkin
"""


def palindromo(n):
    i=0
    while i <= (len(str(n))-1):
    
        if str(n)[i] == str(n)[-(i+1)]:
            r = True
        else:
            r = False
            break
        i += 1  
    return r 


n = input("ingrese n: ")

print(palindromo(n))