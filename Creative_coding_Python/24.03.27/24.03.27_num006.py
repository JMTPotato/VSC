age = int(input('나이를 입력하세요. '))

if age < 6:
    fare = 0
    safetybelt = '착용'

else:
    fare = 3000
    safetybelt = '미착용'

print("입장료는", fare, "입니다.")
print("안전벨트는", safetybelt, "합니다.")