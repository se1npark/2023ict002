# -*- coding: utf-8 -*-
"""박세인test4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fq4odCz_FQ0EN4cfejaSCo-313cShw26
"""

용도=int(input())
kwh=float(input())

if 용도 == 1 :
  print("용도: 주택용", "사용량:",kwh, "전기요금:", fee+kwh*88)
elif 용도 == 2:
  print("용도: 공업용", "사용량:", kwh, "전기요금:", fee+kwh*182)
else :
  print("용도: 산업용", "사용량:", kwh, "전기요금:", fee+kwh*275)

name=input("이름: ")
국어점수, 영어점수, 수학점수=map(int,input(). split())

총점=국어점수+영어점수+수학점수
평균=round(총점/3,2)

if 평균 >= 95 :
  print("학점:A+")
elif 평균 >=90 :
  print("학점:A")
elif 평균 >=85 :
  print("학점:B+")
elif 평균 >=80 :
  print("학점:B")
elif 평균 >=75 :
  print("학점:C+")
elif 평균 >=70 :
  print("학점:C")
elif 평균 >=65 :
  print("학점:D")
elif 평균 >=60:
  print("학점:D+")
else :
  print("학점:F")

print(f"{name}의 총점은 {총점}점, 평균은 {평균}점입니다")