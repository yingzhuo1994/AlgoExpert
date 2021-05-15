# def nonConstructibleChange(coins):
#     # Write your code here.
#     coins.sort()
#     amount = 1
#     allvalue = [sum(lst) for lst in allChange(coins)]
#     while True:
#         if amount in allvalue:
#             amount += 1
#         else:
#             return amount
#
# def allChange(coins):
#     if not coins:
#         return [[]]
#     withcoin = [[coins[0]] + elem for elem in allChange(coins[1:])]
#     withoutcoin= allChange(coins[1:])
#     return withcoin + withoutcoin

def nonConstructibleChange(coins):
    coins.sort()
    amount = 0
    for coin in coins:
        if coin > amount + 1:
            return amount + 1
        amount += coin
    return amount + 1


coins = [5, 7, 1, 1, 2, 3, 22]
# for lst in allChange(coins):
    # print(lst)
# print([sum(lst) for lst in allChange(coins)])
print(nonConstructibleChange(coins))
