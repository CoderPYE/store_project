# 터틀 그래픽을 이용하여 사각형 3개를 그려보자. 단 조건은 사각형은 20도씩 기울어져 있다.
import turtle

t = turtle.Pen()

for i in range(10):
    t. left(20)

    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)

# 터틀 그래픽 창이 클릭이 되어야 화면에서 사라지게 하는 코드
turtle.exitonclick()
