import time
import random

input_num = int(input("\n>>만들고자하는 리스트의 개수를 입력해 주세요:"))

rand_list = [random.randint(0,10000) for i in range(input_num)]

buble_start = time.time()
for i in range(len(rand_list)):
    for j in range(len(rand_list)-1):
        if rand_list[j] > rand_list[j+1]:
            rand_list[j], rand_list[j+1] = rand_list[j+1],rand_list[j]

buble_end = time.time() - buble_start
print("Bubble Sorting Time is {}".format(buble_end))


rand_list = [random.randint(0,10000) for i in range(input_num)]

start = time.time()
rand_list.sort()
end = time.time() - start

print("Running Sorting Time is {}".format(end))
