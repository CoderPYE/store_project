# 피보나치 수열을 구하는 프로그램
# 피보나치 수열이란 앞의 2개의 수를 더해서 다음 수를 결정 짓는 수열이다.
# 예) 사용자로부터 13을 입력받고 난뒤 피보나치 수열의 값 : 1 1 2 3 5 8

# 만들어보기
# num = int(input("정수를 입력하세요 : "))
# first = 0
# second = 1
#
# print(second, end=" ")
# for i in range(num+1):
#     fib = first + second
#     if fib == num:
#         break
#     else:
#         print(fib, end=" ")
#         first = second
#         second = fib

# 풀이
n1 = 1
n2 = 1
n3 = 1

fi = int(input("피보나치 수열을 만들 정수를 입력하세요 : "))

for i in range(1, fi):
    if i < 3:
        n3 = 1
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    # 사용자로부터 입력받은 값보다 작은 수만 출력하게끔 하였다.
    if n3 < fi:
        print(n3, end=" ")
