class Solution {
    get_next(s: string): number[] {
        const next = new Array(s.length).fill(-1);
        let j = -1;
        for (let i = 1; i < s.length; i++) {
            while (j >= 0 && s[i] !== s[j + 1]) j = next[j];
            if (s[i] === s[j + 1]) j++;
            next[i] = j;
        }
        return next;
    }

    strStr(haystack: string, needle: string): number {
        if (needle.length === 0) return 0;

        let j = -1;
        const next_pos = this.get_next(needle);

        for (let i = 0; i < haystack.length; i++) {
            while (j >= 0 && haystack[i] !== needle[j + 1]) j = next_pos[j];
            if (haystack[i] === needle[j + 1]) j++;
            if (j === needle.length - 1) return i - j;
        }
        return -1;
    }
}
