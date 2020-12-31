number = ['one','two','three','four','five']

for i in number:
    print(f"Number is {i}")
print( " f 문 사용 ------------------")

for i in number:
    print("Number is {}".format(i))
print("format문 사용 ------------------")

for i in number:
    print("Number is %s 입니다.",i)
print("% 활용 해서 나타내기 ------------")
