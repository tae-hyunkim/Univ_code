key = ['Alpha','Beta','Gamma','Delta','Epdilon','Zeta','Eta','Theta','Iota','Kappa','Lambda','Mu',
       'Nu','Xi','Omicron','Pi','Rho','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega']

value = ['알파','베타','감마','델타','앱실론','제타','에타','세타','요타','카파','람다','뮤','뉴','크사이','오미크론',
         '파이','로','시그마','타우','입시론','피','카이','프사이','오메가']

dic = {}
for i, j in zip(key,value):
    dic[i] = j



print('\n>>>stop을 입력하면 종료됩니다.')
while True:
    input_value = input("그리스 문자를 영어로(ex: Gamma, Alpha) 입력해 주세요:").lower().capitalize()
    
    if input_value == 'Stop':
        break
    try:
        print(dic[input_value])
    except:
        print("단어를 잘못 입력 하셨습니다.")
            
        
    
    
