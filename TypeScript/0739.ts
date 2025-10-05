class Solution {
    dailyTemperatures(temperatures: number[]): number[] {
        const res: number[] = new Array(temperatures.length).fill(0);
        const stack: number[] = []; // stack of indices

        for (let i = 0; i < temperatures.length; i++) {
            while (stack.length && temperatures[stack[stack.length - 1]] < temperatures[i]) {
                const idx = stack.pop()!;
                res[idx] = i - idx;
            }
            stack.push(i);
        }
        return res;
    }
};
