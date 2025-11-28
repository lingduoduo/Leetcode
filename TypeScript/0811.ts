function subdomainVisits(cpdomains: string[]): string[] {
    const res: Map<string, number> = new Map();

    for (const cp of cpdomains) {
        const [countStr, domain] = cp.split(" ");
        const count = parseInt(countStr, 10);

        const frags = domain.split(".");
        for (let i = 0; i < frags.length; i++) {
            const sub = frags.slice(i).join(".");
            res.set(sub, (res.get(sub) || 0) + count);
        }
    }

    const ans: string[] = [];
    for (const [dom, cnt] of res.entries()) {
        ans.push(`${cnt} ${dom}`);
    }
    return ans;
}
