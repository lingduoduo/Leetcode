def findContentChilden(x, y):
    result = 0
    x.sort()
    y.sort()
    for i in range(len(x)):
        j = 0
        while j < len(y) and y[j] < x[i]:
            j += 1
        if j < len(y):
            result += 1
    return (result)


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [1, 1]
    print(findContentChilden(a, b))
    
    a = [1, 2, 3]
    b = [1, 2]
    print(findContentChilden(a, b))
