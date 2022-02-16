# 1st solution
# O(4^n * n) time | O(4^n * n) space
# where n is the length of the phone number
def phoneNumberMnemonics(phoneNumber):
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
    lst = ['']
    for i, num in enumerate(phoneNumber):
        lst = [s + ch for s in lst for ch in dic[num]]
    return lst
            
# 2nd solution
# O(4^n * n) time | O(4^n * n) space
# where n is the length of the phone number
def phoneNumberMnemonics(phoneNumber):
    currentMnemonic = ["0"] * len(phoneNumber)
    mnemonicsFound = []
    phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonic, mnemonicsFound)
    return mnemonicsFound

def phoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonic, mnemonicsFound):
    if idx == len(phoneNumber):
        mnemonic = "".join(currentMnemonic)
        mnemonicsFound.append(mnemonic)
    else:
        digit = phoneNumber[idx]
        letters = DIGIT_LETTERS[digit]
        for letter in letters:
            currentMnemonic[idx] = letter
            phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currentMnemonic, mnemonicsFound)

DIGIT_LETTERS = {
    '1': '1',
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