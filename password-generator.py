# -*- coding: utf-8 -*-
"""
write a password generator
"""

import string
import random 

def password_generator(size=8, characters= string.ascii_letters + string.digits 
                       + string.punctuation):
    return ''.join(random.choice(characters) for _ in range(size))


while True:
    try:
        print(password_generator(int(input("How long is your password: how many characters? Enter a number: "))))
    except ValueError:
        pass
    else:
        break