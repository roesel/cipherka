#!/usr/bin/env python27
#coding=utf8
def process(input, parameters=None):
	#return str(input)[::-1]
	print('Module \'reverse\': PRE-ALPHA TESTING VERSION')
	output = []
	temp = ''
	for i in range(len(input)):
		letter = input[i]
		if temp != '':
			temp += letter
			output += [temp]
			temp = ''
			continue
		elif ord(letter) > 128:	# Needs to be tested!
			temp = letter
			continue
		output += [letter]
	output.reverse()
	realoutput = ''
	for letter in output:
		realoutput += letter
	return realoutput