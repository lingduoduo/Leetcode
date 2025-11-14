/**
 * // This is the Robot's API interface.
 * class Robot {
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     move(): boolean {}
 *     
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     turnRight(): void {}
 *     turnLeft(): void {}
 *     
 *     // Clean the current cell.
 *     clean(): void {}
 * }
 */

function cleanRoom(robot: Robot): void {
    // directions: 0 = up, 1 = right, 2 = down, 3 = left
    const moves: [number, number][] = [
        [-1, 0], // up
        [0, 1],  // right
        [1, 0],  // down
        [0, -1], // left
    ];

    const cleaned = new Set<string>();

    const goBack = () => {
        // turn around, move one step, turn back to original direction
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    };

    const dfs = (x: number, y: number, direction: number) => {
        cleaned.add(`${x},${y}`);
        robot.clean();

        // Try all 4 directions from the current orientation
        for (let i = 0; i < 4; i++) {
            const newDir = (direction + i) % 4;
            const [dx, dy] = moves[newDir];
            const newX = x + dx;
            const newY = y + dy;

            if (!cleaned.has(`${newX},${newY}`) && robot.move()) {
                // Successfully moved into the new cell
                dfs(newX, newY, newDir);
                // Backtrack to previous cell and orientation
                goBack();
            }

            // Turn right to face the next direction
            robot.turnRight();
        }
    };

    // Start at (0, 0), facing "up" (direction 0)
    dfs(0, 0, 0);
}
