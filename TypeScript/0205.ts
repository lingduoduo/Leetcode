class Solution {
  isIsomorphic(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const m1 = new Map<string, string>(); // s -> t
    const m2 = new Map<string, string>(); // t -> s

    for (let i = 0; i < s.length; i++) {
      const a = s[i];
      const b = t[i];

      const m1b = m1.get(a);
      const m2a = m2.get(b);

      if ((m1b !== undefined && m1b !== b) || (m2a !== undefined && m2a !== a)) {
        return false;
      }
      m1.set(a, b);
      m2.set(b, a);
    }
    return true;
  }
}
