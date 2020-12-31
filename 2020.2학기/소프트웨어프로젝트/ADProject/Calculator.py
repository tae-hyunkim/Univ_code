def calcPercent(prevStar):
    # 강화시 성공/파괴될 확률 계산
    percent = 0
    broken = 0
    if prevStar <= 2:
        percent = 95 - 5 * prevStar
    elif prevStar <= 14:
        percent = 100 - 5 * prevStar
        if prevStar == 12:
            broken = 0.6
        elif prevStar == 13:
            broken = 1.3
        elif prevStar == 14:
            broken = 1.4
    elif prevStar <= 21:
        percent = 30
        if prevStar <= 17:
            broken = 2.1
        elif prevStar <= 19:
            broken = 2.8
        else:
            broken = 7
    elif prevStar == 22:
        percent = 3
        broken = 19.4
    elif prevStar == 23:
        percent = 2
        broken = 29.4
    elif prevStar == 24:
        percent = 1
        broken = 39.6
    return [percent, broken]

def calcMeso(prevStar, nowWeaponText):
    # 강화 시도에 사용된 비용을 계산
    useMeso = 0
    weaponLV = int(nowWeaponText)
    if prevStar <= 9:
        useMeso = 1000 + weaponLV**3 * (prevStar + 1) / 25
    elif prevStar <= 14:
        useMeso = 1000 + weaponLV**3 * (prevStar + 1)**2.7 / 400
    else:
        useMeso = 1000 + weaponLV**3 * (prevStar + 1)**2.7 / 200
    useMeso = int((useMeso / 100) * 100)
    return useMeso
