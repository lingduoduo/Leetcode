class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        
        regex = re.compile('[^a-zA-Z]')
        license = regex.sub('', licensePlate)
        count1 = collections.Counter(license.lower())
        
        def match(counter1, word):
            counter2 = collections.Counter(word)
            counter2.subtract(counter1)
            return all([c >= 0 for c in counter2.values()])
        
        result = ""
        for word in words:
            if match(count1, word):
                if result == '' or len(word) < len(result):
                    result = word
        
        return result
