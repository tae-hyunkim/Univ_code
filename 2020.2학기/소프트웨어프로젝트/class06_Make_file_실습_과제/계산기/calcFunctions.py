from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'
    
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def RomanTodec(numStr):
    
    romans = [
        ('M',1000), ('CM',900), ('D',500), ( 'CD',400),
         ( 'C',100),  ( 'XC',90),  ( 'L',50),  ( 'XL',40),
          ( 'X',10),   ( 'IX',9),   ( 'V',5),   ( 'IV',4),
           ( 'I',1)
    ]

    key = ['M','D','C','X','L','V','I']
    
    for i in numStr:
        if i not in key:
            print(i)
            return 'Error!'

    result = 0
    for i,j in romans:
        num = 0
        p = numStr.find(i)
        while p >= 0:
            num += j
            numStr = numStr[p+len(i):]
            p = numStr.find(i)
        result += num
    return result

def constantListFunc(key, constantList):
    if key == constantList[0]:
        return '3.141592'
    elif key == constantList[1]:
        return '3E+8'
    elif key == constantList[2]:
        return '340'
    elif key == constantList[3]:
        return '1.5E+8'

def functionListFunction(key,functionList,n):
    if key == functionList[0]:
        return str(factorial(n))
    elif key == functionList[1]:
        return str(decToBin(n))
    elif key == functionList[2]:
        return str(binToDec(n))
    elif key == functionList[3]:
        return str(decToRoman(n))
    elif key == functionList[4]:
        return str(RomanTodec(n))