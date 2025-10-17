function maxAreaOfIsland(grid: number[][]): number {
  if (grid.length === 0 || grid[0].length === 0) return 0;

  const rows = grid.length;
  const cols = grid[0].length;
  const dirs = [[-1,0], [1,0], [0,-1], [0,1]];

  let cnt = 0;
  function dfs(row: number, col: number): void {
    // bounds or water check
    if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] === 0) return;

    // mark visited
    grid[row][col] = 0;
    cnt++;

    // 4-directional neighbors (no diagonals)
    for (let i = 0; i < dirs.length; i++) {
      const dx = dirs[i][0];
      const dy = dirs[i][1];
      dfs(row + dx, col + dy);
    }
  }

  let res = 0;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === 1) {
        cnt = 0;
        dfs(i, j);
        res = Math.max(res, cnt);
      }
    }
  }
  return res;
}
