def validIPAddresses(string):
    # Write your code here.
    lst = []
    n = len(string)
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
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
    if 0 < num <= 255 and int(s[0]) != 0:
        return True
    elif num == 0 and len(s) == 1:
        return True
    else:
        return False