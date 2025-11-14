function minAddToMakeValid(s: string): number {
    let left = 0;
    let res = 0;
    for (let chr of s) {
        if (chr === "(") {
            left += 1;
        } else {
            if (left > 0) {
                left -= 1;
            } else {
                res += 1;
            }
        }
    }
    return res + left;
};