function minWindow(s: string, t: string): string {
    if (t.length === 0 || s.length === 0) return "";

    let res = "";
    let cur = Infinity; // track current best length as a number

    let start = 0;
    let t_len = t.length; // how many chars we still need
    const t_d: Record<string, number> = {}; // char -> count

    // build frequency map for t
    for (const c of t) {
        t_d[c] = (t_d[c] ?? 0) + 1;
    }

    for (let i = 0; i < s.length; i++) {
        const c = s[i];

        // only update counts if c is relevant (in t)
        if (c in t_d) {
            t_d[c] = t_d[c] - 1;
            if (t_d[c] >= 0) {
                // we used one needed character
                t_len -= 1;
            }
        }

        // shrink from the left while we have all needed chars
        while (t_len === 0) {
            const windowLen = i - start + 1;
            if (windowLen < cur) {
                cur = windowLen;
                res = s.slice(start, i + 1);
            }

            const leftChar = s[start];

            if (leftChar in t_d) {
                t_d[leftChar] = t_d[leftChar] + 1;
                if (t_d[leftChar] > 0) {
                    // window no longer satisfies all counts
                    t_len += 1;
                }
            }
            start += 1;
        }
    }
    return res;
};
