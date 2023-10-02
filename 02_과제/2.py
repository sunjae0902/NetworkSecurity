from Crypto.Cipher import AES
import os, random, struct #struct: 파이썬과 c사이 구조체 자료형 간 데이터 변환

# enc1.txt 파일을 복호화하여 화면에 출력하는 프로그램
								   
def decrypt_file(key, filename):
	chunk_size = 1024  #1024바이트 단위로 읽어옴
	with open(filename, 'rb') as infile:
		iv = b'Netsec@Soongsil.'
		origsize = struct.unpack('I', infile.read(struct.calcsize('I')))[0] 
# format 문자열에 맞춰 buffer(infile)에서크기에 맞춰 언패킹

 # Create the cipher using the key and the IV. -> 복호화 객체 생성
		decryptor = AES.new(key, AES.MODE_CBC, iv)
		remsize = origsize

		while remsize >= chunk_size: # 단위만큼 읽어오면서 끝날때까지 반복
			chunk = infile.read(chunk_size)
			remsize -=chunk_size
			print(decryptor.decrypt(chunk).decode(),end='')

		if remsize > 0: # 1024씩 처리하고 남은 데이터 처리
			chunk = infile.read(chunk_size)
			decryptedStr = decryptor.decrypt(chunk).decode()
			print(decryptedStr[:remsize])

			


# 암호 해독을 수행하고 결과를 출력합니다.
decrypt_file(b'ABCDEF0123456789','enc1.txt')

