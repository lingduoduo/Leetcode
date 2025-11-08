function isPerfectSquare(num: number): boolean {
    if (num === 1) return true;

    let left = 1, right = Math.floor(num/2) + 1;
    while (left < right){
        let mid = left + Math.floor((right - left)/2);
        if (mid ** 2 === num) return true;
        if (mid ** 2 < num) left = mid + 1;
        else right = mid;
    }
    return false;
};