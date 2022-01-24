# 1st solution
# O(n^2) time | O(n) space
def palindromePartitioningMinCuts(string):
    places = set([0])
    count = 0
    while places:
        level = set()
        if len(string) in places:
            return count - 1
        for startIdx in places:
            for i in range(startIdx, len(string)):
                if isPalindrome(string, startIdx, i):
                    level.add(i + 1)
        count += 1
        places = level
                
def isPalindrome(string, a, b):
    while a < b:
        if string[a] != string[b]:
            return False
        a += 1
        b -= 1
    return True