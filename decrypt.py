#!/usr/bin/python3

import os
from cryptography.fernet import Fernet

#getting all files in files variable

files = []

for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	else:
		files.append(file)

#opening thekey.key file and setting it to a variable

with open("thekey.key", "rb") as key:
	secret_key = key.read()

#setting up kinda like password to run the decrypt.py script

password = "NOOB"
i = input("Enter a password loser: ")
if i == password:
	# here, we are opening every single file in this directry and read it and decrypting it and saving it.
	for file in files:
		with open(file, "rb") as rf:
			content = rf.read()
		dec_content = Fernet(secret_key).decrypt(content)
		with open(file, "wb") as wf:
			wf.write(dec_content)
	print("CONGO")
else:
	print("You suck at everthing<?>")


print("Decryption Done!!!")
#pasword is "NOOB"
