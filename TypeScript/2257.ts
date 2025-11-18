function countUnguarded(m: number, n: number, guards: number[][], walls: number[][]): number {
    const UNGUARDED = 0;
    const GUARDED = 1;
    const GUARD = 2;
    const WALL = 3;

    const grid: number[][] = Array.from({ length: m }, () => Array(n).fill(UNGUARDED));

    // Mark guards' positions
    for (const [r, c] of guards) {
        grid[r][c] = GUARD;
    }

    // Mark walls' positions
    for (const [r, c] of walls) {
        grid[r][c] = WALL;
    }

    // Function to mark cells in a direction from a guard
    function markDirection(row: number, col: number, dr: number, dc: number): void {
        let r = row + dr;
        let c = col + dc;

        // Move in a straight line until we hit a wall or another guard or boundary
        while (r >= 0 && r < m && c >= 0 && c < n) {
            if (grid[r][c] === WALL || grid[r][c] === GUARD) {
                break;
            }
            if (grid[r][c] === UNGUARDED) {
                grid[r][c] = GUARDED;
            }
            r += dr;
            c += dc;
        }
    }

    // Mark cells as guarded by traversing from each guard
    for (const [gr, gc] of guards) {
        for (const [dr, dc] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
            markDirection(gr, gc, dr, dc);
        }
    }

    // Count unguarded cells
    let unguardedCount = 0;
    for (const row of grid) {
        for (const cell of row) {
            if (cell === UNGUARDED) {
                unguardedCount++;
            }
        }
    }

    return unguardedCount;
};
