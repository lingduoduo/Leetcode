function maxArea(height: number[]): number {
    let res = 0;
    let left = 0;
    let right = height.length - 1;
    while (left < right){
        let h = Math.min(height[left], height[right]);
        res = Math.max(res, h * (right - left));
        if (height[left] < height[right]) left += 1;
        else right -= 1
    }
    return res;
};