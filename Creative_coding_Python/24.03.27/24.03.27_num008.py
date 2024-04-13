score = int(input("점수를 입력하시오: "))
grade = ''

if score >= 90:
    grade = 'A'
    
elif score >= 80:
    grade = 'B'    

elif score >= 70:
    grade = 'C'
    
elif score >= 60:
    grade = 'D'

else:
    grade = 'F'
    
print(score, "의 성적은 ", grade, "입니다.")