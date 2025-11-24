// | 状态编号  | 含义                               |
// | ----- | -------------------------------- |
// | **0** | 当天 **持有股票**                      |
// | **1** | 当天 **不持有股票，且今天不是卖出的冷冻期**（正常休息状态） |
// | **2** | 当天 **刚卖出股票**（卖出当天）               |
// | **3** | 当天 **处于冷冻期**（昨天卖出导致今天不能买）        |

function maxProfit(prices: number[]): number {
    const n = prices.length;
    if (n === 0) {
        return 0;
    }

    const dp: number[][] = Array.from({ length: n }, () => Array(4).fill(0));
    dp[0][0] = -prices[0];
    for (let i = 1; i < n; i++) {
        dp[i][0] = Math.max(dp[i - 1][0], Math.max(dp[i - 1][3], dp[i - 1][1]) - prices[i]);
        dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][3]);
        dp[i][2] = dp[i - 1][0] + prices[i];
        dp[i][3] = dp[i - 1][2];
    }
    return Math.max(dp[n - 1][3], dp[n - 1][1], dp[n - 1][2]);
    
};

