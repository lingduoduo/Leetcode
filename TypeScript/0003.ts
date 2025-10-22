function lengthOfLongestSubstring(s: string): number {
    let res = 0;
    let map = new Map<string, number>();
    let start = 0;

    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (map.has(char) && map.get(char)! >= start) {
            start = map.get(char)! + 1;
        }
        map.set(char, i);
        res = Math.max(res, i - start + 1);
    }
    return res;
};