# mutable object 중 dictionary라는 타입이 있다.
# 딕셔너리라는 타입의 형태는 키와 값의 쌍으로 이루어져있다.
# 딕셔너리의 키의 값은 유니크한 값이 되어야 한다. 하지만 값은 변경이 가능하다.
# 딕셔너리의 call by reference가 성립되는 이유는 변경가능한 mutable object이기 때문에 가능한 것이다.call by objective-reference라고도 칭한다.

def change(dic):
    print("change()험수 내의 연산전의 dic의 값 : ", dic)
    print("change()험수 내의 연산전의 dic의 주소값 : ", id(dic))
    dic["몸무게"]=42
    print("change()험수 내의 연산후의 dic의 값 : ", dic)
    print("change()험수 내의 연산후의 dic의 주소값 : ", id(dic))

dic = {"name":"김연아", "age":14, "height":160}    # 키:값
# print(dic)
# 키를 주고 값을 얻어온다.
# print(dic["name"])
print("호출전의 dic의 값 : ", dic)
print("호출전의 dic의 주소값 : ", id(dic))
change(dic)
print("호출후의 dic의 값 : ", dic)
print("호출후의 dic의 주소값 : ", id(dic))
