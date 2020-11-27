sum_of_num_list = []
number = 1


while True:
    num = int(input(">> n = "))
    print(">> 입력한 n = {}".format(num))
    print()
    
    if 1 <= num and num <= 100:
        break
    else :
        print(">> 0 ~ 100 사이의 값을 입력하세요")

while number <= 100:
    if number % num == 0:
        sum_of_num_list += [number]
    number += 1

print(">> 0 ~ 100 사이의 11의 배수 리스트 :", end=' ')
for i in sum_of_num_list:
    print(i, end = ' ')
print()
print()

print(">> 1 ~ 100 사이의 {}의 배수의 수 : {}".format(num,len(sum_of_num_list)))
print("   1 ~ 100 사이의 모든 {}의 배수의 합 : {}".format(num,sum(sum_of_num_list)))
    
