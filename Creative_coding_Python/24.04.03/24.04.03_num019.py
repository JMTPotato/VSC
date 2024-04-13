#터틀을 이용한 체인 오먕인 원의 고리를 만들기

import turtle
t = turtle.Turtle()
t.shape('turtle')

for i in range(1, 11):
    t.circle(20)
    
    t.up()
    t.goto(i*30, 0)
    t.down()