import math

print("\n>>에라토스테네스의 체를 활용하여 소수를 출력하는 파일 입니다.")
input_number = int(input('>>탐색할 범위의 값을 입력해 주세요:'))

max_iter = int(math.sqrt(input_number))

number_list = list(range(1,input_number+1))

for i in range(2,max_iter+1):
    if i in number_list:
        for j in range(i+i,input_number+1,i):
            number_list[j-1] = 0

print("\n>>에라토스테네스의 체를 활용하여 얻은 {}값 까지의 소수값은:".format(input_number))
print([i for i in number_list if i > 1 ])
