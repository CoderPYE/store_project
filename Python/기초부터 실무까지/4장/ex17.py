# 사용자로부터 정수를 입력받아서 음수, 0, 양수 중에 어떤 값인지를 출력하는 프로그램

# 만들어보기
# number = int(input("정수를 입력하세요(음수, 0, 양수) : "))
#
# if number > 0:
#     print("양수 입니다.")
# elif number == 0:
#     print("0 입니다.")
# else:
#     print("음수 입니다.")

# 풀이
num = int(input("정수를 입력하시오 : "))
if num > 0:
    print("입력된 정수는 양수입니다.")
elif num == 0:
    print("입력된 정수는 0입니다.")
else:
    print("입력된 정수는 음수입니다.")
