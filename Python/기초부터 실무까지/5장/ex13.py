# 사용자롤부터 임의의 개수의 성적을 입력받아서 합계와 평균을 계산한 후 출력하는 프로그램을 작성해보시오.
# 단, 센티널은 음수의 값을 사용하시오.

# 만들어보기
# i = 0
# sum_score = 0
# avg_score = 0
# while True:
#     score = float(input("성적을 입력하세요(종료는 음수값 입력) : "))
#
#     if score < 0:
#         avg_score = sum_score / i
#         print("종료되었습니다. 점수의 합 = ", sum_score, ", 점수의 평균 = ", avg_score)
#         break
#     else:
#         sum_score += score
#         i += 1

# 풀이
cnt = 0
hap = 0
score = 0
aver = 0
# 센티널(보초값)을 사용자에 제시하는 코드
print("종료하시려면 음수를 입력하세요(예 : -1)")

while score >= 0:
    score = int(input(str(cnt+1) + "번째 학생의 성적을 입력해주세요 : "))
    # 음수 값인지 검사하는 코드
    if score >= 0:
        hap += score    # 성적의 합계를 구하는 코드
        cnt += 1        # 학생의 수를 누적하는 코드
# 합계와 평균을 계산하고 출력하는 코드
if cnt > 0:
    aver = hap / cnt
# 합계와 평균을 출력하는 코드
print(str(cnt+1) + "명의 학생의 합계는 %d입니다." % hap)
print(str(cnt+1) + "명의 학생의 평균은 %.1f입니다." % aver)
