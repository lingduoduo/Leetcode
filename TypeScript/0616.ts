function addBoldTag(s: string, words: string[]): string {
    const n = s.length;
    const bold = new Array<boolean>(n).fill(false);

    for (let word of words) {
        let start = s.indexOf(word);
        while (start !== -1) {
            const end = start + word.length;
            for (let i = start; i < end; i++) {
                bold[i] = true;
            }
            start = s.indexOf(word, start + 1);
        }
    }

    const res: string[] = [];
    let i = 0;
    while (i < n) {
        if (bold[i]) {
            res.push("<b>");
            while (i < n && bold[i]) {
                res.push(s[i]);
                i++;
            }
            res.push("</b>");
        } else {
            res.push(s[i]);
            i++;
        }
    }

    return res.join('');
};

