function removeDuplicates(s: string, k: number): string {
    let stack: [string, number][] = [['#', 0]];
    for (const c of s) {
        if (stack[stack.length - 1][0] === c) {
            stack[stack.length - 1][1] += 1;
            if (stack[stack.length - 1][1] === k) {
                stack.pop();
            }
        } else {
            stack.push([c, 1]);
        }
    }
    return stack.map(([c, count]) => c.repeat(count)).join('');
};
