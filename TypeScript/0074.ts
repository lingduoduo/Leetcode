function searchMatrix(matrix: number[][], target: number): boolean {
    let n = matrix.length;
    let m = matrix[0].length;

    let left =0;
    let right = n * m;

    while (left < right){
        let mid = left + Math.floor((right - left)/2);
        let r = Math.floor(mid / m);
        let c = mid % m;
        if (matrix[r][c] === target) return true;
        if (matrix[r][c] < target) left = mid + 1;
        else right = mid;
    }
    return false;
};

