# O(n) time | O(1) space
# where n is the number of coins
def nonConstructibleChange(coins):
    coins.sort()
    amount = 0
    for coin in coins:
        if coin > amount + 1:
            return amount + 1
        amount += coin
    return amount + 1
