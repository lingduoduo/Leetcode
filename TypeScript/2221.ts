function triangularSum(nums: number[]): number {
    let stack = [...nums];

    while (stack.length > 0) {
        const first = stack.shift()!; // pop(0) equivalent
        let current = first;

        for (let i = 0; i < stack.length; i++) {
            const second = stack.shift()!;
            stack.push((current + second) % 10);
            current = second;
        }

        if (stack.length === 0) {
            return current; // same as returning 'first' after the loop ends
        }
    }
    return 0; // fallback, though this path is never reached
}

// Example
console.log(triangularSum([1, 2, 3, 4, 5]));
