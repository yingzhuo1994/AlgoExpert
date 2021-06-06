def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    # 1st solution
    # O(n^2) time | O(1) space
    n = len(fuel)
    for i in range(n):
        miles = fuel[i] * mpg
        j = i
        while True:
            if miles < distances[j]:
                break
            miles -= distances[j]
            j  = (j + 1) % n
            miles += fuel[j] * mpg
            if j == i:
                return i

    # O(n) time | O(1) space
    if sum(fuel) * mpg - sum(distances) < 0:
        return -1
    
    miles, start_index = 0, 0
    
    for i in range(len(fuel)):
        miles += fuel[i] * mpg - distances[i]
        
        if miles < 0:
            start_index = i + 1
            miles = 0
        
    return start_index
    
