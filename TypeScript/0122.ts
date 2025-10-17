function maxProfit(prices: number[]): number {
    let res = 0;
    for (let i= 1; i<prices.length; i++){
        res += Math.max(prices[i] - prices[i-1], 0)
    }
    return res;
};