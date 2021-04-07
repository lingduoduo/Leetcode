def tournamentWinner(competitions, results):
    # Write your code here.
    d = {}
    max_k, max_v = "", 0
    for i, competition in enumerate(competitions):
        if results[i] == 0:
            d[competition[1]] = d.get(competition[1], 0) + 1
            if d[competition[1]] > max_v:
                max_k = competition[1]
                max_v = d[competition[1]]
        else:
            d[competition[0]] = d.get(competition[0], 0) + 1
            if d[competition[0]] > max_v:
                max_k = competition[0]
                max_v = d[competition[0]]
    return max_k


competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]

print(tournamentWinner(competitions, results))
