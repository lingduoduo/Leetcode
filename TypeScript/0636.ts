function exclusiveTime(n: number, logs: string[]): number[] {
    const stack: Array<[number, number]> = [];
    const res: number[] = new Array(n).fill(0);

    for (const log of logs) {
        const [idStr, action, timeStr] = log.split(':');
        const id = parseInt(idStr, 10);
        const time = parseInt(timeStr, 10);

        if (action === "start") {
            if (stack.length > 0) {
                res[stack[stack.length - 1][0]] += time - stack[stack.length - 1][1];
            }
            stack.push([id, time]);
        } else {
            const [prevId, startTime] = stack.pop()!;
            const duration = time - startTime + 1;
            res[prevId] += duration;
            if (stack.length > 0) {
                stack[stack.length - 1][1] = time + 1;
            }
        }
    }
    return res
};
