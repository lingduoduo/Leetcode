function removeDuplicates(nums: number[]): number {
    let cnt = 1;
    let idx = 0;
    for (let i=1; i < nums.length; i++){
        if (nums[i] != nums[idx]){
            cnt = 1;
            idx++;
            nums[idx] = nums[i];
        } else if (nums[i] === nums[idx] && cnt === 1){
            cnt++;
            idx++;
            nums[idx] = nums[i];
        }
    }
    return idx + 1;
};