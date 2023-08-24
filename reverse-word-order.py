# -*- coding: utf-8 -*-
"""
The program let's the user type something and return the word(s) in reverse
order'

"""
import re 

def main():
    user_input = input("Type something: ")
    reverse =  reverse_word(user_input)
    print(reverse)

def reverse_word(w):
    if not bool(re.search(r"\s", w)):
           return(w[::-1])
    else:
          return ' '.join(w.split()[::-1])
         
 
main()