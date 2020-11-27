import numpy as np
import matplotlib.pyplot as plt 

data = 55 + 5 * np.random.randn(1000)

num_bins = 10
plt.hist(data,num_bins,density = False)
plt.show()