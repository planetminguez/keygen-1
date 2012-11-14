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
	filename = False

class keygen(object):

	def __init__(self):
		self.letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') # you can add some letters or remove the diggits, but leave A-Z and a-z there!
		self.letterslength = len(self.letters)
		self.tmpkey = self.letters[randint(0, 52)]
		
	def create_keys(self):
		key_info = keygen_information()
		ex_file = external_file()

		for i in xrange(0, key_info.amount):
			
			keys = keygen() # first character already initialized with a letter
			keys.create_single_key(key_info.length)
	
			print keys.tmpkey

			ex_file.write_key(keys.tmpkey)
	
		ex_file.close_file()

	def create_single_key(self, length_of_a_key):
		# creating a temporary key
		for i in xrange(0, length_of_a_key - 1):
			self.tmpkey = '%s%s' % (self.tmpkey, self.letters[randint(0, self.letterslength-1)])
		return self.tmpkey

class keygen_information(keygen):

	def __init__(self):
		self.prompt = '> '
		self.amount = self.amount_of_keys()
		self.length = self.length_of_a_single_key()

	def amount_of_keys(self):
		print 'How many keys do you want to create?'
		return int(raw_input(self.prompt))

	def length_of_a_single_key(self):
		print 'How long should a single key be?'
		return int(raw_input(self.prompt))

class external_file(keygen):
	def __init__(self):

		if not filename:
			print 'If you want to save the file with the keys, you have\nto add a second argument with the name of the file.'
			print 'e.g. "$ python keygen.py output.txt"'
		elif exists(filename):
			print 'The file does already exist and will be overwritten.\nIf you want to abort, press CTRL+C (^C), otherwise press RETURN'
			raw_input()
		else:
			print 'The file %r doesn\'t exist, it will be created' % filename

		if filename:
			self.dataset = open(filename, 'w')

	def close_file(self):
		if filename != False:
			self.dataset.close()

	def write_key(self, key):
		if filename:
			self.dataset.write('%s\n' % key)


def main():
	keygen().create_keys()

if __name__ == '__main__':
	main()