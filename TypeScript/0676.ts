class MagicDictionary {
    private trie: Record<string, any>;

    constructor() {
        this.trie = {};
    }

    buildDict(dictionary: string[]): void {
        for (const word of dictionary) {
            let cur = this.trie;
            for (const c of word) {
                if (!(c in cur)) {
                    cur[c] = {};
                }
                cur = cur[c];
            }
            cur["#"] = true;   // end marker
        }
    }

    private dfs(node: any, word: string, index: number, diff: number): boolean {
        // if we've consumed the whole word, valid only if exactly 1 diff and at end marker
        if (index === word.length) {
            return diff === 1 && node["#"] === true;
        }

        const c = word[index];

        for (const ch in node) {
            if (ch === "#") continue;

            if (ch === c) {
                // same char, don't use a diff
                if (this.dfs(node[ch], word, index + 1, diff)) return true;
            } else {
                // different char, we can only spend diff if we haven't yet
                if (diff === 0) {
                    if (this.dfs(node[ch], word, index + 1, 1)) return true;
                }
            }
        }

        return false;
    }

    search(searchWord: string): boolean {
        return this.dfs(this.trie, searchWord, 0, 0);
    }
}
