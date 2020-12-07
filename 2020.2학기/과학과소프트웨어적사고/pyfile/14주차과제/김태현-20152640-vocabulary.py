import re 

f = open('vocabulary.txt','r')

word = {}
for line in f.readlines():
    a = line.strip().split('\t')
    word[a[1]] = a[3]
    word[a[6]] = a[8]
f.close()

while True:
    input_value = input('\n검색하고자 하는 단어를 입력해 주세요 : \t')

    if input_value == '그만':
        break 
    if input_value in word:
        print('\n단어 : {} \t 의미 : {} '.format(input_value, word[input_value]))
    elif re.match('[^a-z]',input_value):
        print('\n 영단어를 입력해 주셔야 합니다.')
    else:
        print('\n 단어장에 없는 단어 입니다. ')
