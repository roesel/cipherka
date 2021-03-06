#!/usr/bin/env python27
#coding=utf8

def info():
    return {"name":"Morse (test)",
            "desc":"Překládá text do Morseovy abecedy.",
            "doc":"http://bla.bla.cz/bla",
            "version":"1"}

# Imports
import re

def run(input, parameters=None):
    # Load defaults parameters if none given
    if parameters == None:
    	parameters = {'unrec_replace': False,
    	              'unrec_keep': True,
    	              'unrec_ignore': False,
    	              'remove_diacritics': True,
    	              'replace_C_H_with_CH': False}
    #čistit české znaky
    #vyřešit co s nedefinovanymi
    ##přeskočit
    ##ponechat
    ##nahradit znakem - field
    #nahradit ch, ano/ne
    return str(code(input, parameters))
    
def code(string, parameters):
    # Optional: Pre-cleaning of known (but uncharted) czech characters
    if parameters['remove_diacritics'] == True:
        czech_characters = {"š":"s", "ě":"e", "č":"c", "ř":"r", "ž":"z", "ý":"y", "á":"a", "í":"i", "é":"e", "ú":"u", "ů":"u", "ť":"t", "ď":"d", "ň":"n", "ó":"o", "Š":"S", "Ě":"E", "Č":"C", "Ř":"R", "Ž":"Z", "Ý":"Y", "Á":"A", "Í":"I", "É":"E", "Ú":"U", "Ů":"U", "Ť":"T", "Ď":"D", "Ň":"N", "Ó":"O"}
        for v, k in czech_characters.items():
            string=re.sub(v,czech_characters[v],string)
    
    morse_dict = {" ":"",
               # Special characters
               ".":".-.-.-",
               ",":"--..--",
               "?":"..--..",
               "'":".----.",
               "!":"-.-.--",
               "/":"-..-.",
               "(":"-.--.",
               ")":"-.--.-",
               "&":".-...",
               ":":"---...",
               ";":"-.-.-.",
               "=":"-...-",
               "+":".-.-.",
               "-":"-....-",
               "_":"..--.-",
               "\"":".-..-.",
               "$":"...-..-",
               "@":".--.-.",
               # Numbers "":"",
               "1":".----",
               "2":"..---",
               "3":"...--",
               "4":"....-",
               "5":".....",
               "6":"-....",
               "7":"--...",
               "8":"---..",
               "9":"----.",
               "0":"-----",
               # Non-capital letters
               "a":".-", 
               "b":"-...", 
               "c":"-.-.", 
               "d":"-..", 
               "e":".", 
               "f":"..-.",
               "g":"--.",
               "h":"....",
               "i":"..",
               "j":".---",
               "k":"-.-",
               "l":".-..",
               "m":"--",
               "n":"-.",
               "o":"---",
               "p":".--.",
               "q":"--.-",
               "r":".-.",
               "s":"...",
               "t":"-",
               "u":"..-",
               "v":"...-",
               "w":".--",
               "x":"-..-",
               "y":"-.--",
               "z":"--..",
               # Capital letters
               "A":".-", 
               "B":"-...", 
               "C":"-.-.", 
               "D":"-..", 
               "E":".", 
               "F":"..-.",
               "G":"--.",
               "H":"....",
               "I":"..",
               "J":".---",
               "K":"-.-",
               "L":".-..",
               "M":"--",
               "N":"-.",
               "O":"---",
               "P":".--.",
               "Q":"--.-",
               "R":".-.",
               "S":"...",
               "T":"-",
               "U":"..-",
               "V":"...-",
               "W":".--",
               "X":"-..-",
               "Y":"-.--",
               "Z":"--.."}
    output="|"
    for letter in string:
        if letter in morse_dict:
            output += (morse_dict[letter]+"|")
        # Process an unrecognized character
        elif parameters['unrec_keep'] == True:
            output += letter	# Keep the character unmodified (don't convert to morse)
        elif parameters['unrec_replace'] == True:
            output += "(unrecognized character)"	# Replace the character with an error string
        elif parameters['unrec_ignore'] == True:
            output += ''	# Skip the character
        else:
            pass	# This should never happen
        
    ## Optional: |C|H| -> |CH| (czech morse code edit)
    if parameters['replace_C_H_with_CH'] == True:
        output=re.sub("\|\-\.\-\.\|\.\.\.\.\|","|----|",output)
    
    return output