class Solution {
    removeDuplicates(s: string): string {
        const stack: string[] = [];
        for (let i = 0; i < s.length; i++) {
            const c = s[i];
            if (stack.length && stack[stack.length - 1] === c) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        return stack.join('');
    }
}