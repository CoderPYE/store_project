# 학생들의 성적을 처리하는 프로그램을 만들기
# 조건 : 사용자로부터 성적을 입력받아서 리스트에 저장한다.
#       성적의 평균을 구하고 해당 점수가 80점 이상 성적을 받은 학생의 수를 출력하라.
#       학생수는 상수값으로 STUDENT = 5를 이용한다.
# 출력결과
# 성적을 입력하시요 : 10
# 성적을 입력하시요 : 20
# 성적을 입력하시요 : 60
# 성적을 입력하시요 : 70
# 성적을 입력하시요 : 80
# 성적 평균은 48.0입니다.
# 80점 이상 성적을 받은 학생은 1 명입니다.

# 만들어보기(세번째 조건 추가 전)
# score_list = []
# cnt = 0
# student = int(input("성적을 입력받을 학생의 수를 입력하세요 : "))
#
# for i in range(student):
#     score = int(input("성적을 입력하세요 : "))
#     score_list.append(score)
#     if score >= 80:
#         cnt += 1
#
# avg = sum(score_list) / student
# print("성적 평균은 ", avg, "입니다.")
# print("80점 이상 성적을 받은 학생은 ", cnt, " 명 입니다.")

# 만들어보기(세번째 조건 추가 후)
# STUDENT = 5
# score_list = []
# cnt = 0
#
# for i in range(STUDENT):
#     score_list.append(int(input("성적을 입력하세요 : ")))
#     if score_list[i] >= 80:
#         cnt += 1
# avg = sum(score_list) / STUDENT
# print("성적 평균은 ", avg, "입니다.")
# print("80점 이상 성적을 받은 학생은 ", cnt, " 명 입니다.")

# 풀이
STUDENT = 5   # 전역 상수 선언
scores = []   # 학생들의 성적을 저장할 리스트
score_Sum = 0   # 학생들의 성적 합계를 저장할 변수
score_aver = 0.0   # 학생들의 성적 평균을 저장할 변수
cnt_80 = 0      # 80점 이상인 학생 수 합계를 저장할 변수
for i in range(STUDENT):
    score = int(input("성적을 입력하세요 : "))
    scores.append(score)    # 학생들의 성적을 list에 저장함(append() 이용)
    score_Sum += score      # 성적 합계
    # 80점 이상 학생 수 구하기
    if score >= 80:
        cnt_80 += 1
score_aver = score_Sum / len(scores)    # 평균을 구함

print("성적 평균은 ", score_aver, "입니다.")
print("80점 이상 성적을 받은 학생은 ", cnt_80, " 명 입니다.")
