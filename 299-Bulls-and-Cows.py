class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d1 = {}
        d2 = {}
        bull = 0
        cow = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] in d1:
                    d1[secret[i]] += 1
                else:
                    d1[secret[i]] = 1
                    
                if guess[i] in d2:
                    d2[guess[i]] += 1
                else:
                    d2[guess[i]] = 1
        for i in d1:
            if i in d2:
                cow += min(d1[i], d2[i])
        s = ''
        s += str(bull)
        s += 'A'
        s += str(cow)
        s += 'B'
