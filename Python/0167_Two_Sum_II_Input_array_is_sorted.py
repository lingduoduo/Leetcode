class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ###d = dict()
        #
        ###for i in range(len(numbers)):
        ###    g = d.setdefault(numbers[i], list())
        ###    g.append(i)
        #
        ###for num in numbers:
        ###    if target - num in d.keys():
        ###        idx1 = d[num].pop(0) + 1
        ###        idx2 = d[target - num].pop(0) + 1
        ###        return [idx1, idx2]
        ###return [0]

        ###second try
        start = 0
        end = len(numbers) - 1
        sum = 0

        while start != end:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start + 1, end + 1]
