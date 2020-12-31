import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# wc파일에서 받은 값을 하나하나 받아와 dataframe으로 만들고 진행 추후 그림그리기 편하게. 
data = []
i = 0
for line in sys.stdin:
    if i == 1:
        print(line)
        i += 1
    data.append(line.strip().split('\t'))
    

word_df = pd.DataFrame(data,columns=['count','word'])
word_df['count'] = word_df['count'].astype('int64')
word_df['log_count'] = np.log10(word_df['count'])
word_df = word_df.reset_index()
word_df['index'] = word_df['index'] + 1
word_df['log_index'] = np.log10(word_df['index'])

plt.plot(word_df['log_index'], word_df['log_count'])
plt.yticks([4,5,6,7],['$10^{4}$','$10^{5}$','$10^{6}$','$10^{7}$'])
plt.xticks([0,1,2,3],['$10^{0}$','$10^{1}$','$10^{2}$','$10^{3}$'])
plt.savefig('h01_김태현_20152640_plot.png')


slope = (word_df.loc[0,'log_count'] - word_df.loc[999,'log_count'] )/(word_df.loc[0,'log_index'] - word_df.loc[999,'log_index'] )
intercept = word_df.loc[0,'log_count'] + slope * word_df.loc[0,'log_index']

c = 10**intercept
s = (intercept - word_df.loc[999,'log_count'])/np.log10(999)

print("C의 값은 약:")
print(sys.stdout.write(str(c)))
print("S 의 값은 약: ")
print( sys.stdout.write(str(s)))
