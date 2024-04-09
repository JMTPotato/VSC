#for문과 while문의 차이점
currentTemperature = 30.0
targetTemperature = float(input('희망 온도를 입력하세요: '))

for i in range(1000):
    currentTemperature -= 0.1
    print('현재 온도 :', format(currentTemperature, '.2f'))

    if currentTemperature <= targetTemperature:
        break

print('냉방 기능 종료!')