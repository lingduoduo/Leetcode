function exist(board: string[][], word: string): boolean {
    const n = board.length;
    if (n === 0) return false;
    const m = board[0].length;

    function dfs(idx: number, r: number, c: number): boolean {
        if (idx === word.length) return true;
        if (r < 0 || r >= n || c < 0 || c >= m || board[r][c] !== word[idx]) return false;

        const curr = board[r][c];
        board[r][c] = '#'; // mark visited

        const paths = [[0, 1], [0, -1], [1, 0], [-1, 0]] as const;
        for (const [dr, dc] of paths) {
            if (dfs(idx + 1, r + dr, c + dc)) {
                board[r][c] = curr; // restore before returning
                return true;
            }
        }

        board[r][c] = curr; // restore if not found
        return false;
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (dfs(0, i, j)) return true;
        }
    }
    return false;
}
