class Solution {
    generateMatrix(n: number): number[][] {
        const matrix: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

        let startx = 0, starty = 0;   // Starting coordinates
        const j = Math.floor(n / 2);  // Number of layers
        const mid = Math.floor(n / 2); // Center index if n is odd
        let count = 1;                // Counter

        for (let offset = 1; offset <= j; offset++) {
            // Fill top row (left to right)
            for (let i = starty; i < n - offset; i++) {
                matrix[startx][i] = count++;
            }
            // Fill right column (top to bottom)
            for (let i = startx; i < n - offset; i++) {
                matrix[i][n - offset] = count++;
            }
            // Fill bottom row (right to left)
            for (let i = n - offset; i > starty; i--) {
                matrix[n - offset][i] = count++;
            }
            // Fill left column (bottom to top)
            for (let i = n - offset; i > startx; i--) {
                matrix[i][starty] = count++;
            }

            // Move starting point inward
            startx++;
            starty++;
        }

        // If n is odd, fill the center
        if (n % 2 !== 0) {
            matrix[mid][mid] = count;
        }

        return matrix;
    }
}

// ✅ Example usage
const sol = new Solution();
console.log(sol.generateMatrix(3));
// [
//   [1, 2, 3],
//   [8, 9, 4],
//   [7, 6, 5]
// ]

console.log(sol.generateMatrix(4));
// [
//   [1,  2,  3,  4],
//   [12, 13, 14, 5],
//   [11, 16, 15, 6],
//   [10,  9,  8, 7]
// ]
