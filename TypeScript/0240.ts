function searchMatrix(matrix: number[][], target: number): boolean {
    let m = matrix.length;
    let n = matrix[0].length;
    let i = 0;
    let j = n - 1;
    while (0 <= i && i < m && 0 <= j && j < n){
        if (matrix[i][j] === target) return true;
        else if (matrix[i][j] < target) i += 1;
        else j -= 1
    }
    return false;
};