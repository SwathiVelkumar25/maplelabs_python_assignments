def possible_str(str):
    if len(str)==1:
        return [str]
    x= possible_str(str[1:])
    c= str[0]
    res=[]
    for y in x:
        for i in range(len(y) + 1):
            res.append(y[:i] + c + y[i:])
    return res
print(possible_str('aeiou'))