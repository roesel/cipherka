#!/usr/bin/env python27
#coding=utf8

# Imports
import re
import math

def process(input, parameters=None):
    return str(code(input))
    
def code(string):
    length=len(string)
    sharp_side=math.sqrt(length)
    int_side=int(math.ceil(sharp_side))
    letter_field=[]
    for let in string:
        letter_field.append(let)    
    table_field=[]
    for i_col in range(0,int_side):
        table_field.append([])
        for i_row in range(0,int_side):
            try:
                table_field[(i_col)].append(letter_field[0])
                letter_field.remove(letter_field[0])
            except:
                break
    output=""
    for a in table_field:
        output=output+str(a)+"\n"
    return output