from Crypto.Hash import HMAC
import MD5

#sender

password=b'input("pwd:")'

h=HMAC.new(password) 
h.update (b'message')
mac= h.digest()

#receiver

h=HMAC.new( b'password')
h.update (b'message')
mac2= h.digest()


if mac == mac2 : 
	print ("OK")
else:
	print("NOK")


