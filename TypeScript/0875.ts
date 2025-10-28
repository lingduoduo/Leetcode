function minEatingSpeed(piles: number[], h: number): number {
    let left= 1;
    let right = Math.max(...piles);
    while (left < right){
        let mid = left + Math.floor((right - left) / 2);
        let hour = 0;
        for (let pile of piles){
            hour += Math.ceil(pile / mid);
        }
        if (hour <= h) right = mid;
        else left = mid + 1;
    }
    return left;
};
