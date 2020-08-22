'''
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
'''


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        d = dict()
        
        for i in range(len(S)):
            d[S[i]] = i
        
        start = 0
        end = 0
        
        res = []
        for i in range(len(S)):
            end = max(end, d[S[i]])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res

if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    result = Solution().partitionLabels(S)
    print(result)
    
