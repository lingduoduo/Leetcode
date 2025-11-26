function replaceWords(dictionary: string[], sentence: string): string {
    const trie: Record<string, any> = {};

    // Insert function
    function insert(word: string) {
        let cur = trie;
        for (const ch of word) {
            if (!(ch in cur)) cur[ch] = {};
            cur = cur[ch];
        }
        cur["#"] = true; // mark end
    }

    // Build trie
    for (const word of dictionary) {
        insert(word);
    }

    const res: string[] = [];

    // Process each word in the sentence
    for (const word of sentence.split(" ")) {
        let cur = trie;
        const chrs: string[] = [];
        let replaced = false;

        for (const ch of word) {
            if (!(ch in cur)) break;
            chrs.push(ch);
            cur = cur[ch];

            if ("#" in cur) {
                res.push(chrs.join(""));
                replaced = true;
                break;
            }
        }

        if (!replaced) {
            res.push(word);
        }
    }

    return res.join(" ");
}
