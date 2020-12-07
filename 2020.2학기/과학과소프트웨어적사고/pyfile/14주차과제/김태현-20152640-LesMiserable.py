import re 
# 모든 단어에 대하여 살펴보면 좋겠지만 너무 많은 시간이 소요될 것이기 때문에 상위 50개 단어만 지프의 법칙 비교해보고자 한다. 
f = open('Les_Miserables-Victor_Hugo.txt','r')

words = f.read().split()

word_count = {}
for word in words:
    # 단어를 소문자료 변경한 후 영어가 아닌 모든 문자 제거하기 위한 코드
    word = re.sub('[^a-z]','',word.strip().lower())

    # 단어 제거 결과 영단어가 하나도 없을 경우 제외하고 word_count 수행하기 위한 코드 
    if word.strip() == '':
        continue

    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

def sort_value(x):
    return x[1]

word_count_value = sorted(word_count.items(),key=sort_value,reverse=True)
max_value = word_count_value[0][1]

i = 1
for key,value in word_count_value:
    print("단어 : {} \t 단어수/최대값 : {:.3f} \t 지프의법칙 : {:.3f} \t 비율차이 : {:.3f}".format(key, value/max_value,1/i, (value/max_value)-(1/i)))
    i += 1
    if i == 50:
        break 

# 지프의 법칙과 실제 단어수/최대값을 보면 비율의 차이가 초반에 존재하지만 뒤로 갈수록 비율 차이가 줄어드는 모습을 볼 수 있다.
# 이는 점차 수렴한다는 사실을 의미하며 데이터가 많으면 이러한 법칙이 더 잘 맞을 것이라 생각된다. 