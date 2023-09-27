import hmac
import hashlib

#sender

f=open('1.txt','r')
f2=open('H.txt','w')

password=input("pwd:")
message=''

h=hmac.new(password.encode('utf-8'),message.encode('utf-8'),hashlib.sha256) 
message=f.read(1024)
f2.write(message)
h.update(message.encode('utf-8'))
mac= h.digest()
f2.write(mac.decode('iso-8859-1'))
print("HMAC: ",mac)



