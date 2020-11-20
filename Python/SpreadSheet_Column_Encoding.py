# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:38:42 2020
@author: Pratik

Write a function to convert 'A'=1, 'C'=3,... 'AA'=26.....'ZZ'=702
"""

def convert_col_to_num(str):
    words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {}
    l = len(str)
    
    for i, val in enumerate(words):
        d[val]=i+1
    
    if l==0:
        return 0
    elif l==1:
        if not (str[0].isdigit()):
            return d[str]
        else:
            return 'Incorrect Input'
    else:
        i = 0
        val = 1
        while l>1:
            if not (str[i].isdigit()):
                val=val*d[str[i]]*26
                l-=1
                i+=1
            else:
                return 'Incorrect Input'
        
        if l ==1:
            val+=d[str[i]]
        
        return val
            
        

#test
print(convert_col_to_num(''))
print(convert_col_to_num('A'))
print(convert_col_to_num('AA'))
print(convert_col_to_num('ZZ'))
print(convert_col_to_num('AAA'))
print(convert_col_to_num('A1A'))
print(convert_col_to_num('111'))
print(convert_col_to_num('1'))

