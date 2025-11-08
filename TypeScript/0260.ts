function singleNumber(nums: number[]): number[] {
    let diff = 0;
    for (let num of nums){
        diff ^= num;
    }
    diff &= -diff;
    let res1 = 0;
    let res2 = 0;
    for (let num of nums){
        if ((num & diff) === 0) res1 ^= num
        else res2 ^= num
     }
    return [res1, res2].sort((a, b) => a - b)
};