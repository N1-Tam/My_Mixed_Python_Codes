# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 19:40:16 2026

@author: Konstantin.Playford
"""
import sys
x = int(input("Enter a number: "))
if x == 0: sys.exit("Error! '0' detected!")
y = int(input("Enter a second number: "))
if y == 0: sys.exit("Error! '0' detected!")
choice = int(input("Enter an operation: 1(X), 2(/), 3(+), or 4(-): "))
if choice == 1:
    print (x * y)
elif choice == 2:
    print (x / y)
elif choice == 3:
    print (x + y)
elif choice == 4:
    print (x - y)
    
exit = input("Hit a key and hit ENTER to exit: ")
if exit != 0: sys.exit