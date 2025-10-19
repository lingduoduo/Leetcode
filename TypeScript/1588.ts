function sumOddLengthSubarrays(arr: number[]): number {
    let res = 0;

    for (let l = 1; l < arr.length; l+=2){
        for (let i = 0; i <= arr.length - l; i++) {
            res += arr.slice(i, i + l).reduce((a, b) => a + b, 0);
        }
    }
    return res
};