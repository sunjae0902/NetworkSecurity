from Crypto.Hash import HMAC

# 사용자에게 key 입력 받아 hmac생성 후 출력하기
# 생성된 hmac값을 기존 1.txt뒤에 붙여서 H.txt로 저장하기

infile=open('1.txt','rb')
outfile=open('H.txt','wb')

password=input("pwd:").encode()
message=''
chunk_size=1024

h=HMAC.new(password) #해시값 생성

while True:
	chunk = infile.read(chunk_size)
	if len(chunk) == 0:
		break;
	outfile.write(chunk) # 1.txt파일 내용 복사 
	h.update(chunk) #해시값 갱신
hmac = h.digest()
print("HMAC: ",hmac) #화면에 출력 후, H.txt 파일에 씀
outfile.write(hmac)



