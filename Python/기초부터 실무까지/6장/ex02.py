# 정수를 사용자로부터 입력받아서 제곱한 값을 반환하는 함수를 만들어 보시오.
# 사용자가 5를 입력을 하면 출력값은 25가 되어야 한다.

# 만들어보기
# num = int(input("제곱할 정수를 입력하세요 : "))
#
# def square(n):
#     return pow(n, 2)
#
# print(square(num))


# 풀이
from calc import *

# 함수 호출
num = int(input("제곱하고 싶은 정수를 입력하세요 : "))
print("제곱하기 전 : ", num)
print("제곱한 후 : ", square(num))
