# 파이썬에서의 자료형(Data-type)
# int 형
print(type(17))
# float 형
print(type(10.77779))
# str 형
print(type("안녕하세요"))

# 반지름이 r인 구의 부피는 4/3 * PI * r의 세제곱
# 반지름이 5인 구의 부피를 계산하는 프로그램
from math import *
r = 5.0
# volume = 4.0 / 3.0 * pi * r**3
volume = 4.0 / 3.0 * pi * pow(r, 3)
print("구의 부피 : ", volume)
# 문자열 + float은 타입이 일치가 안되어 문자열을 생성할 수 없음
# 해결하기 위한 방법은 실수값을 str()을 이용하여 문자열로 변환하면
# +연산이 이루어진다.
print("구의 부피 : ", str(volume))
# 구의 겉넓이 공식 : 4 * pi * r의 제곱
outer_area = 4 * pi * pow(r, 2)
print("구의 겉넓이 : ", outer_area)
