/**
 Do not return anything, modify board in-place instead.
 */
function solve(board: string[][]): void {
    const n = board.length;
    if (n === 0) return;
    const m = board[0].length;

    function dfs(x: number, y: number) {
        if (x < 0 || x >= n || y < 0 || y >= m) return;
        if (board[x][y] !== 'O') return;       // only flood-fill O's
        board[x][y] = '2';                     // mark as safe (connected to border)
        const directions = [[-1, 0], [0, -1], [1, 0], [0, 1]];
        for (const [dx, dy] of directions) {   // iterate pairs correctly
            dfs(x + dx, y + dy);
        }
    }

    // mark all border-connected 'O' as '2'
    for (let r = 0; r < n; r++) {
        if (board[r][0] === 'O') dfs(r, 0);
        if (board[r][m - 1] === 'O') dfs(r, m - 1);
    }
    for (let c = 0; c < m; c++) {
        if (board[0][c] === 'O') dfs(0, c);
        if (board[n - 1][c] === 'O') dfs(n - 1, c);
    }

    // flip remaining 'O' to 'X', and restore '2' back to 'O'
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < m; c++) {
            if (board[r][c] === '2') board[r][c] = 'O';
            else if (board[r][c] === 'O') board[r][c] = 'X';
        }
    }
}
