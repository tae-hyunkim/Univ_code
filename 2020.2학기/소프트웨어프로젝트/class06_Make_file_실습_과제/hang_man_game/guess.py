class Guess:

    def __init__(self, word):
        self.numTries = 0
        self.guessedChars = []
        self.secretWord = word
        self.currentStatus = '_'*len(word)

    def display(self):
        
        print("Current:", end = ' ')
        for i in self.currentStatus:
            print(i, end=' ')
        print()
        print("Tries: ", self.numTries)


    def guess(self, character):
        self.guessedChars.append(character)
        count = 0
        for i in range(len(self.currentStatus)):
            if self.secretWord[i] == character:
                self.currentStatus= self.currentStatus[:i]+character+self.currentStatus[i+1:]
                count += 1
        if count == 0:
            self.numTries += 1 
        if self.currentStatus == self.secretWord:
            return True

if __name__ == '__main__':
    Example = Guess('abcd')
    print("abcd 맞추기")
    print("default 추론단어 모음",end = ' ')
    print(Example.guessedChars)
    print("맞춘 단어 모음",Example.currentStatus)
    Example.guess('a')
    print('----a 추론 추가----')
    print("a 추론 후 current 단어 ",Example.currentStatus)
    print("a 추론 후 예측단어모음",end = ' ')
    print(Example.guessedChars)