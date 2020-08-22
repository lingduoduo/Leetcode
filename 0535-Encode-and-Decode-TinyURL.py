import string
import random
import math

full_tiny = {}
tiny_full = {}
letters = string.ascii_letters + string.digits

class Codec:
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        def short_addr:
            res = ""
            for i in range(6):
                tmp = letters[random.randint(0,1000) % 62]
                res += tmp
            return res
        
        if longUrl in full_tiny:
            return "http://tinyurl.com/" + full_tiny[longUrl]
        else:
            suffix = short_addr()
            full_tiny[longUrl] = suffix
            tiny_full[suffix] = longUrl
        return "http://tinyurl.com/" + suffix
    
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.split("/")[-1]
        if shortUrl in tiny_full:
            return tiny_full[shortUrl]
        else:
            return None
        
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
