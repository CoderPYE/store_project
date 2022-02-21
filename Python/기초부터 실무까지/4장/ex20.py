# 중복(nested) if ~ else 구문
# 사용자로부터 아이디를 입력받아서 등록되어진 아이디인지를 검사하는 프로그램을 작성하는데,
# 등록된 아이디를 리스트(list)에 저장하도록한다.
# 아이디가 등록되어 있다면 패스워드를 물어보도록한다.
# 단, 패스워드는 "1234"라고 가정하도록 한다.

# 만들어보기
# userId = input("아이디를 입력하세요 : ")
# pw = 1234
#
# id_list = ['kim', 'lee', 'park']
#
# if userId in id_list:
#     pw1 = int(input("패스워드를 입력하세요 : "))
#     if pw1 == pw:
#         print("로그인 성공")
#     else:
#         print("비밀번호 오류입니다.")
# else:
#     print("아이디가 일치하지 않습니다. 다시 입력하세요")

# 풀이
# 아이디들의 값들을 리스트에 저장하는 코드
user_list = ["김연아", "손연재", "박길수", "지창욱", "박보검"]
# 패스워드 정의
pw = "1234"

id = input("아이디를 입력하세요 : ")

if id in user_list:    # 사용자가 입력한 id가 user_list에 있는지 확인하는 코드
    password = input("패스워드를 입력하세요 : ")
    if password == pw:    # 중첩 if문
        print(id + "님이 로그인하셨습니다.")
    else:
        print("패스워드가 틀렸습니다.")
else:
    print("등록된 아이디가 존재하지 않습니다.")
