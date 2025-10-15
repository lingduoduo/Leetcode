function longestPalindrome(s: string): number {
  const extra = new Set<string>();

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    if (extra.has(ch)) extra.delete(ch);
    else extra.add(ch);
  }

  // If no odd counts, use all chars; otherwise use all but (extra.size - 1) and place one odd in the center
  return extra.size === 0 ? s.length : s.length - extra.size + 1;
}
