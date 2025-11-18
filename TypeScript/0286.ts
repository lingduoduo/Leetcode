function wallsAndGates(rooms: number[][]): void {
    if (rooms === null || rooms.length === 0) return;
    const r_size = rooms.length;
    const c_size = rooms[0].length;
    const queue: [number, number][] = [];

    for (let r = 0; r < r_size; r++) {
        for (let c = 0; c < c_size; c++) {
            if (rooms[r][c] === 0) {
                queue.push([r, c]);
            }
        }
    }

    const directions = [
        [-1, 0],
        [0, -1],
        [1, 0],
        [0, 1],
    ];

    while (queue.length > 0) {
        const [x, y] = queue.shift()!;
        const distance = rooms[x][y] + 1;

        for (const [dx, dy] of directions) {
            const newX = x + dx;
            const newY = y + dy;

            if (
                newX >= 0 &&
                newX < r_size &&
                newY >= 0 &&
                newY < c_size &&
                rooms[newX][newY] === 2147483647
            ) {
                rooms[newX][newY] = distance;
                queue.push([newX, newY]);
            }
        }
    }
};
