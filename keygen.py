#!/usr/bin/python
# -*- coding: utf-8 -*-
# This script creates a key. A character can be a letter (a-z, A-Z) or a number (0-9)
# © 2012 Exceen

from sys import argv
from os import system
from os.path import exists
from random import randint

try:
	script, filename = argv
except:
	script = argv
	filename = False

system('clear')
print '%r\n' % script

###############################
# creating the array 'letters'
a = ord('A')
z = ord('Z')
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

for i in xrange(a, z+1):
	letters.append(str(unichr(i)))

a = ord(str(unichr(a)).lower()) #97
z = ord(str(unichr(z)).lower()) #122

for i in xrange(a, z+1):
	letters.append(str(unichr(i)))

for i in xrange(0, 10):
	letters.append(i)

###############################
# asking some questions
prompt = '> '

print 'How many keys do you want to create?'
amount_of_keys = int(raw_input(prompt))

print '\nHow long should a single key be?'
length_of_a_key = int(raw_input(prompt))

if not filename:
	print '\nIf you want to save the file with the keys, you have\nto add a second argument with the name of the file.'
	print 'e.g. "$ python password_generator.py keys.txt"'
elif exists(filename):
	print '\nThe file does already exist and will be overwritten.\nIf you want to abort, press CTRL+C (^C), otherwise press RETURN'
	raw_input()
else:
	print '\nThe file %r doesn\'t exist, it will be created' % filename

if not filename:
	print_out = True
else:
	print '\nDo you want to print the keys out on the screen? (y/n)'
	print_out = raw_input(prompt).lower()

	if print_out == 'n' or print_out == 'no':
		print_out = False
	else:
		print_out = True

#only small letters/caps/numbers?
#...
#first character always not(number)?
#...
#last character always a number?
#...

if print_out:
	length_of_the_line = length_of_a_key + 1
	if length_of_the_line < 16:
		length_of_the_line = 16

	print '\nKeys:\n', '-' *length_of_the_line

###############################
# creating and printing the key(s)
letterslength = len(letters)

if filename:
	dataset = open(filename, 'w')

for i in xrange(0, amount_of_keys):

	key = ''
	for i in xrange(0, length_of_a_key):
		key = '%s%s' % (key, letters[randint(0, letterslength-1)])
	
	if print_out:
		print key

	if filename:
		key = '%s\n' % key
		dataset.write(key)

if filename is not False:
	dataset.close()