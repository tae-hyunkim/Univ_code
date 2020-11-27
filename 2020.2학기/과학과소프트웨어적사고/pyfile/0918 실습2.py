print("삼각형의 세 변의 길이를 입력해 주세요. (단 a<= b<= c)")

a = int(input('변 a의 길이 :'))
b = int(input('변 b의 길이 :'))
c = int(input('변 c의 길이 :'))

length = sorted([a,b,c])
a = length[0]
b = length[1]
c = length[2]

if a^2 + b^2 == c^2:
    print('직각 삼각형')
elif a^2 + b^2 > c^2:
    print("둔각 삼각형")
else:
    print("예각 삼각형")
