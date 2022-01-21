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
