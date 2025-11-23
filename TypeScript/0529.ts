function updateBoard(board: string[][], click: number[]): string[][] {
    const [x, y] = click;
    const m = board.length;
    const n = board[0].length;

    const dirs: number[][] = [
        [0, 1], [0, -1], [1, 0], [1, -1],
        [1, 1], [-1, -1], [-1, 0], [-1, 1]
    ];

    // If we click on a mine, game over: mark as 'X'
    if (board[x][y] === "M") {
        board[x][y] = "X";
        return board;
    }

    const dfs = (r: number, c: number): void => {
        // Only expand from unrevealed empty cells
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] !== "E") return;

        // Count adjacent mines
        let count = 0;
        for (const [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                if (board[nr][nc] === "M") {
                    count++;
                }
            }
        }

        if (count > 0) {
            // If there are adjacent mines, show the count
            board[r][c] = count.toString();
        } else {
            // No adjacent mines: mark as 'B' and expand neighbors
            board[r][c] = "B";
            for (const [dr, dc] of dirs) {
                dfs(r + dr, c + dc);
            }
        }
    };

    dfs(x, y);
    return board;
}
