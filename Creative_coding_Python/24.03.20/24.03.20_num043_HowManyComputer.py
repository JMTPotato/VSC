#컴퓨터 3대로 8시간을 일하면 업무 처리 가능, 근데 단축 근무로 인해 근무 시간 줄어듬.
#근무 시간을 입력하면 필요한 컴퓨터 수량을 파악하는 프로그램 작성

# 3 * 8 = computer * time
# computer = 3 * 8 / time

time = int(input('근무 시간을 입력하세요. '))

computer = 3 * 8 // time    # /아니고 //인거 기억하기
addComputer = 1 if (3 * 8 % time) > 0 else 0

print('필요한 컴퓨터 : ', computer + addComputer)