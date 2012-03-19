#!/usr/bin/env python27
#coding=utf8

# Imports
import re

shift_field=[]

def process(input, parameters=None):
    global shift_field
    shift_field=[]
    return str(code(input, "letadlo"))	# Encode
    #return str(code(input, "letadlo", True))	# Decode


pass_pos=0
def shiftIt():
    global pass_pos
    global shift_field
    if pass_pos<(len(shift_field)-1):
        pass_pos+=1
        return shift_field[pass_pos-1]
    else:
        pass_pos=0
        print("shift_field:"+str(shift_field))
        return shift_field[-1]    
    
def code(string, password, decode=False):
    global pass_pos
    # Optional: Pre-cleaning of known (but uncharted) czech characters
    czech_characters = {"š":"s", "ě":"e", "č":"c", "ř":"r", "ž":"z", "ý":"y", "á":"a", "í":"i", "é":"e", "ú":"u", "ů":"u", "ť":"t", "ď":"d", "ň":"n", "ó":"o",
                        "Š":"S", "Ě":"E", "Č":"C", "Ř":"R", "Ž":"Z", "Ý":"Y", "Á":"A", "Í":"I", "É":"E", "Ú":"U", "Ů":"U", "Ť":"T", "Ď":"D", "Ň":"N", "Ó":"O"}
    for v, k in czech_characters.items():
        string=re.sub(v,czech_characters[v],string)
    # Capitalizing the input
    string=string.upper()
    letter_dict = {
               # Non-capital letters
               "A":0, 
               "B":1, 
               "C":2, 
               "D":3, 
               "E":4, 
               "F":5,
               "G":6,
               "H":7,
               "I":8,
               "J":9,
               "K":10,
               "L":11,
               "M":12,
               "N":13,
               "O":14,
               "P":15,
               "Q":16,
               "R":17,
               "S":18,
               "T":19,
               "U":20,
               "V":21,
               "W":22,
               "X":23,
               "Y":24,
               "Z":25}
    letter_dict_back = {
               # Non-capital letters
               0:"A", 
               1:"B", 
               2:"C", 
               3:"D", 
               4:"E", 
               5:"F",
               6:"G",
               7:"H",
               8:"I",
               9:"J",
               10:"K",
               11:"L",
               12:"M",
               13:"N",
               14:"O",
               15:"P",
               16:"Q",
               17:"R",
               18:"S",
               19:"T",
               20:"U",
               21:"V",
               22:"W",
               23:"X",
               24:"Y",
               25:"Z"}
    # Encoding password into a list with numbers (where possible)
    password=password.upper()
    for letter in password:
        if letter in letter_dict:
            shift_field.append(letter_dict[letter])
        else:
            pass
            
    # Encoding string into a list with numbers (where possible)
    string_num=[]
    for letter in string:
        if letter in letter_dict:
            string_num.append(letter_dict[letter])
        else:
            string_num.append(letter)
    #output = str(string_num) 
    output=""
    for i in range(0,len(string_num)):
         if isinstance(string_num[i], int):
             if decode == True:
                 shifted = (26+string_num[i]-shiftIt())%26
             else:
                 shifted = (string_num[i]+shiftIt())%26
             output+=letter_dict_back[shifted]
         else:
             output+=string_num[i]
    pass_pos=0
    return output