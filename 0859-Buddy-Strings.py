class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        
        if A == B:
            s = set()
            for a in A:
                if a in s:
                    return True
                s.add(a)
            return False
        
        A = list(A)
        B = list(B)
        
        first = 0
        while first<len(A) and A[first] == B[first]:
            first += 1
            
        second = first+1
        while second<len(A) and A[second] == B[second]:
            second += 1
        
        if first >= len(A) or second >= len(A):
            return False
            
        A[first], A[second] = A[second], A[first]
        return A==B
        