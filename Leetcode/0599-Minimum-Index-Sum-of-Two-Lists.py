class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = []
        midx = len(list1) + len(list2)

        commons = [word for word in list1 if word in list2]
        for common in commons:
            i = list1.index(common)
            j = list2.index(common)
            if i + j < midx:
                result = [common]
                midx = i + j
            elif i + j == midx:
                result.append(common)
        return result


if __name__ == "__main__":
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]

    results = Solution().findRestaurant(list1, list2)
    print(results)
