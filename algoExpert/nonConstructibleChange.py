def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()

    curr = 0

    for coin in coins:
        if coin > curr + 1:
            return curr + 1
        curr += coin

    return curr + 1

