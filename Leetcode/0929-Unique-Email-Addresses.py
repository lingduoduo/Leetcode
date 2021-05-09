import re


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        r = set()
        for email in emails:
            name, domain = email.split('@')
            
            name = re.sub('\.', '', name)
            if name.find('+'):
                s = name.split('+')
                name = s[0]
            
            r.add(name + '@' + domain)
        return len(r)


if __name__ == "__main__":
    s = ["testemail@leetcode.com", "testemail1@leetcode.com", "testemail+david@lee.tcode.com"]
    results = Solution().numUniqueEmails(s)
    print(results)
