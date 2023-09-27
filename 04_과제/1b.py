from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import binascii
import base64

f=open("Alice_public.pem","rb")
pubKeyPEM=f.read()
pubKey= RSA.importKey(base64.b64decode(pubKeyPEM))
f.close()

txt_f=open("1.txt","r")
text=txt_f.read()
txt_f.close()

encryptor = PKCS1_OAEP.new ( pubKey ) 
encrypted=encryptor.encrypt(bytes(text, 'utf-8'))

enc_f=open("Enc.txt","wb")
enc_f.write(binascii.hexlify(encrypted))
enc_f.close()
