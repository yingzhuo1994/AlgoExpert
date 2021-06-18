# 1st solution
# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    lst = []
    heightSoFar = 0
    if direction == 'WEST':
        for i, height in enumerate(buildings):
            if height > heightSoFar:
                lst.append(i)
                heightSoFar = height
        return lst
    else:
        for i in reversed(range(len(buildings))):
            height = buildings[i]
            if height > heightSoFar:
                lst.append(i)
                heightSoFar = height
        return lst[::-1]

# 2nd solution
# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    lst = []
    heightSoFar = 0
    if direction == 'WEST':
        idx = 0
        step = 1
    else:
        idx = len(buildings) - 1
        step = -1
    
    while 0 <= idx < len(buildings):
        height = buildings[idx]
        if height > heightSoFar:
            lst.append(idx)
            heightSoFar = height
        idx += step
    if step < 0:
        return lst[::-1]
    return lst