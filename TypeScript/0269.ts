function alienOrder(words: string[]): string {
    const edge: Map<string, Set<string>> = new Map();
    const inDegree: Map<string, number> = new Map();

    // Initialize all characters in inDegree and edge
    for (const word of words) {
        for (const char of word) {
            if (!inDegree.has(char)) inDegree.set(char, 0);
            if (!edge.has(char)) edge.set(char, new Set());
        }
    }

    // Build graph (edges) and in-degree map
    for (let i = 0; i < words.length - 1; i++) {
        const first = words[i];
        const second = words[i + 1];
        const minLength = Math.min(first.length, second.length);
        let foundDifference = false;

        for (let j = 0; j < minLength; j++) {
            const char1 = first[j];
            const char2 = second[j];

            if (char1 !== char2) {
                const neighbors = edge.get(char1)!;
                if (!neighbors.has(char2)) {
                    neighbors.add(char2);
                    inDegree.set(char2, inDegree.get(char2)! + 1);
                }
                foundDifference = true;
                break;
            }
        }

        // Invalid case: prefix issue (e.g., "abc", "ab")
        if (!foundDifference && second.length < first.length) {
            return "";
        }
    }

    // Topological sort (Kahn's algorithm)
    const res: string[] = [];
    const queue: string[] = [];

    for (const [char, degree] of inDegree.entries()) {
        if (degree === 0) queue.push(char);
    }

    // Use index pointer instead of shift() for O(1) queue operations
    let head = 0;
    while (head < queue.length) {
        const current = queue[head++];
        res.push(current);

        const neighbors = edge.get(current);
        if (!neighbors) continue;

        for (const neighbor of neighbors) {
            const deg = inDegree.get(neighbor)! - 1;
            inDegree.set(neighbor, deg);
            if (deg === 0) {
                queue.push(neighbor);
            }
        }
    }

    if (res.length < inDegree.size) {
        // Cycle detected or incomplete ordering
        return "";
    }

    return res.join("");
}
