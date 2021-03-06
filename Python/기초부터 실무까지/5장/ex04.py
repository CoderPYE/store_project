# 1에서 100까지 누적값을 구하는데, 누적값이 2000이상이 되면 for문을 빠져 나오는 프로그램을 작성하시오.

# 만들어보기
# Sum = 0
# for x in range(1, 101):
#     Sum += x
#     if Sum >= 2000:
#         print("합계는 : ", Sum)
#         break
#     else:
#         continue

# 풀이
hap = 0
# breakpoint(중단점)는 디버깅(에러를 잡아나가는 과정)에 아주 효율적으로 사용할 수가 있다.(단축키 shift+F9)--매우 중요함
# 한 단계씩 변수의 값이 변화되는 과정으로 살펴보기 위해서는 F7번을 눌러가면서 확인하여 디버깅을 할 수가 있다.
for i in range(101):
    # 2000 이상이면 for 루프를 빠져나오는 코드
    if hap >= 2000:
        print("마지막으로 더해지는 i의 값 : ", i-1)
        break
    hap += i

print("hap : ", hap)
