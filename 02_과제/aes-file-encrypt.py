from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os, random, struct

def encrypt_file(key, filename):
	
	chunk_size = 1024
	
	output_filename = filename + '.encrypted'

	# Initialization vector
	iv = os.urandom(16)
	
	#create the encryption cipher
	encryptor = AES.new(key, AES.MODE_CBC, iv)
	
	#Determine the size of the file
	filesize = os.path.getsize(filename)
	
	#Open the output file and write the size of the file. 
	#We use the struct package for the purpose.
	with open(filename, 'rb') as inputfile:
		with open(output_filename, 'wb') as outputfile:
			outputfile.write(iv)
			outputfile.write(struct.pack('<Q', filesize))

			while True:
				chunk = inputfile.read(chunk_size)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += b' ' * (16 - len(chunk) % 16)

				outputfile.write(encryptor.encrypt(chunk))

password = b"password"

def getKey(password):
	hasher = SHA256.new(password)
	return hasher.digest()
	
encrypt_file(getKey(password), 'file.txt');
