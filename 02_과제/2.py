from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os
import struct

def decrypt_file(key, iv, filename):
    chunk_size = 1024
    output_filename = os.path.splitext(filename)[0] + '.decrypted'
    
    # Open the encrypted file and the initialization vector.
    # The IV is required for creating the cipher.
    with open(filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        
        # Create the cipher using the key and the IV.
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        
        # Write the decrypted data to the output file.
        with open(output_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)

# Key, IV, 및 암호화된 파일 이름을 지정합니다.
key = b'ABCDEF0123456789'  # 16 바이트 키
iv = b'Netsec@Soongsil.'   # 16 바이트 IV
encrypted_file = 'enc1.txt'

# 암호 해독을 수행하고 결과를 출력합니다.
decrypt_file(key, iv, encrypted_file)

