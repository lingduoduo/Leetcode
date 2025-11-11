function minMutation(startGene: string, endGene: string, bank: string[]): number {
    const stack: [string, number][] = [[startGene, 0]];
    const seen = new Set<string>();
    seen.add(startGene);

    while (stack.length) {
        const [node, steps] = stack.shift()!;

        if (node === endGene) return steps;

        for (let i = 0; i < node.length; i++) {
            for (const c of "ACGT") {
                const neighbor = node.slice(0, i) + c + node.slice(i + 1);

                if (!seen.has(neighbor) && bank.includes(neighbor)) {
                    seen.add(neighbor);
                    stack.push([neighbor, steps + 1]);
                }
            }
        }
    }

    return -1;
}
