function reconstructQueue(people: number[][]): number[][] {
    people.sort((a, b) => (b[0] - a[0]) || (a[1] - b[1]));

    const res: number[][] = [];
    for (const p of people) {
        res.splice(p[1], 0, p);
    }
    return res;
};