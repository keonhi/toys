# -*- coding: utf-8 -*-

# 암호화 키를 입력 받는다.
key = input("암호화 키: ")

# 알파벳을 나열한 텍스트가 자주 쓰이기 때문에 미리 지정해둔다.
alphabets = "abcdefghijklmnopqrstuvwxyz"

# find 함수로 알파벳을 0~25의 수로 변환한다.
first_key = alphabets.find(key[0])
second_key = alphabets.find(key[1])
third_key = alphabets.find(key[2])
fourth_key = alphabets.find(key[3])

# 평문을 입력 받는다.
plaintext = input("평문: ")

# find 함수로 알파벳을 0~25의 수로 변환해 key를 더하고 26으로 나눈 나머지를 구한다.
first_number = ( alphabets.find(plaintext[0]) + first_key ) % 26
second_number = ( alphabets.find(plaintext[1]) + second_key ) % 26
third_number = ( alphabets.find(plaintext[2]) + third_key ) % 26
fourth_number = ( alphabets.find(plaintext[3]) + fourth_key ) % 26

# 0~25의 수를 알파벳으로 변환한다.
first_letter = alphabets[first_number]
second_letter = alphabets[second_number]
third_letter = alphabets[third_number]
fourth_letter = alphabets[fourth_number]

# 네 개의 알파벳을 연결해 암호문을 만들고 출력한다.
cyphertext = first_letter+second_letter+third_letter+fourth_letter
print("비즈네르 암호문:",cyphertext)