score = int(input('점수를 입력하세요. '))

if score >= 90:         #점수가 90점 이상이면 'A'를 출력
    print('A')     

elif score >= 80 and score < 90:       #점수가 90점 미만 80점 이상이면 'B'를 출력   //else if 아님
    print('B')    

elif score >= 70 and score < 70:       #점수가 80점 미만 70점 이상이면 'C'를 출력
    print('C')   

elif score >= 60 and score < 70:       #점수가 70점 미만 60점 이상이면 'D'를 출력
    print('D')   

else:                   #점수가 60점 미만이면 'F'를 출력
    print('F')      