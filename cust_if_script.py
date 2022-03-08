#!/usr/bin/env python3

password = input("Enter a new password: ")

passlen = len(password)

if passlen <= 6:
        print("Password Strenth: Weak: ")
elif passlen == 7 or passlen <= 12:
    print("Password Strenght: Medium")
else:
    print("Password Strength: Strong")



