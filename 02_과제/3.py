from Crypto.Cipher import AES
from Crypto.Util import Counter
import os, random, struct

# CTR모드로 Enc2.txt 파일을 복호화하여 화면에 출력하는 프로그램

def decrypt_file(key, filename):
	chunk_size = 1024

	with open(filename, 'rb') as infile:
		ctr = Counter.new(128)

		origsize = struct.unpack('I', infile.read(struct.calcsize('I')))[0]
		
		decryptor = AES.new(key, AES.MODE_CTR, counter=ctr)
		
		remsize = origsize
		while remsize >= chunk_size:
			chunk = infile.read(chunk_size)
			remsize -= chunk_size
			print(decryptor.decrypt(chunk).decode(), end='')

		if remsize > 0:
			chunk = infile.read(chunk_size)
			decryptedStr = decryptor.decrypt(chunk).decode()
			print(decryptedStr[:remsize])

decrypt_file(b'ABCDEF0123456789', 'enc2.txt')

