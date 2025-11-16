function carPooling(trips: number[][], capacity: number): boolean {
    const timestamp: Array<[number, number]> = [];

    for (const trip of trips) {
        const numPassengers = trip[0];
        const start = trip[1];
        const end = trip[2];

        // +num at start, -num at end
        timestamp.push([start, numPassengers]);
        timestamp.push([end, -numPassengers]);
    }

    // Sort by time; if time is equal, process dropoffs (-) before pickups (+)
    timestamp.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return a[1] - b[1]; // negative first, then positive
    });

    let used_capacity = 0;
    for (const [, passenger_change] of timestamp) {
        used_capacity += passenger_change;
        if (used_capacity > capacity) {
            return false;
        }
    }
    return true;
}

