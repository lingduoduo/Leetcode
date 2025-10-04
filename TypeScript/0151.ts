class Solution {
    reverseWords(s: string): string {
        let arr = s.trim().split(/\s+/); // split by one or more spaces
        let l = 0;
        let r = arr.length - 1;

        while (l < r) {
            const tmp = arr[l];
            arr[l] = arr[r];
            arr[r] = tmp;
            l++;
            r--;
        }
        return arr.join(' ');
    }
}
