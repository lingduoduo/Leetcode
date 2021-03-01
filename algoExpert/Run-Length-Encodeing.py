def runLengthEncoding(string):
    # Write your code here.

    prev = ""
    n = 1
    res = []
    for s in string:
        if s == prev:
            n += 1
        else:
            while n > 9:
                res.append("9" + prev)
                n -= 9
            if n > 0:
                res.append(str(n)+prev)

            prev = s
            n = 1

    if s == prev:
        while n > 9:
            res.append("9" + prev)
            n -= 9

        if n > 0:
            res.append(str(n)+prev)

    return "".join(res[1:])


s = "AAAAAAAAAABBCAA"
res = runLengthEncoding(s)
print(res)

s =  "************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"
res = runLengthEncoding(s)
print(res)