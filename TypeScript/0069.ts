
function mySqrt(x: number): number {
    if (x < 2) return x;

    let left = 1;
    let right = Math.floor(x/2) + 1;
    while (left < right){
        let mid = left + Math.floor((right - left) / 2);
        if (mid ** 2 === x) return mid;
        if (mid ** 2 < x) left = mid + 1;
        else right = mid;

    }
    return left - 1;
};

