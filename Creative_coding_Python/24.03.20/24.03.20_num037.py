targetScore = 90
muScore = int(input('점수를 입력하세요. '))

result = '합격' if muScore >= targetScore else '불합격'
print('시험 결과 : ' + result)