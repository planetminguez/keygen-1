#!/usr/bin/python
# -*- coding: utf-8 -*-
# This script creates a key. A character can be a letter (a-z, A-Z) or a number (0-9)
# © 2012 Exceen

from sys import argv
from os import system
from os.path import exists
from random import randint

class keygen(object):

	def __init__(self):

		self.letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') # you can add some letters, but leave A-Z and a-z there!
		self.letterslength = len(self.letters)
		self.tmpkey = self.letters[randint(0, 52)]
		
		# old code:
		# a = ord('A')
		# z = ord('Z')
		# for i in xrange(a, z+1):
		# letters.append(str(unichr(i)))
		# a = ord(str(unichr(a)).lower()) #97
		# z = ord(str(unichr(z)).lower()) #122
		# for i in xrange(a, z+1):
		# 	letters.append(str(unichr(i)))
		# for i in xrange(0, 10):
		# 	letters.append(i)'

	def create_tmpkey(self):
		# creating a temporary key
		self.tmpkey = '%s%s' % (self.tmpkey, self.letters[randint(0, self.letterslength-1)])

class questions(keygen):

	def __init__(self):
		self.prompt = '> '

	def amount_of_keys(self):
		print 'How many keys do you want to create?'
		return int(raw_input(self.prompt))

	def length_of_a_single_key(self):
		print 'How long should a single key be?'
		return int(raw_input(self.prompt))

class external_file(keygen):
	
	def __init__(self, filename):

		if not filename:
			print 'If you want to save the file with the keys, you have\nto add a second argument with the name of the file.'
			print 'e.g. "$ python keygen.py output.txt"'
		elif exists(filename):
			print 'The file does already exist and will be overwritten.\nIf you want to abort, press CTRL+C (^C), otherwise press RETURN'
			raw_input()
		else:
			print 'The file %r doesn\'t exist, it will be created' % filename

	def open_file(self, filename):
		if filename:
			self.dataset = open(filename, 'w')

	def close_file(self, filename):
		if filename is not False:
			self.dataset.close()


def main():
	try:
		script, filename = argv
	except:
		filename = False
	
	key_info = questions()

	amount = key_info.amount_of_keys()
	length_of_a_key = key_info.length_of_a_single_key()

	ex_file = external_file(filename)
	ex_file.open_file(filename)
	
	###############################
	# creating, printing and writing the key(s)

	for i in xrange(0, amount):
		
		keys = keygen() # first character already initialized with a letter

		for i in xrange(0, length_of_a_key - 1):
			keys.create_tmpkey()

		print keys.tmpkey

		if filename:
			keys.tmpkey = '%s\n' % keys.tmpkey
			ex_file.dataset.write(keys.tmpkey)
	
	ex_file.close_file(filename)



if __name__ == '__main__':
	main()