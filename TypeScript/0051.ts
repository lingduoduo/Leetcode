function solveNQueens(n: number): string[][] {
  const res: string[][] = [];
  const chessboard: string[] = Array.from({ length: n }, () => ".".repeat(n));

  function valid(row: number, col: number, board: string[]): boolean {
    // same column
    for (let i = 0; i < row; i++) {
      if (board[i][col] === "Q") return false;
    }
    // main diagonal ↖
    for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
      if (board[i][j] === "Q") return false;
    }
    // anti-diagonal ↗
    for (let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
      if (board[i][j] === "Q") return false;
    }
    return true;
  }

  // helper to set a single char in the row string
  function setChar(row: number, col: number, ch: "Q" | ".") {
    chessboard[row] =
      chessboard[row].slice(0, col) + ch + chessboard[row].slice(col + 1);
  }

  function dfs(row: number): void {
    if (row === n) {
      res.push([...chessboard]); // copy current solution
      return;
    }
    for (let col = 0; col < n; col++) {
      if (valid(row, col, chessboard)) {
        setChar(row, col, "Q");
        dfs(row + 1);
        setChar(row, col, ".");
      }
    }
  }

  dfs(0);
  return res;
}
