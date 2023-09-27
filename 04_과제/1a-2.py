from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import base64

password=input("passphrase: ")

#개인키 읽어오기 


priKey=RSA.importKey(base64.b64decode(open("Alice_private.pem","rb").read()),passphrase=password)

enc_f=open("Enc.txt","rb") #암호화 파일 읽어오기
encrypted=enc_f.read()
enc_f.close()

decryptor=PKCS1_OAEP.new( priKey )  #복호화
decrypted=decryptor.decrypt(binascii.unhexlify(encrypted))
print("Decrypted: ",decrypted.decode('utf-8'))

