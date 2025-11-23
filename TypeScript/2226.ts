function maximumCandies(candies: number[], k: number): number {
    const canDistribute = (mid: number): boolean => {
        let count = 0;
        for (const candy of candies) {
            count += Math.floor(candy / mid);
        }
        return count >= k;
    };
    
    let left = 1;
    let right = Math.max(...candies) + 1;
    let result = 0;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (canDistribute(mid)) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return result;   
};
