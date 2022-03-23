# 더블 루프를 이용하여 아래와 같이 출력하는 프로그램을 작성하시오.
# 출력결과
'''
    *
   ***
  *****
 *******
*********
'''

# 만들어보기
# 1. 더블루프 사용
# for i in range(1, 11, 2):
#     for j in range(int((10-i)/2)):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print("")

# 2. format() 이용
# for i in range(1, 11, 2):
#     print("{:^9}".format("*" * i), end="")
#     print("")

# 풀이
# 1. 더블루프 사용
# for i in range(1, 6):
#     # 공백을 찍는 내부 루프
#     for j in range(5-i):
#         print(" ", end="")
#     # 별표를 찍는 부분
#     for j in range(1, i*2):
#         print("*", end="")
#     # 줄바꿈
#     print("")

# 2. format() 이용
print("-----------------------")
# for i in range(1, 11, 2):
#     # 중앙 정렬을 위해서는 ^ 특수문자를 사용하면 된다.
#     print("{:^10}".format("*" * i))

# 더블 루프를 이용하여 아래와 같이 출력하는 프로그램을 작성하시오.
# 출력결과
'''
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''

# 만들어보기
# 1. 더블루프 사용
# for i in range(1, 11, 2):
#     for j in range(int((10-i)/2)):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print("")
# for i in range(9, 0, -2):
#     for j in range(int((10-i)/2)):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print("")

# 풀이
# 1. 더블루프 사용
print("-----------------------")
# 위의 삼각형 부분을 *로 찍는 코드
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")
    for j in range(1, i*2):
        print("*", end="")
    print("")
# 아래의 삼각형 부분을 *로 찍는 코드
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for j in range(10, (i*2)+1, -1):
        print("*", end="")
    print("")
