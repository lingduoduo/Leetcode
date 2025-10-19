function isValidSudoku(board: string[][]): boolean {
  const n = board.length; // 9

  function valid(row: number, col: number, ch: string): boolean {
    // row & column checks (skip the current cell)
    for (let i = 0; i < n; i++) {
      if (i !== col && board[row][i] === ch) return false; // row
      if (i !== row && board[i][col] === ch) return false; // col
    }

    // 3x3 box check (skip the current cell)
    const r0 = Math.floor(row / 3) * 3;
    const c0 = Math.floor(col / 3) * 3;
    for (let i = 0; i < 9; i++) {
      const r = r0 + Math.floor(i / 3);
      const c = c0 + (i % 3);
      if ((r !== row || c !== col) && board[r][c] === ch) return false;
    }
    return true;
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const val = board[i][j];
      if (val === '.') continue;
      if (!valid(i, j, val)) return false;
    }
  }
  return true;
}
