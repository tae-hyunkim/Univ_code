print(">> 찾고자 하는 최대 공약수의 값을 큰 순서대로 입력해 주세요. \n")

first_num = int(input(">> 숫자를 입력해 주세요:"))
second_num = int(input(">> 숫자를 입력해 주세요:"))

print("\n>> 입력받은 숫자는 {}, {} 입니다.".format(first_num,second_num))

while True:
    X = first_num
    first_num = second_num
    second_num = X%first_num
    if second_num == 0:
        break
    
print("\n>> 찾아낸 최대 공약수 값은 {}입니다.".format(first_num))
    
