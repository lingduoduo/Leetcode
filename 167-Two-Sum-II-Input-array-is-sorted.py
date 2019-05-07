class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        
        for i in range(len(numbers)):
            g = d.setdefault(numbers[i], list())
            g.append(i)
        
        for num in numbers:
            if target - num in d.keys():
                idx1 = d[num].pop(0) + 1
                idx2 = d[target - num].pop(0) + 1
                return [idx1, idx2]
        return [0]
