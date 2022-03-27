# 간단한 사칙연산 계산기 만들기

# 만들어보기
# def operation(n1, n2, op):
#     value = 0
#     if op == "+":       # 더하기
#         value = n1 + n2
#     elif op == "-":     # 빼기
#         value = n1 - n2
#     elif op == "*":     # 곱하기
#         value = n1 * n2
#     elif op == "/":     # 나누기
#         value = n1 / n2
#     elif op == "%":     # 나머지
#         value = n1 % n2
#     else:   # 연산자 오류
#         print("연산자 오류. 다시 입력하세요.")
#     return value
#
# num1 = float(input("숫자를 입력하세요 : "))
# num2 = float(input("숫자를 입력하세요 : "))
# oper = input("연산자를 입력하세요(+,-,*,/,%) : ")
#
# print(operation(num1, num2, oper))

# 풀이
# 더하기 함수
def add(x, y):
    return x + y

# 빼기 함수
def substract(x, y):
    return x - y

# 곱하기 함수
def multiply(x, y):
    return x * y

# 나누기 함수
def divide(x, y):
    return round((x / y), 2)

temp = "y"
# 연산자에 의해서 분기를 시킨다.
while True:
    if temp == "n":
        break
    elif temp == "y":
        n1 = float(input("첫 번째 수 입력 : "))
        n2 = float(input("첫 번째 수 입력 : "))
        op = input("원하는 연산을 입력(+, -, *, /) : ")
        if op == "+":
            print(n1, "+", n2, "=", add(n1, n2))
        elif op == "-":
            print(n1, "-", n2, "=", substract(n1, n2))
        elif op == "*":
            print(n1, "*", n2, "=", multiply(n1, n2))
        elif op == "/":
            print(n1, "/", n2, "=", divide(n1, n2))
        else:
            print("잘못된 연산자입니다.")
        temp = input("계산을 계속 하시겠습니까?(y or n) : ")
