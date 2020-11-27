import math

'''
sigmoid 식을 풀어서 활용하면 e**x / ( 1 + e**x)이다.
이를 활용하기 위해 e**x 활용하여 구해보자.
'''

# 항의 개수를 10으로 하니 오차가 너무 커서 sigmoid function이 제대로 그려지지 않습니다.
def e_x50(x):
    num = 0
    for i in range(50):
        num = num + x**i/math.factorial(i)
    return num

def e_x(x):
    num = 0
    for i in range(10):
        num = num + x**i/math.factorial(i)
    return num

def sigmoid(x):
    return e_x(x)/(1+e_x(x))

def sigmoid50(x):
    return e_x50(x) / (1+e_x50(x))

lis = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
print(">> -5부터 5까지 정수 입력 결과")
print(">> 항의 갯수 10개일때 : ",end=' ')
print([sigmoid(i) for i in lis])

print("\n>> 항의 갯수 50개일때 : ",end=' ')
print([sigmoid50(i) for i in lis])
