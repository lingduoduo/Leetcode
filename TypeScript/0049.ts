function groupAnagrams(strs: string[]): string[][] {
    const res = new Map<string, string[]>();

    for (let i = 0; i < strs.length; i++) {
        const k = new Array(26).fill(0);
        const s = strs[i];

        for (let j = 0; j < s.length; j++) {
            const code = s.charCodeAt(j) - 97; // assuming lowercase a-z
            if (code >= 0 && code < 26) k[code] += 1;
        }

        const key = k.join('#');
        if (!res.has(key)) res.set(key, []);
        res.get(key)!.push(s);
    }

    return Array.from(res.values());
}