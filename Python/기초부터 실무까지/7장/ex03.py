# call by reference에 대한 실습
# 함수를 호출할 떼, 실질적인 주소값이 넘거가서 호출한 곳에 영향을 끼치는 형태가 된다.
# 파이썬에서는 함수의 매개변수 값이 전부 객체인데 list, dictionary와 같은 mutable object
# 즉 변경 가능한 객체이므로 call by objective-reference라고 한다.

def change(li):
    print("change()험수 내의 연산전의 li의 값 : ", li)
    print("change()험수 내의 연산전의 li의 주소값 : ", id(li))
    li += [100, 200]
    print("change()험수 내의 연산후의 li의 값 : ", li)
    print("change()험수 내의 연산후의 li의 주소값 : ", id(li))


list = ["안녕", 1, 3, 1, 1.1]
print("호출전의 list의 값 : ", list)
print("호출전의 list의 주소값 : ", id(list))
change(list)
print("호출후의 list의 값 : ", list)
print("호출후의 list의 주소값 : ", id(list))
