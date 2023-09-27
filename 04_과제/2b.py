from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
import hashlib
from Crypto.Signature import PKCS1_PSS
import base64


sig_f=open("sig.txt","rb")
sig = base64.b64decode(sig_f.read())
sig_f.close()

pub_f=open("Public.der","rb")
pubKeyDER=pub_f.read()
pub_f.close()

pubKey = RSA.import_key(pubKeyDER)
verifier=PKCS1_PSS.new(pubKey)

txt_f=open("1.txt","r");
h = SHA.new(bytes(txt_f.read(),'utf-8'))
txt_f.close()
	
if(verifier.verify(h,sig)):
   	print("verified")
else:
   	print("not verified")
