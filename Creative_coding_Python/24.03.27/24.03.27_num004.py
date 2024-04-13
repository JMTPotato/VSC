num = int(input('양의 점수를 입력하세요. '))

if num > 0:
    print('num : ', num)
    if num % 2 == 0:
        print('num은 짝수')

    else:
        print('num은 홀수')

else:
    print('num은 양수가 아니다.')