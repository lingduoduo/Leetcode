function largestRectangleArea(heights: number[]): number {
  const nums = [0, ...heights, 0];      // sentinels
  const stack: number[] = [0];          // stack of indices, start with left sentinel
  let res = 0;

  for (let i = 1; i < nums.length; i++) {
    // Pop while current bar is lower than the bar at stack top
    while (stack.length && nums[i] < nums[stack[stack.length - 1]]) {
      const mid = stack.pop()!;
      const h = nums[mid];
      const leftIdx = stack[stack.length-1];
      const w = i - leftIdx - 1;
      res = Math.max(res, h * w);
    }
    stack.push(i);
  }

  return res;
};