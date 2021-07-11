# 1st brute-force solution
# O(n^3) time | O(1) space
def longestPalindromicSubstring(string):
    # Write your code here.
    longestPalindrome = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            if isPalindrome(string, i, j) and j - i + 1 > len(longestPalindrome):
                longestPalindrome = string[i:j + 1]
    return longestPalindrome

def isPalindrome(string, start, end):
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

# 2nd solution
# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    pair = [0, 0]
    for i in range(len(string) - 1):
        odd = getLongestPalindromeFrom(string, i, i)
        even = getLongestPalindromeFrom(string, i, i + 1)
        pair = max(pair, odd, even, key = lambda x: x[1] - x[0])
    return string[pair[0]:pair[1] + 1]

def getLongestPalindromeFrom(s, start, end):
    while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
    return [start + 1, end - 1]