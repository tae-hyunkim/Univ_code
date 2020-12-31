number = ['one','two','three','four','five']

for i in number:
    if i == 'one': # continue는 다음 루프로 넘어가라는 의미 
        continue
    elif i == 'two': # next는 다음에 존재하는 구문으로 넘어가라는 의미
        next 
    elif i == 'four': # break는 반복문을 끝내라는 의미 
        break
    print("Number is ", i)
