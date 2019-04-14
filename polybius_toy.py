# -*- coding: utf-8 -*-

# 평문을 입력 받는다.
plaintext = input("평문: ")

# 알파벳을 나열한 텍스트를 저장한다. j는 제외한다.
alphabets = "abcdefghiklmnopqrstuvwxyz"

# newtext를 만들고 j가 있을 경우 이를 i로 바꿔 저장한다.
newtext= ""
for char in plaintext:
    if char == "j":
       newtext += "i"
    else:
        newtext += char
       
# newtext의 위치를 5로 나눈 몫이 십의 자리, 나머지가 일의 자리가 되도록 한다.         
first_number = ((alphabets.find(newtext[0]))//5)*10+(alphabets.find(newtext[0]))%5
second_number = ((alphabets.find(newtext[1]))//5)*10+(alphabets.find(newtext[1]))%5
third_number = ((alphabets.find(newtext[2]))//5)*10+(alphabets.find(newtext[2]))%5
fourth_number = ((alphabets.find(newtext[3]))//5)*10+(alphabets.find(newtext[3]))%5

# 한 자리 수일 경우 앞에 0이 출력되도록 설계한다.
print("폴뤼비오스 암호문: {:02d} {:02d} {:02d} {:02d}".format(first_number, second_number, third_number, fourth_number))