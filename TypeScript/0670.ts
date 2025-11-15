function maximumSwap(num: number): number {
    let strs = num.toString().split('');
    let d = new Map<number, number>();
    for (let i = 0; i < strs.length; i++) {
        d.set(parseInt(strs[i]), i);
    }
    for (let i = 0; i < strs.length; i++) {
        for (let j = 9; j > parseInt(strs[i]); j--) {
            if (d.has(j) && d.get(j)! > i) {
                let temp = strs[i];
                strs[i] = strs[d.get(j)!];
                strs[d.get(j)!] = temp;
                return parseInt(strs.join(''));
            }
        }
    }
    return num;
};
                         