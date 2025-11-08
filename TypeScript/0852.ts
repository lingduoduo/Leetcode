function peakIndexInMountainArray(arr: number[]): number {
    let l = 0;
    let r = arr.length;
    while (l < r){
        let m = l + Math.floor((r - l)/2);
        if (arr[m] < arr[m + 1]) l = m + 1;
        else r = m;
    }
    return l;
    
};