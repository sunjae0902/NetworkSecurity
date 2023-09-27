import hmac
import hashlib

f1=open('1.txt','r')

password=input("pwd:")
message=''

h1=hmac.new(password.encode('utf-8'),message.encode('utf-8'),hashlib.sha256) 
message=f1.read(1024)
h1.update(message.encode('utf-8'))
mac= h1.digest()
print("1.txt's HMAC: ",mac)


#receiver

f2=open("H.txt",'r')


h2=hmac.new(password.encode('utf-8'),message.encode('utf-8'),hashlib.sha256)
message=f2.read(1024)
h2.update (message.encode('utf-8'))
mac2= h2.digest()
print("H.txt's HMAC: ",mac2)


if mac == mac2 : 
	print ("OK")
else:
	print("NOK")


