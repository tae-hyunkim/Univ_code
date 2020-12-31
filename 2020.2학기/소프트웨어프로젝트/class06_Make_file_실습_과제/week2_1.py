count = int(input("Enter a Number:"))

for i in range(count+1):
    print('*'*i)
# 개선 사항
[print("*"*i) for i in range(count+1)]