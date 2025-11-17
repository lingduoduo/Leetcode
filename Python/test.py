import collections

words = ["wrt","wrf","er","ett","rftt"]

graph = collections.defaultdict(set)
chrs = [0] * 26
start = set( )
for w1, w2 in zip(words, words[1:]):
    for chr1, chr2 in zip(w1, w2):
        if chr1 != chr2:
            graph[chr1].add(chr2)
            chrs[ord(chr2) - ord("a")] += 1
            start.add(chr1)

print(graph)
print(chrs)
print(start)