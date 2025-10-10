function findBuildings(heights: number[]): number[] {
    let stack: number[] = [];
    stack.push(0);
    for (let i = 1; i < heights.length; i++) {
        while (stack.length && heights[i] >= heights[stack[stack.length - 1]]) {
            stack.pop();
        }
        stack.push(i);
    }
    return stack;
};