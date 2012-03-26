#!/usr/bin/env python27
#coding=utf8

def info():
    return {"name":"Flip (test)",
            "desc":"Navrací text s převrácenými písmeny.",
            "doc":"http://bla.bla.cz/bla",
            "version":"1"}

import reverse

def run(input, parameters=None):
    print('Module \'flip\': WORK IN PROGRESS')
    input = reverse.run(input)
    print('a',input)
    output = ''
    for char in input:
        if char in subs and subs[char] != '':
            flippedchar = subs[char]
        else:
            # Character not in table
            flippedchar = char    # Use original character
            #flippedchar = ' '    # Use space instead
        output += flippedchar
    return output

subs = {
'a' : '',
'b' : 'q',
'c' : '',
'd' : 'p',
'e' : '',
'f' : '',
'g' : '',
'h' : 'y',
'i' : '!',
'j' : '',
'k' : '',
'l' : '',
'm' : '',
'n' : '',
'o' : '',
'p' : 'd',
'q' : 'b',
'r' : '',
's' : '',
't' : '',
'u' : '',
'v' : '',
'w' : '',
'x' : '',
'y' : '',
'z' : '',
'\'' : ',',
',' : '\'',
'!' : ''
}