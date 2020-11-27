import math

k = 100

for i in range(1,k+1):
    summ = 0
    for j in range(1,i+1):
        summ += 1/j
    print("조화급수 값: {0:0.5f} \t ln(n+1)값 {1:0.5f} \t 오차율 {2: 0.5f}".format(summ,math.log(i+1),(math.log(i+1)-summ)/summ))
