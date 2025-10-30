function rotate(matrix: number[][]): void {
    const n = matrix.length;

    // Step 1: Transpose the matrix (swap across the diagonal)
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {  // start from i+1 to avoid double swap
            const tmp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = tmp;
        }
    }

    // Step 2: Reverse each row
    for (let i = 0; i < n; i++) {
        matrix[i].reverse();
    }
}