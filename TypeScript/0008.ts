function myAtoi_likeYours(s: string): number {
    const INT_MIN = -(2 ** 31);
    const INT_MAX = 2 ** 31 - 1;

    s = s.trim();
    if (s.length === 0) return 0;

    let res = 0;
    let sign = 1;
    let i = 0;

    if (s[0] === "-") {
        sign = -1;
        i = 1;
    } else if (s[0] === "+") {
        sign = 1;
        i = 1;
    }

    while (i < s.length && s[i] >= "0" && s[i] <= "9") {
        const digit = s.charCodeAt(i) - "0".charCodeAt(0);
        res = res * 10 + digit;
        i++;
    }

    res *= sign;
    if (res < INT_MIN) return INT_MIN;
    if (res > INT_MAX) return INT_MAX;
    return res;
}
