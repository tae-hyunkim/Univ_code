fH = open('c:/Users/hyoun/Documents/GitHub/class-06-tae-hyunkim/class_file/test17.dat', 'r')
lines = fH.readlines()
fH.close()

fH = open('c:/Users/hyoun/Documents/GitHub/class-06-tae-hyunkim/class_file/test17.out', 'w')
for line in lines:
    words = line.split(' ')
    for word in words:
        word = word.strip()
        fH.write(word + '\n')
fH.close()