class Solution {
    reverseString(s: string[]): void {
        let l = 0;
        let r = s.length - 1;

        while (l < r) {
            const temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            l++;
            r--;
        }
    }
}