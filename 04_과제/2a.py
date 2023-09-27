from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
from Crypto.Util.asn1 import *
import binascii
import base64

key=RSA.generate(2048)
pubkey=key.publickey()
pubKeyDER=pubkey.export_key(format="DER")

pub_f=open("Public.der","wb")
pub_f.write(pubKeyDER)
pub_f.close()


txt_f=open("1.txt","r")
msg=txt_f.read()
h=SHA.new()
h.update(bytes(msg,"utf-8"))
signer=PKCS1_PSS.new(key)
sig=signer.sign(h)

sig_f=open("sig.txt","w")
sig_f.write(base64.b64encode(sig).decode('utf-8'))
sig_f.close()

