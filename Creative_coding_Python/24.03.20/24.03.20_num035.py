#or 연산자

num1 = 10
num2 = 20
num3 = 30

(num1 < num3) or (num2 < num3) #True and True = True
(num1 > num3) or (num2 < num3) #False and True = True
(num1 > num3) or (num2 > num3) #False and False = False

(num1 < num2) or (num2 < num3) or (num3 > num1) #True and True and True = True
(num1 < num2) or (num2 > num3) or (num3 < num1) #True and False and False = True
(num1 > num2) or (num2 > num3) or (num3 < num1) #False and False and False = False

