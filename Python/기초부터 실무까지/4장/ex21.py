# 학점을 세부적으로 나누는 프로그램을 작성하기(중첩 if문 사용)
# 조건
# 1. 사용자로부터 점수를 입력받는다.
# 2. 점수가 95점이상 100점 이하라면 A+을 출력한다.
# 3. 점수가 90점이상 94점 이하라면 A0를 출력한다.
# 다른 B, C, D학점도 위와 같이 출력한다.
# 단, F는 그냥 출력하도록 하자.

# 만들어보기
# grade = int(input("점수를 입력하세요 : "))
#
# if grade <= 100:
#     if (grade >= 95) and (grade <= 100):
#         print("A+ 학점입니다.")
#     elif (grade >= 90) and (grade <= 94):
#         print("A0 학점입니다.")
#     elif (grade >= 85) and (grade <= 89):
#         print("B+ 학점입니다.")
#     elif (grade >= 80) and (grade <= 84):
#         print("B0 학점입니다.")
#     elif (grade >= 75) and (grade <= 79):
#         print("C+ 학점입니다.")
#     elif (grade >= 70) and (grade <= 74):
#         print("C0 학점입니다.")
#     elif (grade >= 65) and (grade <= 69):
#         print("D+ 학점입니다.")
#     elif (grade >= 60) and (grade <= 64):
#         print("D0 학점입니다.")
#     else:
#         print("F 학점입니다.")
# else:
#     print("성적의 범위가 잘못되었습니다. 다시 입력하세요.")

# 풀이
score = int(input("점수를 입력하세요 : "))
grade = ""

print("입력한 점수 : ", score)

if score >= 90:
    if score >= 95:
        grade = "A+"
    else:
        grade = "A0"
elif score >= 80:
    if score >= 85:
        grade = "B+"
    else:
        grade = "B0"
elif score >= 70:
    if score >= 75:
        grade = "C+"
    else:
        grade = "C0"
elif score >= 60:
    if score >= 65:
        grade = "D+"
    else:
        grade = "D0"
else:
    grade = "F"

print("당신의 점수는 ", score, "점이며, 학점은 ", grade, "입니다.")
