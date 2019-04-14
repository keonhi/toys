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