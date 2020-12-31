import re
import sys
from collections import Counter

words = Counter()
for line in sys.stdin :  
    line = line.lower()
    line = re.sub('\'',' ',re.sub(r' [ ]',' ',re.sub(r'[^a-z\' ]','',line))).split()
    words.update(line)

most1000 = words.most_common()[:1000]

for word, count in most1000 : 
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")