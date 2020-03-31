# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:54:56 2020

@author: Pratik

Daily Coding Problem: Problem #27 [Easy]
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""



def braketsclosed(str_value):
    dict_brackets = {')':'(', ']':'[','}':'{'}
    lst = []
    
    for char in str_value:
        if char in dict_brackets.values():
            lst.append(char)
        elif char in dict_brackets.keys():
            if(dict_brackets.get(char)==lst[-1]):
                lst.pop(-1)
            else:
                break
    
    if len(lst)==0:
        return True
    else:
        return False
            
            
str_value = "([])[]({})"
#str_value ="([)]"
#str_value ="((()"
print(braketsclosed(str_value))
        
    
