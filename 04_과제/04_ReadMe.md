# 과제 4-1
### :키쌍을 생성하여, 1.txt파일을 공개키로 암호화하여 저장하고, 사용자에게 passphrase를 입력받아 개인키로 복호화한 결과를 출력하기

# 과제 4-2
### :RSA 전자서명
#### - 2a.py<br/>- 키쌍 생성, 공개키를 der 형식으로 저장<br/>  1.txt를 읽어서 서명 값을 base64 encoding하여 sig.txt에 저장
#### - 2b.py<br/>- 공개키 파일과 1.txt, sig.txt를 읽은 뒤 원본에 대한 서명을 검증하여<br/>맞으면 "verified", 틀리면 "not verified"가 출력되도록 작성
