class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ###i = 0
        ###while i*i < x:
        ###	i+=1
        ###if i*i == x:
        ###    return i
        ###else:
        ###    return i-1
        
        ###L = 0
        ###R = x
        ###while L<=R:
        ###	mid = (L+R)//2
        ###	if mid**2 == x:
        ###		return mid
        ###	elif mid**2 > x:
        ###		R = mid-1
        ###	else:
        ###		L = mid+1
        ###return R
        
        ###second Try
        ###L = 0
        ###R = x + 1
        ###while L < R:
        ###    mid = L + (R - L) // 2
        ###    if mid ** 2 <= x:
        ###        L = mid + 1
        ###    else:
        ###        R = mid
        ###return L - 1
        
        if x<2:
            return x
        
        left, right = 1, x//2
        while left <= right:
            mid = left + (right-left)//2
            if (mid ** 2 == x):
                return mid
            elif mid ** 2 < x:
                left = mid+1
            else:
                right = mid-1
        return left-1
                
        