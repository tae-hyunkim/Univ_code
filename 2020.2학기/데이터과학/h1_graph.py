
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

lss = []
for line in sys.stdin : 
    i, j = line.split()
    i = int(i)
    lss.append(i)



x = np.log10(range(1,1001))
y = np.log10(lss)

plt.plot(x,y)
plt.xticks(range(0,4),['$10^{0}$','$10^{1}$','$10^{2}$','$10^{3}$'])
plt.yticks(range(5,8),['$10^{5}$','$10^{6}$','$10^{7}$'])
plt.savefig('homework1.png')

Reg = linear_model.LinearRegression()
Reg.fit(np.array(x).reshape(-1, 1),np.array(y).reshape(-1, 1))

c = 10**(Reg.intercept_)
s = Reg.intercept_

# 식으로 나타내면 
# log y = -0.9082972 log x + 6.92765752 
# n = ck^(-s) -> log n = - slogk + logc 이므로 

print("c : {}".format(c), " s : {}".format(s))