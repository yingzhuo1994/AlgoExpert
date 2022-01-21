# 1st solution
# O(n^2) time | O(n^2) space
def lineThroughPoints(points):
    if len(points) <= 2:
        return len(points)
    pointsInLine = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            lineParameters = getLineParameters(points[i], points[j])
            A, B, C = lineParameters
            if A < 0:
                A, B, C = -A, -B, -C
            g = gcd(A, gcd(B, C))
            A, B, C = A // g, B // g, C// g
            lineParameters = (A, B, C)
            pointsInLine.setdefault(lineParameters, set())
            pointsInLine[lineParameters].add(i)
            pointsInLine[lineParameters].add(j)
    return max(map(len, pointsInLine.values()))
                
def getLineParameters(pointOne, pointTwo):
    x1, y1 = pointOne
    x2, y2 = pointTwo
    A = y2 - y1
    B = x1 -x2
    C = x2 * y1 - x1 * y2
    return (A, B, C)

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

# 2nd official solution
# O(n^2) time | O(n) space - where n is the number of points
def lineThroughPoints(points):
    maxNumberOfPointsOnLine = 1

    for idx1, p1 in enumerate(points):
        slopes = {}
        for idx2 in range(idx1 + 1, len(points)):
            p2 = points[idx2]
            rise, run = getSlopeOfLineBetweenPoints(p1, p2)
            slopeKey = createHashableKeyForRational(rise, run)
            if slopeKey not in slopes:
                slopes[slopeKey] = 1
            
            slopes[slopeKey] += 1
        
        maxNumberOfPointsOnLine = max(maxNumberOfPointsOnLine, max(slopes.values(), default=0))
    
    return maxNumberOfPointsOnLine

def getSlopeOfLineBetweenPoints(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    slope = [1, 0]

    if p1x != p2x:
        xDiff = p1x - p2x
        yDiff = p1y - p2y
        gcd = getGreatestCommonDivisor(abs(xDiff), abs(yDiff))
        xDiff = xDiff // gcd
        yDiff = yDiff // gcd
        if xDiff < 0:
            xDiff *= -1
            yDiff *= -1
        
        slope = [yDiff, xDiff]
    
    return slope

def createHashableKeyForRational(numerator, denominator):
    return str(numerator) + ":" + str(denominator)

def getGreatestCommonDivisor(num1, num2):
    a = num1
    b = num2
    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        
        a, b = b, a % b        