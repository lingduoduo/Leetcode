function validateStackSequences(pushed: number[], popped: number[]): boolean {
    const stack: number[] = [];
    let j = 0; 

    for (const num of pushed) {
        stack.push(num);
        while (
            stack.length > 0 &&
            j < popped.length &&
            stack[stack.length - 1] === popped[j]
        ) {
            stack.pop();
            j++;
        }
    }

    return j === popped.length;
}