sum_of_num_list = []
sum_of_num = 0
count = 0
number = 1


while True:
    num = int(input("n = "))
    print(">> 입력한 n = {}".format(num))
    if 1 <= num and num <= 100:
        print()
        break
    else :
        print(">> 0 ~ 100 사이의 값을 입력하세요")
5

while number <= 100:
    if number % num == 0:
        sum_of_num_list += [number]
        count += 1
        sum_of_num += number
    number += 1

print(">> 0 ~ 100 사이의 11의 배수 리스트 :", end=' ')
for i in sum_of_num_list:
    print(i, end = ' ')
print()
print()

print(">> 1 ~ 100 사이의 {}의 배수의 수 : {}".format(num,count))
print("   1 ~ 100 사이의 모든 {}의 배수의 합 : {}".format(num,sum_of_num))
    
