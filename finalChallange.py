#!/usr/bin/env python
# 
# finalChallange.py
# This programs lets you write some text to a file, and retrieve it.
# Version 0.1 / march 3, 2016
# by J.Kroesschell <jaap at kroesschell-ictconsulting.ch>
# 

import os, sys


def main():
	myFile = askFilename()
	print("your selected filename is : " + myFile)
	action = askReadOrWrite()
	if action == 'W' :
		saveMyFile(myFile)
	elif action == 'R':
		readMyFile(myFile)
	else :
		print("No valid answer given")
	return

def askFilename():
	# Ask user for filename to be used
	dirs = os.listdir('.')
	for item in dirs:
		if item.endswith('.txt'):			
			print(item)
	myFile = raw_input("Please enter the Filename to be used. ")
	return myFile

def askReadOrWrite():
	userAction = raw_input("Do you wish to read or write to a file (r/w) ").upper()
	return userAction

def readMyFile(myFile):
	if os.path.exists(myFile): 
		with open(myFile, mode='r') as mygit config --global user.name "YOUR NAME"file:
		# myfile = open(myFile, mode='r')
			fileData = myfile.read()
			print(fileData)
			myfile.close()
	else:
		print("Sorry, the entered file does not exist. \n")
	return

def saveMyFile(myFile):
	content = raw_input("Please enter text to be written to the file : \n")
	with open(myFile, mode='w') as myfile:
	# myfile = open(myFile, mode='w')
		myfile.write(content)
		myfile.close()

	return content


main()