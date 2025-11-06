function singleNumber(nums: number[]): number {
  const uniqueSum = Array.from(new Set(nums)).reduce((a, b) => a + b, 0);
  const totalSum = nums.reduce((a, b) => a + b, 0);
  return (3 * uniqueSum - totalSum) / 2;
}
