#정육각형

import turtle
t = turtle.Turtle()
t.shape = ('turtle')
angle = int(input('회전 각도를 입력하세요. '))      #60
legnth = int(input('전지 길이를 입력하세요. '))     #100

t.forward(legnth)
t.left(angle)
t.forward(legnth)
t.left(angle)
t.forward(legnth)
t.left(angle)
t.forward(legnth)
t.left(angle)
t.forward(legnth)
t.left(angle)
t.forward(legnth)