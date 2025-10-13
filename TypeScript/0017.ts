function letterCombinations(digits: string): string[] {
    if (!digits) return [];

    let res: string[] = [];
    const d: Record<string, string> = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    };

    function dfs(idx, path){
        if (path.length == digits.length){
            res.push(path.join(''));
            return
        }

        const letters = d[digits[idx]];
        for (let j = 0 ; j < letters.length; j++){
            path.push(letters[j]);
            dfs(idx + 1, path);
            path.pop();
        }
    }

    dfs(0, [])
    return res
};