# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:01:31 2018

@author: Akshay Tyagi
"""
def generate_code():
    l=[0,1,2,3,4,5,6,7,8,9]
    from random import shuffle
    shuffle(l)
    global lc
    lc= []
    for i in range(3):
        lc.append(l[i])
    return lc
def guess():
    count=0
    while (count!=3):
        count = 0
        lu=list(input("Enter Your Guessed Three Digit Number: "))
        for i in range(3):
            if (int(lu[i])==lc[i]):
                print("Match")
                count += 1
            elif (int(lu[i]) in lc and int(lu[i])!=lc[i]):
                print("Close")
            elif (int(lu[i]) not in lc):
                print("Nope")
    print("Code Cracked")
    return 

print("Welcome, Let's see if you can guess my code\n")
generate_code()
print("Code Has Been Generated \n")
guess()