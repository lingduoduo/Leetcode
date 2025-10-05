class Solution{
    getNext(s: string){
        let j = -1
        const next: number[] = new Array(s.length).fill(-1);
        for (let i = 1; i < s.length; i++){
            while (j >= 0 && s[i] != s[j + 1]) j = next[j];
            if (s[i] == s[j + 1]) j++;
            next[i] = j;
        }
        return next;
    }
    repeatedSubstringPattern(s: string): boolean {
        const next_pos = this.getNext(s);
        const last = next_pos[next_pos.length - 1];   // index of longest prefix-suffix
        const longest = last + 1;                      // length of that prefix-suffix
        if (last !== -1 && s.length % (s.length - longest) === 0) return true;
        return false;
    }
}