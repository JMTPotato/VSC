#확인문제 별 찍기
loopCnt = 6 #반복 횟수

for n1 in range(loopCnt):
    for n2 in range(loopCnt - n1 - 1):
        print(' ', end='')
        
    for n3 in range((n1 + 1) * 2 - 1):
        print('*', end='')
        
    print()