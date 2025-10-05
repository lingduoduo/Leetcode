class Solution {
    topKFrequent(nums: number[], k: number): number[] {
        const countMap: Map<number, number> = new Map();
        for (const num of nums) {
            countMap.set(num, (countMap.get(num) ?? 0) + 1);
        }
        return Array.from(countMap.entries())
            .sort((a, b) => b[1] - a[1])
            .slice(0, k)
            .map(([num]) => num);
    }
}
