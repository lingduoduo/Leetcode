# Tip: You can use the type(element) function to check whether an item

# is a list or an integer.

import  math
def productSum(array):
    # Write your code here.
    
    stack = []
    res = 0

    level = 1
    for num in array:
        if type(num) is list:
            stack.append((level + 1, num))
        else:
            res += level * num

    while stack:
        print(stack)
        level, nums = stack.pop(0)
        for num in nums:
            if type(num) is list:
                stack.append(((level + 1), num))
            else:
                res += math.factorial(level) * num
                print([level, num])
    return res
    


array = [5, 2, [7, -1], 3, [6,  [-13, 8], 4]]
# array = [
#   [
#     [
#       [
#         [5]
#       ]
#     ]
#   ]
# ]
print(productSum(array))