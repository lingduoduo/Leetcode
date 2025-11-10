function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    // Always binary-search on the shorter array
    if (nums1.length > nums2.length) {
        let tmp = nums1;
        nums1 = nums2;
        nums2 = tmp;
    }

    const m = nums1.length;
    const n = nums2.length;
    let left = 0;
    let right = m;

    while (left <= right) {
        const midA = Math.floor((left + right) / 2);
        const midB = Math.floor((m + n + 1) / 2) - midA;

        const leftA  = midA === 0 ? -Infinity : nums1[midA - 1];
        const rightA = midA === m ?  Infinity : nums1[midA];

        const leftB  = midB === 0 ? -Infinity : nums2[midB - 1];
        const rightB = midB === n ?  Infinity : nums2[midB];

        if (leftA <= rightB && leftB <= rightA) {
            // Found correct partition
            if ((m + n) % 2 === 0) {
                return (Math.max(leftA, leftB) + Math.min(rightA, rightB)) / 2;
            } else {
                return Math.max(leftA, leftB);
            }
        } else if (leftA > rightB) {
            // Move partition A left
            right = midA - 1;
        } else {
            // Move partition A right
            left = midA + 1;
        }
    }
}
