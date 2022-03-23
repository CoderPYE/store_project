# 입력받은 문자열의 모든 공백을 제거한 문자열을 출력하는 프로그램을 작성하시오.

# 만들어보기
# string = input("문자열을 입력하세요 : ")
# new_string = ""
#
# for word in string:
#     if word == " ":
#         word.replace(" ", "")
#     else:
#         new_string += word
#
# print(new_string)

# 풀이
statements = input("원하는 문자열을 입력하세요 : ")
result = ""

for ch in statements:
    if ch != " ":
        result += ch

print("입력한 문자열 : " + statements)
print("공백을 제거한 문자열 : " + result)
