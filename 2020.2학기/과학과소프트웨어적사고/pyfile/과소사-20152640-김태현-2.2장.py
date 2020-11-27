x = 10
a = 3
for i in range(1,10):
    bit = x * i
    exp = a * i
    print("%d bit와 10^%d와의 오차율 = %s"%(bit,exp,((2**bit)-10**exp)/10**exp))

print(" bit의 값이 커질수록 오차율이 커진다.")
