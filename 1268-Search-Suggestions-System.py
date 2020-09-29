class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    	pass

if __name__ == '__main__':
	products = ["mobile","mouse","moneypot","monitor","mousepad"]
	searchWord = "mouse"
	results = Solution().suggestedProducts(products, searchWord)
	print(results)