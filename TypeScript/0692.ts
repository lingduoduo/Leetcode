function topKFrequent(words: string[], k: number): string[] {
    const countMap: Map<string, number> = new Map();

    // Count frequency
    for (const word of words) {
        countMap.set(word, (countMap.get(word) ?? 0) + 1);
    }

    // Sort by frequency (descending), then lexicographically (ascending)
    return Array.from(countMap.entries())
        .sort((a, b) => {
            const freqDiff = b[1] - a[1];
            if (freqDiff !== 0) return freqDiff;
            return a[0].localeCompare(b[0]);
        })
        .slice(0, k)
        .map(([word]) => word);
}
