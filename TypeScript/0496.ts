class Solution{
    nextGreaterElement(nums1: number[], nums2: number[]): number[] {
        const stack: number[] = [];                          // indices in nums2
        const res: number[] = new Array(nums1.length).fill(-1);

        for (let i = 0; i < nums2.length; i++) {
            while (stack.length && nums2[stack[stack.length - 1]] < nums2[i]) {
                const j = stack.pop()!;                      // index in nums2 whose NGE we just found
                const val = nums2[j];
                const idx = nums1.indexOf(val);              // find position in nums1 when needed
                if (idx !== -1) res[idx] = nums2[i];         // store the next greater value
            }
            stack.push(i);
        }
        return res;
    }
}