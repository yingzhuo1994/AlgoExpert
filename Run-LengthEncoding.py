def runLengthEncoding(string):
    # Write your code here.
    if not string:
        return []
    lst = []
    count = 1
    ch = string[0]
    i = 1
    while i < len(string):
        if string[i] == ch and count < 9:
            count += 1
        else:
            lst.append(str(count))
            lst.append(ch)
            ch = string[i]
            count = 1
        i += 1
    lst.append(str(count))
    lst.append(ch)
    return ''.join(lst)
