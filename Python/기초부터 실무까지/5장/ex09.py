# 사용자로부터 2개의 정수 값을 입력받고 첫 번째 입력받은 값부터 두 번째 입력 받은 값까지의 범위에서
# 3의 배수이고 4의 배수를 제외하고 출력하는 프로그램을 작성하시오.(3과 4의 공배수를 제외하고 출력)

# 만들어보기
# num1 = int(input("첫번째 정수를 입력하시오 : "))
# num2 = int(input("두번째 정수를 입력하시오 : "))
#
# for i in range(num1, num2+1):
#     if i % 3 == 0 and i % 4 == 0:
#         continue
#     else:
#         print(i, end=" ")

# 풀이
n1 = int(input("첫 번째 수 : "))
n2 = int(input("두 번째 수 : "))

for i in range(n1, n2+1):
    # 3의 배수이면서 4의 배수를 출력에서 제외를 한다.
    if (i % 3) == 0 and (i % 4) == 0:
        continue    # continue는 조건식이 참이면 아래 문장을 실행치 아니하고 for문으로 이동하여 증가를 한다.
    print(i)

