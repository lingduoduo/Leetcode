function maxProfit(prices: number[]): number {
    if (prices.length === 0) return 0;
    let minPrice = prices[0];
    let res = 0;

    for (let i = 1; i < prices.length; i++) {
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        } else {
            res = Math.max(res, prices[i] - minPrice);
        }
    }
    return res;
};