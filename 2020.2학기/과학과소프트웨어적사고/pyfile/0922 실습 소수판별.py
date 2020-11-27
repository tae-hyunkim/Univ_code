import math

number = int(input("소수를 판별할 값을 입력해 주세요:"))

i = 2

flag = '소수'
while i <= (int(math.sqrt(number))+1):
    if number % i ==0:
        flag = '소수아님'
        break
    i += 1
print(f'{number} 값은 {flag}입니다.')



        
