function corpFlightBookings(bookings: number[][], n: number): number[] {
    const res = new Array(n).fill(0);

    for (let [first, last, seats] of bookings) {
        res[first - 1] += seats;
        if (last < n) {
            res[last] -= seats;
        }
    }

    for (let i = 1; i < n; i++) {
        res[i] += res[i - 1];
    }

    return res;
}
