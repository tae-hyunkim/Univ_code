import time

class Fibonachi_Sequence:
    
    def __init__(self):
        self.value_list = [0,1]

    def fibonachi(self,n):

        if (n == 1) or (n == 2):
            return 1
        else:
            return self.fibonachi(n-1) + self.fibonachi(n-2)

def main():
    n = int(input('>> 구하고자하는 피보나치수의 항을 입력하세요:'))
    fibo1 = Fibonachi_Sequence()
    start = time.time()
    print(fibo1.fibonachi(n))
    print("1) Running fibonachi(%d) takes %f"%(n,time.time()-start))

    start = time.time()
    value_list = [0,1]
    
    for i in range(n-1):
        value = value_list[i] + value_list[i+1]
        value_list.append(value)

    print("2) Running fibonachi for loop (%d) takes %f"%(n,time.time()-start))
    print("for loop value",value)

main()
