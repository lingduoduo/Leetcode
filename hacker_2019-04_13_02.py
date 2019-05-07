#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'order' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. UNWEIGHTED_INTEGER_GRAPH employees
#  2. INTEGER host
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#

## = employees_nodes[0]
# 5 5
# 1 2
# 1 3
# 2 4
# 3 5
# 1 5
# 1

def order(employees_nodes, employees_from, employees_to, host):
    if not employees_from or not employees_to: return []
    # Write your code here
    nodes = len(set(employees_from + employees_to))
    edges = len(employees_from)
    
    res = []
    M = [[0 for _ in range(1 + nodes)] for _ in range(1 + nodes)]
    visited = [0] * len(M[0])
    
    for i in range(edges):
        M[employees_from[i]][employees_to[i]] = 1
        M[employees_to[i]][employees_from[i]] = 1
        
        M[employees_from[i]][employees_from[i]] = 1
        M[employees_to[i]][employees_to[i]] = 1
    
    def dfs(M, curr, res):
        for j in range(len(M)):
            if M[curr][j] == 1 and j not in res:
                res.append(j)
                M[curr][j] = 0
                M[j][curr] = 0
                dfs(M, j, res)
    
    i = host
    cnt = 0
    while cnt < len(M):
        if visited[i] == 0 and M[i][i] == 1:
            res.append(i)
            print(res)
            dfs(M, i, res)
            visited[i] = 1
        cnt += 1
    res.remove(host)
    return res
    
    # print(visited)
    #
    # for i in range(edges):
    #     M[i][j]
    #
    # ## convert the edges to dictionary
    # d = dict()
    # for i in range(edges):
    #     if employees_from[i] in d:
    #         d[employees_from[i]] += [employees_to[i]]
    #     else:
    #         d[employees_from[i]] = [employees_to[i]]
    #     if employees_to[i] in d:
    #         d[employees_to[i]] += [employees_from[i]]
    #     else:
    #         d[employees_to[i]] = [employees_from[i]]
    #
    # ## sorted the dictionary for each key
    # for i in d:
    #     d[i] = sorted(d[i])
    #
    # res = []
    # visited = []
    # visited.append(host)
    # while len(res)<nodes-1:
    #     ## visit each level
    #     while visited:
    #         fromnodes = visited.pop(0)
    #         if fromnodes in d:
    #             tonodes = d[fromnodes]
    #             for j in range(len(tonodes)):
    #                 if tonodes[j] not in res and tonodes[j] != host:
    #                     res.append(tonodes[j])
    #                     visited.append(tonodes[j])
    #         if not visited:
    #             return res
    # return res


if __name__ == '__main__':
    employees_nodes = 5
    employees_from = [1, 1, 2, 3, 1]
    employees_to = [2, 3, 4, 5, 5]
    host = 1
    # employees_nodes = 3
    # employees_from = [1]
    # employees_to = [2]
    # host = 2
    #
    # employees_nodes = 3
    # employees_from = [1,2]
    # employees_to = [2,3]
    # host = 2
    result = order(employees_nodes, employees_from, employees_to, host)
    print(result)
    # for k, v in result:
    #     print(v)
