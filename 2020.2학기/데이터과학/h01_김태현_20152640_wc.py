from collections import Counter
import re
import sys

# 정규표현식을 활용하여 숫자와 여백 특수문자 등 영어와 공백한칸을 제외한 모든 문자 제거
text_counter = Counter(word for line in sys.stdin
                       for word in re.sub('\'',' ',re.sub(r' [ ]*',' ',re.sub(r'[^a-z\' ]','',line.strip().lower()).strip())).split(' '))

for word, count in text_counter.most_common(1000):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")