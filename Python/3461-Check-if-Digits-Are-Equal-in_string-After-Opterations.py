class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = list(map(int, s))

        while len(digits) > 2:
            digits = list(map(lambda i: (digits[i] + digits[i+1]) % 10, range(len(digits)-1)))

        return digits[0] == digits[1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.hasSameDigits("34789"))  # Example test case
