function customSortString(order: string, s: string): string {
    // Count frequencies of characters in s
    const count = new Map<string, number>();
    for (const ch of s) {
        count.set(ch, (count.get(ch) ?? 0) + 1);
    }

    const res: string[] = [];

    // First, append characters that appear in 'order', in that order
    for (const ch of order) {
        const freq = count.get(ch) ?? 0;
        if (freq > 0) {
            res.push(ch.repeat(freq));
            count.delete(ch); // we've used them up
        }
    }

    // Then, append remaining characters (those not in 'order') in any order
    for (const [ch, freq] of count.entries()) {
        res.push(ch.repeat(freq));
    }

    return res.join("");
}
