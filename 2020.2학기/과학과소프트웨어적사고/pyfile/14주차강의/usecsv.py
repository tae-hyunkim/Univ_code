import csv, os

#
# filename file을 open
# 주의 : opencsv('test.csv') 와 같이 사용
#
def opencsv(filename):
    f = open(filename, "r")
    reader = csv.reader(f)
    output = []

    for i in reader:
        output.append(i)

    return output

#
# filename : 만들고자 하는 file 이름
# the_list : CSV type list를 저장한 객체
#
def writecsv(filename, the_list):

    # open 후 자동으로 file close
    with open(filename, "w", newline = ' ') as f:
        
        tmp = csv.writer(f, delimeter = ",")
        reader = csv.reader(f)

        tmp.writerows(the_list)
