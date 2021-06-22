def validIPAddresses(string):
    # Write your code here.
    lst = []
    n = len(string)
    for i in range(1, min(n, 4)):
        for j in range(i + 1, i + min(n - i, 4)):
            for k in range(j + 1, j + min(n - j, 4)):
                first = string[:i]
                second = string[i:j]
                third = string[j:k]
                forth = string[k:]
                if check(first) and check(second) and check(third) and check(forth):
                    validIP = first + '.' + second + '.' + third + '.' + forth
                    lst.append(validIP)
    return lst

def check(s):
    num = int(s)
    if num > 255:
        return False
    return len(s) == len(str(num))