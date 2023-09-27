from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

keyPair = RSA.generate(2048)

f1=open("Alice_private.pem","wb")
priKeyPEM= base64.b64encode(keyPair.export_key (passphrase="1234")) #개인키
#print(priKeyPEM)
f1.write(priKeyPEM)
f1.close()


f2=open("Alice_public.pem","wb")
pubkey = keyPair.publickey( ) 
pubKeyPEM=base64.b64encode(pubkey.export_key()) #공개키
#print(pubKeyPEM)
f2.write(pubKeyPEM)
f2.close()
