function checkInclusion(s1: string, s2: string): boolean {
    const m = s1.length;
    const n = s2.length;

    if (m > n) return false;

    let d1: Record<string, number> = {};
    let d2: Record<string, number> = {};

    // frequency for s1
    for (let i = 0; i < m; i++) {
        d1[s1[i]] = (d1[s1[i]] || 0) + 1;
    }

    // initial window of size m - 1 in s2
    for (let i = 0; i < m - 1; i++) {
        d2[s2[i]] = (d2[s2[i]] || 0) + 1;
    }

    const isEqual = (a: Record<string, number>, b: Record<string, number>): boolean => {
        const keysA = Object.keys(a);
        const keysB = Object.keys(b);
        if (keysA.length !== keysB.length) return false;
        for (const k of keysA) {
            if (a[k] !== b[k]) return false;
        }
        return true;
    };

    // slide window; i is the right index
    for (let i = m - 1; i < n; i++) {
        const rightChar = s2[i];
        d2[rightChar] = (d2[rightChar] || 0) + 1;

        // check current window [i - m + 1, i]
        if (isEqual(d1, d2)) {
            return true;
        }

        // remove leftmost char from window
        const leftIndex = i - m + 1;
        const leftChar = s2[leftIndex];
        d2[leftChar] -= 1;
        if (d2[leftChar] === 0) {
            delete d2[leftChar];
        }
    }

    return false;
}
