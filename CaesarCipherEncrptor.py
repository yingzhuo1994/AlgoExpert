def caesarCipherEncryptor(string, key):
    # Write your code here.
    # start = ord('a')
    # end = ord('z')
    # lst = []
    # for ch in string:
    #     newNum = ord(ch) + key
    #     while newNum > end:
    #         newNum = newNum - end + start - 1
    #     lst.append(chr(newNum))
    # return ''.join(lst)

    # 2nd Solution
    start = ord('a')
    lst = []
    for ch in string:
        num = start + (ord(ch) + key - start) % 26
        lst.append(chr(num))
    return ''.join(lst)

print(caesarCipherEncryptor('z', 1))
