def minimumCharactersForWords(words):
    # Write your code here.
    dic = {}
    for word in words:
        curDic = {}
        for ch in word:
            curDic[ch] = curDic.get(ch, 0) + 1
        for k, v in curDic.items():
            dic[k] = max(dic.get(k, 0), v)
    lst = []
    for k, v in dic.items():
        lst.extend([k] * v)
    return lst
