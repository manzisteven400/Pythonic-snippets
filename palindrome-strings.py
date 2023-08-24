# -*- coding: utf-8 -*-
"""
write a program that asks the user for a word and prints out whether the
word is a palindrome or not. the palindrome word reads the same forwards and 
backwards
"""
word = (input("Please enter a word: ")).strip()
reverse = word[::-1]
if word == reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")