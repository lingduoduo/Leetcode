function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
  const wordSet = new Set(wordList);
  if (!wordSet.has(endWord)) return 0;

  const queue: [string, number][] = [[beginWord, 1]];

  while (queue.length) {
    const [word, step] = queue.shift()!;
    if (word === endWord) return step; // <- return step!

    for (let i = 0; i < word.length; i++) {
      for (let c = 97; c <= 122; c++) { // 'a'..'z'
        if (word.charCodeAt(i) === c) continue; // optional micro-opt
        const newWord = word.slice(0, i) + String.fromCharCode(c) + word.slice(i + 1);
        if (wordSet.has(newWord)) {
          wordSet.delete(newWord); // mark visited
          queue.push([newWord, step + 1]);
        }
      }
    }
  }
  return 0;
}