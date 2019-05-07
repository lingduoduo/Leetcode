# Complete the hackerCards function below.
def hackerCards(collection, d):
    num_set = set(collection)
    res = []
    cost = 1
    tot = 0
    while cost + tot <= d:
        if cost not in num_set:
            res.append(cost)
            tot += cost
        cost += 1
    return res


if __name__ == '__main__':
    numbers = [3, 1, 3, 4]
    result = hackerCards(numbers, 7)
    print(result)
    
    numbers = [4, 4, 6, 12, 8]
    result = hackerCards(numbers, 14)
    print(result)
    
    numbers = [4, 1, 2, 3, 4]
    result = hackerCards(numbers, 5)
    print(result)
    
    numbers = []
    result = hackerCards(numbers, 3)
    print(result)
