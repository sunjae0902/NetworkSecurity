import socket
import json
import base64

from Crypto import Random
from Crypto.Hash import HMAC

#Challenge-Response protocol (server)

idpw = { 'Alice':'1234', 'Bob':'abcd' }

com_socket = socket.socket()
com_socket.bind(('127.0.0.1',2500))
com_socket.listen(10)

print('Waiting connection from client... ')

connection, address =com_socket.accept()
print('Connected from client... ')

msg1 =connection.recv(1024).decode()
uid=json.loads( msg1)['uid']
print ("\nReceived : ", msg1)

nonce= Random.get_random_bytes (8)
nonceStr=base64.b64encode(nonce).decode()
msg2=  json.dumps ( {'nonce': nonceStr })

connection.send(msg2.encode()) 
print ("\nSent : ", msg2)

msg3 =connection.recv(1024).decode()
hmacStr= json.loads( msg3) ['hmac'].encode()
hmac=base64.b64decode(hmacStr)
print ("\nReceived : ", msg3)
pw = idpw[uid].encode()

h2 = HMAC.new(pw)
hmac2 = h2.update(nonce).digest()

# print("hmac: ",hmac)
# print ("hmac2: ",hmac2)

if  hmac == hmac2 :
    print ("\nVerified: ", uid)
else:
	print("\nNotVerified")

