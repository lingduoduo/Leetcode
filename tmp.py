l = [[1,2],[3],[4]]

res = []
for list in l:
    for num in list:
        res.append(num)
print(res)


# Definition for singly-linked list.

# def buildPath(pathdict, word, path):
#     # if len(pathdict[word]) == 0:
#     if word not in pathdict:
#         result.append([word] + path)
#         return

#     for newword in pathdict[word]:
#         # pathdict[word].remove(newword)
#         # print([word]+path)
#         buildPath(pathdict, newword, [word]+ path)

# pathdict = {'hot': ['hit'], 'dot': ['hot'], 'lot': ['hot'], 'dog': ['dot'], 'log': ['lot'], 'cog': ['dog']}
# result = []
# buildPath(pathdict, 'cog', [])
# print(result)
# strings = "()[]{}"
# strings = "([)]"
# strings = "]"
#     strings ="["
#     results = Solution().isValid(strings)
#     print(results)
#
#
# from string import Template
# language = 'Python'
# t = Template('$name is great')
# t.substitute(name=language)

# import numpy as np
#
# nums = np.random.poisson(2.5, 100000)
# prob = sum([1 if num == 5 else 0 for num in nums]) / 100000
# print(prob)

# def sortport(lis):
#     for i in range(len(lis)):
#         for j in range(len(lis)-1-i):
#             if lis[j]>lis[j+1]:
#                 lis[j], lis[j+1] = lis[j+1], lis[j]
#     return lis

# lis = [12, 54, 1, 3, 5]
# print(sortport(lis))

# import os
# names = [d for d in os.listdir('.')]
# print(names)

# if __name__ == "__main__":

# filepath = ".."
# for i in os.listdir(filepath):
#     print(os.path.join(filepath, i))


# def print_python_dir(filepath):
#     for i in os.listdir(filepath):
#         path = os.path.join(filepath, i)
#         if os.path.isdir(path):
#             print_python_dir(path)
#         if path.endswith(".py"):
#             print(path)
# fpath = ".."
# print_python_dir(fpath)


# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass

#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass

#     return False

# print(is_number('a'))

# import calendar

# check_year = calendar.isleap(2019)
# print(check_year)

# print(calendar.month(2019, 6))


# s = "Test.com"
# print(s.isalnum())  # is digit or letter
# print(s.isalpha())  # is letter
# print(s.isdigit())  # is digit
# print(s.islower())  # is lower
# print(s.istitle())  # is title
# print(s.isspace())  # is '\t' or '\n' pr '\r'

# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.title())

# import time
#
#
# def runtime(func):
#     def wrapper(*args, **kvargs):
#         tic = time.time()
#         result = func(*args, **kvargs)
#         toc = time.time()
#         print('{} is called. {}s used'.format(func.__name__, toc - tic))
#         return result
#
#     return (wrapper)
#
#
# @runtime
# def my_sum(*args):
#     s = 0
#     for i in args:
#         s += 1
#
# my_sum(*range(10000))

# from operator import *
#
# def calculator(a, b, k):
#     return {
#         '+': add,
#         '-': sub,
#         '*': mul,
#         '/': truediv,
#         '**': pow
#     }[k](a,b)
#
# print(calculator(1,2, '+'))
# print(calculator(3,4, '**'))

# for i in range(1,10):
#     for j in range(1, i+1):
#         print('{0}*{1}={2}'.format(j, i, i*j), end="\t")
#     print()
#
# from collections.abc import *
#
# def flatten(input_arr, output_arr=None):
#     if output_arr is None:
#         output_arr = []
#     for ele in input_arr:
#         if isinstance(ele, Iterable):
#             flatten(ele, output_arr)
#         else:
#             output_arr.append(ele)
#     return output_arr
#
# res = flatten([[[1,2,3],[4,5]],[6,7]])
# print(res)

# def max_length(*lst):
#     return max(*lst, key=lambda v: len(v))
# res = max_length([1,2,3], [4,5,6,7], [8])
# print(res)
#
# def max_frequency(lst):
#     return max(lst, default=0, key=lambda v: lst.count(v))
# l=[1,3,4,2,4,5,1,1,1,1]
# print(max_frequency(l))

# def max_lists(*lst):
#     return max(max(*lst, key = lambda v: max(v)))
# print(max_lists([1,2,3], [6,7,8,0], [4,5]))

# from collections import Counter
#
# def find_all_duplicates(lst):

#     c = Counter(lst)
#     return list(filter(lambda k:c[k]>1, c))
#
# print(find_all_duplicates([1,2,2,3,4,5,5]))

# def merge_dict(dict1, dict2):
#     return {**dict1, **dict2}
# print(merge_dict({'a':1, 'b':2}, {'c':3, 'd':4}))

# from heapq import nlargest
#
# students=[{'names':'AA', 'score':80, 'height':198},
#           {'names':'BB', 'score':10, 'height':167},
#           {'names':'CC', 'score':90, 'height':179}]
# print(nlargest(2, students, key=lambda x: x['score']))