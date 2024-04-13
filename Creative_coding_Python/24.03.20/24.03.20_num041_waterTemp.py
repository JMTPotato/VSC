data = int(input('수심을 입력하세요. '))
temperature = 20 - (data // 10 * 0.7)   #10m씩 내려갈 때마다 수온이 0.7 감소
print('수은 :', temperature)