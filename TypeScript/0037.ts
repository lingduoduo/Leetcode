function solveSudoku(board: string[][]): void {
  const n = 9;

  function valid(row: number, col: number, num: number, board: string[][]): boolean {
    const ch = String(num);

    // row & column checks
    for (let i = 0; i < n; i++) {
      if (board[row][i] === ch) return false;
      if (board[i][col] === ch) return false;
    }

    // 3x3 box check
    const r0 = Math.floor(row / 3) * 3;
    const c0 = Math.floor(col / 3) * 3;
    for (let i = 0; i < 9; i++) {
      const r = r0 + Math.floor(i / 3);
      const c = c0 + (i % 3);
      if (board[r][c] === ch) return false;
    }

    return true;
  }

  function dfs(): boolean {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (board[i][j] !== ".") continue;      // only fill empty cells

        // try digits 1..9
        for (let k = 1; k <= 9; k++) {
          if (valid(i, j, k, board)) {
            board[i][j] = String(k);
            if (dfs()) return true;             // solved downstream
            board[i][j] = ".";                  // backtrack
          }
        }
        return false;                            // no digit fits here
      }
    }
    return true;                                 // all cells filled
  }

  dfs(); 
}
