# -*- coding: utf-8 -*-

# 강좌: 컴퓨터의 개념 및 실습
# 날짜: 2018/03/23
# 작성자: 이건희
# 설명: [숙제02심화] 2. 트리테미우스 암호문


# 평문을 입력 받는다.
plaintext = input("평문: ")

# 알파벳을 나열한 텍스트가 자주 쓰이기 때문에 미리 지정해둔다.
alphabets = "abcdefghijklmnopqrstuvwxyz"

# find 함수로 알파벳을 0~25의 수로 변환해 첫 번째 알파벳에 해당하는 수에는 0을, 두 번째는 1을 더하는 방식으로 더한 뒤 26으로 나눈 나머지를 구한다.
first_number = alphabets.find(plaintext[0])
second_number = ( alphabets.find(plaintext[1]) + 1 ) % 26
third_number = ( alphabets.find(plaintext[2]) + 2 ) % 26
fourth_number = ( alphabets.find(plaintext[3]) + 3 ) % 26

# 0~25의 수를 알파벳으로 변환한다.
first_letter = alphabets[first_number]
second_letter = alphabets[second_number]
third_letter = alphabets[third_number]
fourth_letter = alphabets[fourth_number]

# 네 개의 알파벳을 연결해 암호문을 만들고 출력한다.
cyphertext = first_letter+second_letter+third_letter+fourth_letter
print("트리테미우스 암호문:",cyphertext)