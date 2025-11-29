function maximalRectangle(matrix: string[][]): number {
    if (!matrix.length || !matrix[0].length) return 0;

    const m = matrix.length;
    const n = matrix[0].length;

    // heights[j] = height of consecutive '1's ending at current row in column j
    const height: number[] = new Array(n).fill(0);
    let res = 0;

    const largestRectangleArea = (heights: number[]): number => {
        const stack: number[] = []; // store indices
        let maxArea = 0;
        const extended = [...heights, 0]; // sentinel

        for (let i = 0; i < extended.length; i++) {
            while (stack.length && extended[i] < extended[stack[stack.length - 1]]) {
                const topIndex = stack.pop()!;
                const h = extended[topIndex];
                const leftIndex = stack.length === 0 ? -1 : stack[stack.length - 1];
                const width = i - leftIndex - 1;  // NOTE: not i - topIndex
                maxArea = Math.max(maxArea, h * width);
            }
            stack.push(i);
        }

        return maxArea;
    };

    for (let i = 0; i < m; i++) {
        // update histogram heights for this row
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] === "1") {
                height[j] += 1;
            } else {
                height[j] = 0;
            }
        }
        // compute largest rectangle in this histogram
        res = Math.max(res, largestRectangleArea(height));
    }

    return res;
}
