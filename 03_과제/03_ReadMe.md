# 과제 3-0
### :(brute-force 알고리즘) N개의 0 bit으로 hash값이 나오는 입력값 찾기 -> 최초의 24비트가 0이 나오는 소스값 찾기
#### - SHA384 사용
#### - N bytes

# 과제 3-1
### :동일하게 메시지를 HMAC하여 나오는 해시값 비교하여 무결성 검증하기
#### - 1a.py<br/>• 1.txt를 읽어서 HMAC을 생성 후 출력하기 ( key는 사용자에게 입력받기 )<br/>• 1.txt 파일 끝에 HMAC을 붙여서 H.txt로 저장<br/>- 1b.py<br/>• H.txt을 읽어서 파일 무결성 검사 ( key를 사용자에 입력 받기 )
#### - HMAC 값을 print하고 무결하면 "OK" 아니면 "NOK"를 print
