function isPalindrome(s: string): boolean {
    let chrs = [];

    for (let i =0; i < s.length; i++ ){
        let ch = s[i].toLowerCase()
        if ((ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9'))  chrs.push(ch);
    }

    let left = 0;
    let right = chrs.length - 1;
    while (left < right){
        if (chrs[left] !== chrs[right]) return false;
        left++;
        right--;
    }
    return true;
};