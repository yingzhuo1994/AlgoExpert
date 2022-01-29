# 1st solution
# O(n) time | O(n) space
def smallestSubstringContaining(bigString, smallString):
    goalDic = {}
    for ch in smallString:
        goalDic[ch] = goalDic.get(ch, 0) + 1
    ans = [0, float("inf")]
    start = 0
    dic = {}
    goalLength = len(smallString)
    curLength = 0
    for i, ch in enumerate(bigString):
        dic[ch] = dic.get(ch, 0)
        if ch in goalDic and dic[ch] < goalDic[ch]:
            curLength += 1
        dic[ch] += 1
        while start < i:
            ch_start = bigString[start]
            if ch_start not in goalDic:
                start += 1
            elif dic[ch_start] > goalDic[ch_start]:
                dic[ch_start] -= 1
                start += 1
            else:
                break
        if curLength == goalLength:
            if i - start < ans[1] - ans[0]:
                ans = [start, i]
    return bigString[ans[0]:ans[1] + 1] if ans[1] != float("inf") else ""
