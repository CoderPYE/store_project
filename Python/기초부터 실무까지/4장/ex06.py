# 항공사에서는 짐을 부칠 때, 20kg이 넘어가면 20,000원의 추가비용을 내야한다고 하자.
# 20kg 미만이면 수수료는 없다. 사용자로부터 짐의 무게를 입력을 받고
# 사용자가 지불해야하는 금액이 얼마인지 계산하는 프로그램을 작성해보자

# 만들어보기
# weight = int(input("짐의 무게를 입력하세요(kg) : "))
# if weight > 20:
#     print("20,000원의 추가비용이 발생합니다.")
# else:
#     print("추가 비용이 없습니다.")


weight = float(input("짐의 무게를 입력헤세요 : "))

if weight > 20:
    print("짐의 무게가 20kg을 넘었기 때문에 추가비용 20,000원 내셔야 합니다.")
else:
    print("짐에 대한 수수료가 없습니다.")
print("감사합니다. 고객님")
