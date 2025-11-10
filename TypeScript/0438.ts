function findAnagrams(s: string, p: string): number[] {
    const m = p.length;
    const n = s.length;
    const res: number[] = [];

    if (m > n) return res;

    let d_s: { [key: string]: number } = {};
    let d_p: { [key: string]: number } = {};

    // build initial window (size m - 1) and pattern count
    for (let i = 0; i < m - 1; i++) {
        d_s[s[i]] = (d_s[s[i]] || 0) + 1;
    }
    for (let i = 0; i < m; i++) {
        d_p[p[i]] = (d_p[p[i]] || 0) + 1;
    }

    const isEqual = (a: { [key: string]: number }, b: { [key: string]: number }): boolean => {
        const keysA = Object.keys(a);
        const keysB = Object.keys(b);
        if (keysA.length !== keysB.length) return false;
        for (const k of keysA) {
            if (a[k] !== b[k]) return false;
        }
        return true;
    };

    // slide the window; i is the right pointer
    for (let i = m - 1; i < n; i++) {
        const rightChar = s[i];
        d_s[rightChar] = (d_s[rightChar] || 0) + 1;

        // check if current window is an anagram
        if (isEqual(d_s, d_p)) {
            res.push(i - m + 1); // start index of window
        }

        // remove leftmost char from window
        const leftChar = s[i - m + 1];
        d_s[leftChar] -= 1;
        if (d_s[leftChar] === 0) {
            delete d_s[leftChar];
        }
    }

    return res;
};
