class Solution {
  canConstruct(ransomNote: string, magazine: string): boolean {
    if (ransomNote.length > magazine.length) return false;

    const freq = new Map<string, number>();
    for (const c of magazine) {
      freq.set(c, (freq.get(c) ?? 0) + 1);
    }

    for (const c of ransomNote) {
      const left = (freq.get(c) ?? 0) - 1;
      if (left < 0) return false;
      freq.set(c, left);
    }

    return true;
  }
}
