import collections
def isValidSubsequence(array, sequence):
    # Write your code here.
    d = collections.defaultdict(list)
    for idx, num in enumerate(array):
        d[num].append(idx)
    
    prev = -1
    for idx, num in enumerate(sequence):
        print(d)
        if num in d:
            d[num]=sorted(d[num])
            while len(d[num])>0 and d[num][0] < prev:
                d[num].pop(0)
            if len(d[num]) == 0:
                return False
            elif len(d[num])>1:
                curr = d[num].pop(0)
                prev = curr
            elif len(d[num])==1:
                curr = d[num].pop(0)
                del d[num]
                prev = curr
        else:
            return False
    return True

if __name__ == '__main__':
    array = [5, 1, 22, 25, 6, -1,  8,  10]
    sequence = [1,  6,  -1, 10]
    res = isValidSubsequence(array, sequence)
    print(res)

    array = [1, 1, 1, 1, 1]
    sequence = [1,  1]
    res = isValidSubsequence(array, sequence)
    print(res)    

    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [5, 1, 25, 22, 6, -1, 8, 10]
    res = isValidSubsequence(array, sequence)
    print(res)