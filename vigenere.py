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