from Crypto.Hash import HMAC
import os

infile=open('H.txt','rb')

password=input("pwd:").encode()
chunk_size = 1024
filesize = os.path.getsize("H.txt")

textfile = b''
while True:
	chunk = infile.read(chunk_size)
	if len(chunk) == 0:
		break;
	textfile += chunk
mac1 = textfile[filesize-16:] # 마지막hmac 값 (16바이트) 
textfile = textfile[:filesize-16] #hmac 값을 제외한 본문 내용

h = HMAC.new(password)
h.update(textfile) # hash update
mac2 = h.digest()
print("HMAC: ",mac2)


if mac1 == mac2 : 
	print ("OK")
else:
	print("NOK")


