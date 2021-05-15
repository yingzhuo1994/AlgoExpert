def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    oneStart, oneEnd = arrayOne[0], arrayOne[-1]
    twoStart, twoEnd = arrayTwo[0], arrayTwo[-1]
    if oneStart >= twoEnd:
        return [oneStart, twoEnd]
    elif oneEnd <= twoStart:
        return [oneEnd, twoStart]
    else:
        p1 = 0
        p2 = 0
        diff = abs(arrayOne[0] - arrayTwo[0])
        pair = [arrayOne[0], arrayTwo[0]]
        while p1 < len(arrayOne) and p2 < len(arrayTwo):
            a, b = arrayOne[p1], arrayTwo[p2]
            d = abs(a - b)
            if d < diff:
                diff = d
                pair = [a, b]
            if a < b:
                p1 += 1
            elif a > b:
                p2 += 1
            else:
                break
    return pair
