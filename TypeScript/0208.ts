class Trie {
    // nested dictionary: each node is an object whose keys are chars
    // and optional '#' marks end of word
    private d: Record<string, any>;

    constructor() {
        this.d = {};
    }

    insert(word: string): void {
        let cur: Record<string, any> = this.d;
        for (const chr of word) {
            if (!(chr in cur)) {
                cur[chr] = {};
            }
            cur = cur[chr];
        }
        cur['#'] = true;  // mark end of word
    }

    private findNode(s: string): Record<string, any> | null {
        let cur: Record<string, any> = this.d;
        for (const chr of s) {
            if (!(chr in cur)) {
                return null;
            }
            cur = cur[chr];
        }
        return cur;
    }

    search(word: string): boolean {
        const node = this.findNode(word);
        return !!(node && node['#']);  // must end exactly at a word
    }

    startsWith(prefix: string): boolean {
        // only need to know the path exists
        return this.findNode(prefix) !== null;
    }
}
