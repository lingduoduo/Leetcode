class WordDictionary {
    private d: Record<string, any>;

    constructor() {
        this.d = {};
    }

    addWord(word: string): void {
        let cur: Record<string, any> = this.d;

        for (const chr of word) {
            if (!(chr in cur)) {
                cur[chr] = {};
            }
            cur = cur[chr];
        }
        cur['#'] = true;  // mark end of word
    }

    private dfs(cur: Record<string, any>, word: string, i: number): boolean {
        // reached the end of the pattern
        if (i === word.length) {
            return !!cur['#'];
        }

        const ch = word[i];

        // wildcard: try all children
        if (ch === '.') {
            for (const key in cur) {
                if (key === '#') continue; // skip end marker
                if (this.dfs(cur[key], word, i + 1)) {
                    return true;
                }
            }
            return false;
        }

        // normal character: must follow that edge
        if (!(ch in cur)) return false;
        return this.dfs(cur[ch], word, i + 1);
    }

    search(word: string): boolean {
        return this.dfs(this.d, word, 0);
    }
}
