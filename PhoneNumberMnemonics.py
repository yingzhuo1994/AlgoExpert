def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    dic = { '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': '0'
          }
    lst = []
    for i, num in enumerate(phoneNumber):
        if not lst:
            for ch in dic[num]:
                lst.append(ch)
        else:
            lst = [s + ch for s in lst for ch in dic[num]]
    return lst
            

