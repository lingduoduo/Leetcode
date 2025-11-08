function search(nums: number[], target: number): boolean {
    let left = 0;
    let right = nums.length;  
    while (left < right){
        while (left < right - 1 && nums[left] == nums[right - 1])
            left += 1;
        let mid = left + Math.floor((right - left) / 2);
        if (nums[mid] === target) return true;

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
    return false;
};