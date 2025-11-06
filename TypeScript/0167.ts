function twoSum(numbers: number[], target: number): number[] {
    let l = 0;
    let r = numbers.length - 1;
    while (l < r){
        if (numbers[l] + numbers[r] == target) return [l + 1,  r + 1];
        if (numbers[l] + numbers[r] > target) r -= 1;
        else l += 1;
    }
};