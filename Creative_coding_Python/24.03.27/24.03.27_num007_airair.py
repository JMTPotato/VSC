temp = float(input("온도를 입력하시오: "))
moist = int(input("습도를 입력하시오: "))

if temp >= 27 or moist >= 80:
    print("에어컨을 켭니다.")

else:
    print("에어컨을 켜지 않습니다.")