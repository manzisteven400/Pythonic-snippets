# -*- coding: utf-8 -*-
"""
Given two lists, write a program that returns a list that contains only 
the elements that are common between the two lists
"""

import random 

a = random.sample(range(1,30), 11)
print (a)
b = random.sample(range(1,30), 14)
print(b)
overlap = [i for i in set(a) if i in b]
print (overlap)