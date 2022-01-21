# 1st solution
import collections
def minimumAreaRectangle(points):
    useXtoFindY = collections.defaultdict(list)
    useYtoFindX = collections.defaultdict(list)
    ans = float("inf")

    for x, y in points:
        useXtoFindY[x].append(y)
        useYtoFindX[y].append(x)
    
    for x in useXtoFindY.keys():
        if len(useXtoFindY[x]) < 2:
            continue
        for i in range(len(useXtoFindY[x])):
            y1 = useXtoFindY[x][i]
            if len(useYtoFindX[y1]) < 2:
                continue
            for j in range(i + 1, len(useXtoFindY[x])):
                y2 = useXtoFindY[x][j]
                if len(useYtoFindX[y2]) < 2:
                    continue
                for x2 in useYtoFindX[y1]:
                    if x2 != x and x2 in useYtoFindX[y2]:
                        ans = min(ans, abs(x2 - x) * abs(y1 - y2))
    return ans if ans != float("inf") else 0

# 2nd solution
# O(n^2) time | O(n) space - where n is the number of points
def minimumAreaRectangle(points):
    columns = initializeColumns(points)
    minimumAreaFound = float("inf")
    edgesParallelToYAxis = {}

    sortedColumns = sorted(columns.keys())
    for x in sortedColumns:
        yValuesInCurrentColumn = columns[x]
        yValuesInCurrentColumn.sort()

        for currentIdx, y2 in enumerate(yValuesInCurrentColumn):
            for previousIdx in range(currentIdx):
                y1 = yValuesInCurrentColumn[previousIdx]
                pointString = str(y1) + ":" + str(y2)

                if pointString in edgesParallelToYAxis:
                    currentArea = (x - edgesParallelToYAxis[pointString]) * (y2 - y1)
                    minimumAreaFound = min(minimumAreaFound, currentArea)
                
                edgesParallelToYAxis[pointString] = x
    
    return minimumAreaFound if minimumAreaFound != float("inf") else 0

def initializeColumns(points):
    columns = {}

    for point in points:
        x, y = point
        if x not in columns:
            columns[x] = []
        
        columns[x].append(y)
    
    return columns
