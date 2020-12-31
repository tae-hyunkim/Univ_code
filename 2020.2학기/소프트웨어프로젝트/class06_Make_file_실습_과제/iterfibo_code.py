import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)
'''
반복문 활용 파보나치 수열을 구하기 위해서 처음 0,1의 값을 가진 수열을 만들고
해당 값들의 index값 활용 리스트를 수정하며 작업을 진행 최종적으로 계속 삽입하는 방식이 아닌
매번 2개의 값을 수정하는 방식을 취하며 리스트 내의 공간도 확보함.
'''
def iterfibo(n):
    if n <= 1:
        return n
    fn = [0,1]
    i = 1 
    while True:
        if i == n:
            break
        fn.append(fn[-1]+ fn[-2])
        fn = [fn[-2], fn[-1]]
        i += 1
    return fn[-1]
    
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break

    ts = time.time()
    iterfibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("iterFibo(%d)=%d, time %.6f" %(nbr, iterfibonumber, ts))

    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
