function finalPrices(prices: number[]): number[] {
  const res = [...prices];  // make a copy to avoid mutating input directly
  const stack: number[] = [];

  for (let i = 0; i < prices.length; i++) {
    // While stack not empty and current price <= price at top index
    while (stack.length > 0 && prices[stack[stack.length - 1]] >= prices[i]) {
      const idx = stack.pop()!;
      res[idx] = prices[idx] - prices[i];
    }
    stack.push(i);
  }

  return res;
}
