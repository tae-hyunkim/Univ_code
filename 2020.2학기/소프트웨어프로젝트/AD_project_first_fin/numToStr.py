def norToAbnor(nor):              # "1000000" 형태를 "1,000,000" 형태로
    abnor = nor[0:len(nor)%3] + ","
    if abnor == ",":
        abnor = ""
    for i in range(len(nor)//3):
        abnor += nor[len(nor) % 3 + 3 * i : len(nor) % 3 + 3 * (i + 1)] + ","
    abnor = abnor[0:len(abnor) - 1]
    return abnor

def abnorToNor(abnor):            # "1,000,000" 형태를 "1000000" 형태로
    nor = ""
    for i in range(len(abnor)):
        if abnor[i] != ",":
            nor += abnor[i]
    return nor
