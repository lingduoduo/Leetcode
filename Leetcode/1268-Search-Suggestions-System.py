class Solution:
    def suggestedProducts(self, products, searchWord):
        res = []
        for i in range(1, 1+len(searchWord)):
            tmp = []
            for j in range(len(products)):
                if products[j][:i]==searchWord[:i]:
                    tmp.append(products[j])
            tmp.sort()
            res.append(tmp[:3])
        return res
        

if __name__ == '__main__':
    # products = ["mobile","mouse","moneypot","monitor","mousepad"]
    # searchWord = "mouse"
    # products = ["havana"]
    # searchWord = "havana"
    products = ["bags","baggage","banner","box","cloths"]
    searchWord = "bags"
    results = Solution().suggestedProducts(products, searchWord)
    print(results)