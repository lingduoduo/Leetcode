from typing import List

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False  
        
        similarPairsSet = set(tuple(pair) for pair in similarPairs)
        for s1, s2 in zip(sentence1, sentence2):
            if s1 != s2 and (s1, s2) not in similarPairsSet and (s2, s1) not in similarPairsSet:
                return False 
        return True 