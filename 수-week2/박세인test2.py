# -*- coding: utf-8 -*-
"""박세인test2.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o6sckyR5puSquaMXINhSF6VtzJfLV5Ob
"""

num1=int(input("숫자 정수1를 입력하세요:"))
num2=int(input("숫자 정수2를 입력하세요:"))
num3=int(input("숫자 정수3을 입력하세요:"))
tot=num1+num2+num3
print(f"{num1}과 {num2}의 합계는 {tot:,}이다.")

국어점수=int(input("국어점수를 입력하세요:"))
영어점수=int(input("영어점수를 입력하세요:"))
수학점수=int(input("수학점수을 입력하세요:"))
총점=국어점수+영어점수+수학점수
평균=총점/3
print("총점:",총점)
print("평균: {0:.2f}".format(평균))