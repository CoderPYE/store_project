# 1부터 사용자가 입력한 수 num까지 더해서 합계를 구하는 프로그램을 for문을 이용해서 작성하시오.

# 만들어보기
# num = int(input("숫자를 입력하세요 : "))
#
# Sum = 0
# for x in range(1, num+1):
#     Sum = Sum + x
#
# print("합계는 : ", Sum)

# 풀이
hap = 0
num = int(input("어디까지 합계를 구하겠습니까? : "))

for i in range(1, num+1):
    hap += i    # 복합대입연산자(값을 누적하거나 차감할 때 사용하는 연산자)

print("1부터 ", num, "까지의 정수의 합계 = ", hap)
