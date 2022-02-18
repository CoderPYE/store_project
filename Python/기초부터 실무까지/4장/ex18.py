# 주사위 눈을 랜덤으로 발생시켜서 해당하는 숫자를 출력하는 프로그램을 만들기
# randint() 함수를 검색하여 사용법을 익힌 후 프로그램을 작성하시오.

# randint(a, b) ---> 인자로 들어온 a, b 사이의 랜덤한 정수를 반환한다.(a <= N <= b)

# 만들어보기
# from random import *
#
# dice = randint(1, 6)
#
# if dice == 1:
#     print("주사위 숫자는 1입니다.")
# elif dice == 2:
#     print("주사위 숫자는 2입니다.")
# elif dice == 3:
#     print("주사위 숫자는 3입니다.")
# elif dice == 4:
#     print("주사위 숫자는 4입니다.")
# elif dice == 5:
#     print("주사위 숫자는 1입니다.")
# elif dice == 6:
#     print("주사위 숫자는 6입니다.")

# 풀이
from random import *
# randint(a, b) 함수는 a부터 b까지의 사이에 있는 정수를 반환해주는 함수
num = randint(1, 6)
print("주사위 눈 : ", num)
# random() 함수는 0.0부터 1.0 미만의 임의의 값을 float 형태로 반환해주는 함수
# num = random()
# print("num : ", num)
# randrange(start, stop, step) 함수는 start에서 stop까지 step dml rkqtdp Ekfktj
# 임의의 수를 반환을 해주는 함수
# num = randrange(0, 101, 2)
# print("num : ", num)
# randrange(a) 함수는 0에서부터 a미만까지의 임의의 정수를 반환하는 함수
# num = randrange(10)
# print("num : ", num)
