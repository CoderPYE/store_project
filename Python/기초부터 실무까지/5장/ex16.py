# 플래그 변수를 사용한 무한 루프 문제
# 1. 증속, 2. 감속, 3. 중지를 출력하고 사용자의 입력을 1, 2, 3받아서
# 증속을 하면 속도를 10씩 증가하고 출력해준다.
# 감속을 하면 속도를 10씩 감소하고 출력해준다.
# 중지를 하면 플래그 변수를 이용하여 무한 루프를 빠져나간다.

# 만들어보기
# flag = True
# speed = 0
#
# print("1. 증속, 2. 감속, 3. 중지")
# while flag:
#     num = int(input("숫자 중 하나를 선택해 입력하세요 : "))
#     # 1. 증속일 때
#     if num == 1:
#         speed += 10
#         print("증속했습니다. 지금 속도는 %d입니다." % speed)
#     # 2. 감속일 때
#     elif num == 2:
#         if speed <= 0:
#            print("지금 속도는 0입니다.")
#         else:
#             speed -= 10
#             print("감속했습니다. 지금 속도는 %d입니다." % speed)
#     # 3. 중지일 때
#     elif num == 3:
#         print("중지했습니다.")
#         flag = False
#     # 1, 2, 3을 제외한 숫자를 입력했을 때
#     else:
#         print("범위에 없는 숫자입니다. 다시 입력하세요.")

# 풀이
run = True
# print(type(run))
speed = 0
keyCord = 0

while run:
    print("----------------------")
    print("1.증속 | 2.감속 | 3.중지")
    print("----------------------")
    keyCord = int(input("선택 : "))

    # 증속일 경우
    if keyCord == 1:
        speed += 10
        print("현재 속도 : ", speed)
    # 감속일 경우
    elif keyCord == 2:
        speed -= 10
        if speed < 0:
            print("속도는 음수일 수가 없습니다. 뒤로 갈까요?")
            speed = 0
        print("현재 속도 : ", speed)
    # 중지일 경우
    elif keyCord == 3:
        run = False
    # 사용자가 잘못 입력했을 경우
    else:
        print("잘못된 입력값입니다.")
print("프로그램 종료.")
