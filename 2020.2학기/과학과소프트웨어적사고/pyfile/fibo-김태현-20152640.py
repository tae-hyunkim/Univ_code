import time

# for loop문을 활용할 때 list에 처음 두개의 값을 삽입한 후 결과를 계속해서 삽입해서 추가하는 방식으로 활용할 예정이다. 
def fibonachi(n):
    if (n==1) or (n==2):
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)

n = 30

start = time.time()
print(n,fibonachi(n))
print("1) Running fibonachi(%d) takes %f"%(n,time.time()-start))

start = time.time()
value_list = [0,1]
for i in range(n-1):
    value = value_list[i] + value_list[i+1]
    value_list.append(value)

print("2) Running fibonachi for loop (%d) takes %f"%(n,time.time()-start))
print("for loop value",value)

# 재귀함수를 사용할 때 반복문을 사용할때와 비교해 보았을 때 많은 시간이 걸린다는 것을 알 수 있다.
# 왜 이러한 일이 발생하는지에 대하여 생각해 보면 함수를 계속해서 무한적으로 호출해야 하기 때문이다.
# 반복문을 사용해서 활용할 경우 한번 계산한 값을 가지고 계속 활용하지만 함수를 호출해서 사용할 경우 같은 함수를 따로 또 연산하기 때문이다. 
