# 1st solution
# O(br) time | O(br) space
def apartmentHunting(blocks, reqs):
    dp =[]

    for i, block in enumerate(blocks):
        cur = [float("inf")] * len(reqs)
        for k, goal in enumerate(reqs):
            if block[goal]:
                cur[k] = 0
        dp.append(cur)
    
    for i in range(len(dp)):
        cur = dp[i]
        for k in range(len(reqs)):
            if cur[k] == 0:
                for left in reversed(range(i)):
                    if dp[left][k] > dp[left + 1][k] + 1:
                        dp[left][k] = dp[left + 1][k] + 1
                    else:
                        break
                
                for right in range(i + 1, len(dp)):
                    if dp[right][k] > dp[right - 1][k] + 1:
                        dp[right][k] = dp[right - 1][k] + 1
                    else:
                        break

    res = 0
    for i in range(len(dp)):
        cur = dp[i]
        cur.sort(reverse=True)
        # countZero = 0
        # resZero = 0
        # for k in range(len(reqs)):
        #     if cur[k] == 0:
        #         countZero += 1
        #     if dp[res][k] == 0:
        #         resZero += 1
        # if countZero > resZero:
        #     res = i
        #     continue
        
        for k in range(len(reqs)):
            if cur[k] < dp[res][k]:
                res = i
                break
            elif cur[k] == dp[res][k]:
                continue
            else:
                break
    return res

# 2nd solution
# O(b^2*r) time | O(b) space
# where b is the number of blocks and r is the number of requirements
def apartmentHunting(blocks, reqs):
    maxDistancesAtBlocks = [float("-inf") for block in blocks]
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)
    return getIdxAtMinValue(maxDistancesAtBlocks)

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue

def distanceBetween(a, b):
    return abs(a - b)

    
