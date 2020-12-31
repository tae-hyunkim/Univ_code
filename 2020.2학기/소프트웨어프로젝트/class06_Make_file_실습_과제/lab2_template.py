def solution(lst):
    answer = []
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max_value = max(dic.values())
    if max_value == 1:
        return answer
    else:
        for i, j in dic.items():
            if j == max_value:
                answer.append(i)
    return answer

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]