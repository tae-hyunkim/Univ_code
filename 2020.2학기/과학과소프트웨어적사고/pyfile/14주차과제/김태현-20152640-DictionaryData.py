import pickle

class make_pickle:
    def __init__(self, filename, word):
        self.filename = filename
        self.word = word
    
    def openfile(self):
        f = open(self.filename,'rb')
        self.dic = pickle.load(f)
        print(self.dic)
        f.close
    
    def makefile(self):
        f = open('myDic.dat','wb')
        pickle.dump(self.word,f)
        f.close()

class Main:
    def __init__(self, a):
        self.pickle = make_pickle('myDic.dat',a)
    def makeopen(self):
        self.pickle.makefile()
    def openpickle(self):
        self.pickle.openfile()

word = {'waiver':'권리포기, 면제','tuition':'수업료','insurance':'보험'}
app = Main(word)
app.makeopen()
app.openpickle()