# 사용자로부터 태어난 연도를 입력받아서 초등학생, 중학생, 고등학생 대학생 분류 중에서
# 어디에 해당하는지를 출력하는 프로그램을 작성해보세요.(현재나이)
# 나이 -> 8~13(초등학생), 14~16(중학생), 17~19(고등학생), 20~27(대학생)
# 이 외의 나이라면 일반인으로 분류하도록한다.

# 만들어보기
# from datetime import *
# current_year = datetime.today().year
# year = int(input("태어난 연도를 입력하세요 : "))
# age = current_year - year + 1
# if age in range(8, 14):
#     print("나이는", age, "살 초등학생입니다.")
# elif age in range(14, 17):
#     print("나이는", age, "살 중학생입니다.")
# elif age in range(17, 20):
#     print("나이는", age, "살 고등학생입니다.")
# elif age in range(20, 28):
#     print("나이는", age, "살 대학생입니다.")
# else:
#     print("나이는", age, "살 일반인입니다.")

# 풀이
birth_year = int(input("태어난 연도를 입력해주세요 : "))
# 나이계산
age = (2022 - birth_year) + 1
print("현재 나이 : ", age)
# 다중 조건문
if (age >= 8) and (age <= 13):
    print("초등학생이시군요.")
elif (age >= 14) and (age <= 16):
    print("중학생이시군요.")
elif (age >= 17) and (age <= 19):
    print("고등학생이시군요.")
elif (age >= 20) and (age <= 27):
    print("대학생이시군요.")
else:
    print("일반인이시군요.")

