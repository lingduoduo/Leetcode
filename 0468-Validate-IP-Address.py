class Solution:
    def validIPAddress(self, IP: str) -> str:
        pv4 = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$')
        if pv4.match(IP):
            return "IPv4"
        pv6 = re.compile(r'^(([0-9a-f]{1,4}):){7}([0-9a-f]{1,4})$')
        if pv6.match(IP.lower()):
            return "IPv6"
        return "Neither"

class Solution:
    def validIPAddress(self, IP: str) -> str:
        def isIPv4(IP):
            ip = IP.split('.')
            for s in ip:
                if len(s) == 0 or len(s) > 3:
                    return 'Neither'
                if ((s[0] == '0' and len(s) != 1) or not s.isdigit() or int(s) > 255):
                    return 'Neither'
            return 'IPv4'

        def isIPv6(IP: str) -> str:
            ip = IP.split(':') 
            for s in ip:
                if len(s) == 0 or len(s) > 4:
                    return "Neither"
                for c in s:
                     if c not in '0123456789abcdef':
                        return "Neither"
            return 'IPv6'

        if len(IP.split('.')) == 4:
            return isIPv4(IP)
        elif len(IP.split(':')) == 8:
            return isIPv6(IP.lower())
        return "Neither"