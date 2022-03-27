# 화씨 온도를 사용자로부터 입력을 받고 섭씨 온도로 변환하여 반환하는 함수 FtoC()를 작성하시오.
# 공식 : 섭씨(C) = (5.0 * (화씨(F) - 32)) / 9.0

# 만들어보기
# def FtoC(fah):
#     celsius = 0
#     celsius = (5.0 * (fah - 32)) / 9.0
#     return celsius
#
# fahrenheit = float(input("화씨 온도를 입력하세요 : "))
# print("화씨온도는 ", fahrenheit, "변환된 섭씨 온도는 ", FtoC(fahrenheit))

# 풀이
# 함수 선언 및 구현
# def FtoC(temp_f):
#     temp_c = (5.0 * (temp_f - 32.0)) / 9.0
#     return temp_c
#
# temp_f = float(input("화씨온도를 입력해주세요 : "))
# # 함수 호출
# print("화씨 온도인", temp_f, "를 섭씨 온도로 변환한 값 : ", round(FtoC(temp_f),2))

def main():
    # 함수 호출
    print("화씨 온도인", temp_f, "를 섭씨 온도로 변환한 값 : ", round(FtoC(temp_f),2))

temp_f = float(input("화씨온도를 입력해주세요 : "))


def FtoC(temp_f):
    temp_c = (5.0 * (temp_f - 32.0)) / 9.0
    return temp_c

main()
