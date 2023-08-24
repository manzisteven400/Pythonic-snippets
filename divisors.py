# -*- coding: utf-8 -*-
"""
write a program that asks the user for a number and prints out a list of all 
divisors of that number
"""

while True:
    try:
        number = int(input("Enter a number: "))
        potential_divisors = list(range(1,number+1))
        
        list_of_divisors = []
        
        for i in potential_divisors:
            if number % i == 0:
                list_of_divisors.append(i)
        print(list_of_divisors)
    except ValueError:
        pass
    else:
        break