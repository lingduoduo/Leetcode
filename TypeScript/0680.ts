function validPalindrome(s: string): boolean {
  function check(left: number, right: number, skipped: boolean): boolean {
    while (left < right) {
      if (s[left] === s[right]) {
        left++;
        right--;
      } else {
        if (skipped) return false; // already skipped one, can't skip again
        // try skipping left or skipping right
        return check(left + 1, right, true) || check(left, right - 1, true);
      }
    }
    return true;
  }

  return check(0, s.length - 1, false);
}