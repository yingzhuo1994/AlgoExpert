# 1st solution
# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    buildingsWithSunsetViews = []

    if direction == 'WEST':
        idx = 0
        step = 1
    else:
        idx = len(buildings) - 1
        step = -1

    runningMaxHeight = 0
    while 0 <= idx < len(buildings):
        buildingHeight = buildings[idx]

        if buildingHeight > runningMaxHeight:
            buildingsWithSunsetViews.append(idx)
            runningMaxHeight = buildingHeight
        idx += step
    if step < 0:
        return buildingsWithSunsetViews[::-1]
    return buildingsWithSunsetViews

# 2nd solution
# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    candidateBuildings = []

    if direction == 'EAST':
        idx = 0
        step = 1
    else:
        idx = len(buildings) - 1
        step = -1

    while 0 <= idx < len(buildings):
        buildingHeight = buildings[idx]
        
        while len(candidateBuildings) > 0 and buildings[candidateBuildings[-1]] <= buildingHeight:
            candidateBuildings.pop()
        
        candidateBuildings.append(idx)
        idx += step
    
    if step < 0:
        return candidateBuildings[::-1]
    
    return candidateBuildings