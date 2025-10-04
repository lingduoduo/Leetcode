class Solution {
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) return false;

        const freq: number[] = new Array(26).fill(0);
        const pivot = 'a'.charCodeAt(0);

        for (let i = 0; i < s.length; i++) {
            freq[s.charCodeAt(i) - pivot]++;
            freq[t.charCodeAt(i) - pivot]--;
        }
        return freq.every(x => x === 0);
    }
}

// --- tests ---
const sol = new Solution();
console.log(sol.isAnagram("anagram", "nagaram")); // true
console.log(sol.isAnagram("rat", "car"));         // false
console.log(sol.isAnagram("a", "a"));             // true
console.log(sol.isAnagram("abc", "abC"));         // false (case-sensitive)