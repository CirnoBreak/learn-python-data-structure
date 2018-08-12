def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoints = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoints < minCoins:
                minCoins = numCoints
                knownResults[change] = minCoins
    return minCoins

print(recDC([1, 5, 10, 25], 63, [0] * 64))