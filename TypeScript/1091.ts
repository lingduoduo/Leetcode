function shortestPathBinaryMatrix(grid: number[][]): number {
    let m = grid.length, n = grid[0].length;
    if (m === 0 || n === 0) return -1;
    if (grid[0][0] != 0 || grid[m-1][n-1] != 0) return -1;
    
    const directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],          [0, 1],
            [1, -1],  [1, 0], [1, 1]
        ]
        
    function bfs(queue: number[][]): number {
        if (queue.length === 0) return -1;
            
        const new_queue: [number, number][] = [];
        for (let [x, y] of queue){
            if (x === m - 1 && y === n - 1) return grid[x][y];
            for (let [dx, dy] of directions){
                let nx = x + dx, ny = y + dy;
                if (0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] === 0){
                    grid[nx][ny] = grid[x][y] + 1;
                    new_queue.push([nx, ny]);
                }
            }
        }
        return bfs(new_queue)
    }
    grid[0][0] = 1;
    return bfs([[0, 0]])
};
