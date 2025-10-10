function trap(height: number[]): number {
    let stack: number[] = [];
    stack.push(0);
    let res = 0;
    
    for (let i = 1; i < height.length; i++) {
        while (stack.length && height[i] > height[stack[stack.length - 1]]) {
            let mid = stack.pop()!;
            if (stack.length){
                let left = stack[stack.length - 1];
                let right = i;
                let h = Math.min(height[left], height[right]) - height[mid];
                let w = right - left - 1;
                res += h * w;
            }
        }
        stack.push(i)
    }
    return res;
};