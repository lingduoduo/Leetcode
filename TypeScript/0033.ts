function search(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length;  
    while (left < right){
        let mid = left + Math.floor((right - left) / 2);
        if (nums[mid] === target) return mid;

        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid])
                right = mid;        
            else
                left = mid + 1;     
        } else {
            if (nums[mid] < target && target <= nums[right - 1])
                left = mid + 1;    
            else
                right = mid;       
        } 
    }
    return -1;
};
