import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    # 단어 선택에 있어 11글자 이상 되는 단어는 선택하지 않도록 작업 
    def randFromDB(self):
        r = random.randrange(self.count)
        while True:
            if len(self.words[r]) <= 10:
                break
            else:
                r = random.randrange(self.count)
        return self.words[r]

