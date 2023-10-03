# Challenge-Response 프로토콜을 hash 대신 HMAC을 사용하도록 기존 코드 수정하기
### msg1 : 클라이언트에서 uid 입력받아 전송 
### msg2 : 서버는 nonce 값을 생성하여 전송
### msg3 : 클라이언트는 nonce 값을 받고 pwd 입력받아 hmac 값을 생성하여 전송 -> 서버에서 검증 후 결과 출력
