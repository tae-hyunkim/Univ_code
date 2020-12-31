import sys
from collections import Counter
cnt_friends = sorted(Counter(int(x)
for line in sys.stdin
    for x in line.split()).items())

for nid, cnt in cnt_friends:
    print(nid, cnt)