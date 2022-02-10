# 1st solution
# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    start = ord('a')
    end = ord('z')
    key %= 26
    lst = []
    for ch in string:
        newNum = ord(ch) + key
        while newNum > end:
            newNum = newNum - end + start - 1
        lst.append(chr(newNum))
    return ''.join(lst)

# 2nd Solution
# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    start = ord('a')
    key %= 26
    lst = []
    for ch in string:
        num = start + (ord(ch) + key - start) % 26
        lst.append(chr(num))
    return ''.join(lst)
