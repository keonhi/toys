# toys
polybius, trithem, vigenere toys


1.	카이사르 암호문
A.	문제 해결 방법
지난 과제에서 바뀐 부분은 다음과 같습니다. 숫자가 아닌 것이 있을 경우 “숫자를 입력하세요”라는 문구가 나오도록 하는 것은 if문을 쓰고 isdigit()을 사용합니다. for문을 이용해 알파벳 개수의 제약을 없애고 일반화합니다.

B.	코드 설명
# -*- coding: utf-8 -*-

# 암호화 키를 입력 받는다.
raw = input("암호화 키: ")
if raw.isdigit():
    key=int(raw)
    
    # 평문을 입력 받는다.
    plaintext = input("평문: ")

    # 알파벳을 나열한 텍스트가 자주 쓰이기 때문에 미리 지정해둔다.
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    cyphertext = ""
    for char in plaintext:
        # find 함수로 알파벳을 0~25의 수로 변환해 key를 더하고 26으로 나눈 나머지를 구한다.
        number = ( alphabets.find(char) + key ) % 26
    
        # 0~25의 수를 알파벳으로 변환한다.
        letter = alphabets[number]
        cyphertext += letter      
    print("카이사르 암호문:", cyphertext)
else:
    print("숫자를 입력하세요.")
C.	테스트 실행 결과
 

2.	트리테미우스 암호문
A.	문제 해결 방법
지난 과제에서 달라진 부분은 for문을 이용해 평문의 알파벳 개수에 대한 제약을 없앤 것입니다. 이 때 enumerate 함수를 사용해 인덱스와 문자열을 동시에 다뤘습니다.

B.	코드 설명
# -*- coding: utf-8 -*-

# 평문을 입력 받는다.
plaintext = input("평문: ")

# 알파벳을 나열한 텍스트가 자주 쓰이기 때문에 미리 지정해둔다.
alphabets = "abcdefghijklmnopqrstuvwxyz"

# cyphertext 생성
cyphertext = ""

# enumerate 함수를 이용해서 인덱스와 문자열을 동시에 가져온다.
for i, char in enumerate(plaintext):
    number = ( alphabets.find(char) + i ) % 26

    # 0~25의 수를 알파벳으로 변환한다.
    letter = alphabets[number]
    cyphertext += letter

print("트리테미우스 암호문:",cyphertext)
C.	테스트 결과
 

3.	비즈네르 암호문
A.	문제 해결 방법
지난 과제에서 달라진 부분은 for문을 이용해 평문의 알파벳 개수에 대한 제약을 없앤 것입니다. 이 때 enumerate 함수를 사용해 인덱스와 문자열을 동시에 다뤘습니다.

B.	코드 설명
# -*- coding: utf-8 -*-

# 암호화 키를 입력 받는다.
key = input("암호화 키: ")

# 알파벳을 나열한 텍스트가 자주 쓰이기 때문에 미리 지정해둔다.
alphabets = "abcdefghijklmnopqrstuvwxyz"

# 평문 입력 받는다. cyphertext 생성
plaintext = input("평문: ")
cyphertext = ""

# enumerate 함수를 이용해서 인덱스와 문자열을 동시에 가져온다.
for i, char in enumerate(plaintext):

    # i를 key의 길이로 나눈 나머지를 이용한다.
    number = ( alphabets.find(char) + alphabets.find(key[i%len(key)]) ) % 26
        
    letter = alphabets[number]
    cyphertext += letter  
   
print("비즈네르 암호문:",cyphertext)

C.	테스트 결과
 


4.	폴뤼비오스 암호문
A.	문제 해결 방법
지난 과제에서 달라진 부분은 for문을 이용해 평문의 알파벳 개수에 대한 제약을 없앤 것입니다.

B.	코드 설명
# -*- coding: utf-8 -*-

# 평문을 입력 받는다.
plaintext = input("평문: ")

# 알파벳을 나열한 텍스트를 저장한다. j는 제외한다.
alphabets = "abcdefghiklmnopqrstuvwxyz"
cyphertext = ""

# newtext를 만들고 j가 있을 경우 이를 i로 바꿔 저장한다.
newtext= ""
for char in plaintext:
    if char == "j":
       newtext += "i"
    else:
        newtext += char
       
# newtext의 위치를 5로 나눈 몫이 십의 자리, 나머지가 일의 자리가 되도록 한다.
for char1 in newtext:
    coordinate = ((alphabets.find(char1))//5)*10+(alphabets.find(char1))%5  
    # 한 자리 수일 경우 0이 채워지도록 한다.
    cyphertext += str(coordinate).zfill(2) + " "
    
print("폴뤼비오스 암호문:",cyphertext)

C.	테스트 결과
 
