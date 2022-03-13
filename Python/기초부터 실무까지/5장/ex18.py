# 더블 루프를 사용하여 아래와 같이 출력하는 프로그램을 작성하시오.
# 출력결과
'''
*
**
***
****
*****
'''
# 만들어보기
# 1번째 방법(더블 루프)
# for i in range(5):
#     for j in range(i+1):
#         print("*", end="")
#     print("")

# 2번째 방법(format() 함수 이용)
# for i in range(5):
#     print("{:<5}".format("*" * (i+1)), end="")
#     print("")

# 풀이
# 1번째 방법(더블 루프)
# for i in range(5):  # 5행을 만든다.
#     # 처음 루프시는 i가 0이기 때문에 1이 나오므로 별표 1개만 찍게 된다.
#     # 이후는 i값이 증가가 되기 때문에 2번째 루핑할 때는 별표를 2개 찍게 된다.
#     for j in range(i+1):
#         print("*", end="")
#     print("")

# 2번째 방법(format() 함수 이용)
# format 함수는 {} 이용하고 숫자도 같이 이용된다.
# format 함수도 인덱스를 활용하여 해당하는 값들을 출력할 수가 있다.
print("정수값 : {}, string :{}, float : {}".format(10, "안녕하세요", 10.1))
print("정수값 : {0}, string :{1}, float : {2}".format(10, "안녕하세요", 10.1))
print("정수값 : {2}, string :{1}, float : {0}".format(10, "안녕하세요", 10.1))

# format()은 공간확보 및 -으로 채우는 기능도 지원한다.
# 콜론(:)을 기준으로 우측에 > 혹은 < 부등호를 사용해서 방향을 지정해 줄 수가 있다.
# 0을 추가하면 0으로 빈칸을 채워주는 기능도 지원한다.
print("숫자 '{:>5d}'".format(300))
print("숫자 '{:<5d}'".format(300))

# for i in range(5):
#     print("{:<5}".format("*" * (i+1)))

# 더블 루프를 사용하여 아래와 같이 출력하는 프로그램을 작성하시오.
# 출력결과
'''
*****
****
***
**
*
'''
# 만들어보기
# 1번째 더블 루프 방법
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*",end="")
#     print("")

# 2번째 format 함수 방법
# for i in range(5, 0, -1):
#     print("{:<5}".format("*" * i), end="")
#     print("")

# 풀이
# 1번째 더블 루프 방법
print("------------------")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

# 2번째 format 함수 방법
print("------------------")
for i in range(6, 0, -1):
    print("{:<5}".format("*" * (i-1)))
