class Solution {
    reverseStr(s: string, k: number): string {
        let l = 0;
        let r = s.length - 1;
        let c: string;
        let arr = s.split('')
        for (let i = 0, length = arr.length; i < length; i += 2 * k) {
            l = i;
            r = (i + k - 1) >= length ? length - 1 : i + k - 1;
            while (l < r) {
                const temp = arr[l];
                arr[l] = arr[r];
                arr[r] = temp;
                l++;
                r--;
            }
        }
        return arr.join('');
    }
}