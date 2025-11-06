function numRescueBoats(people: number[], limit: number): number {
    people.sort((a, b) => a - b);
    let res = 0;
    let left = 0;
    let right = people.length - 1;
    while (left <= right){
        if (people[left] + people[right] <= limit){
            left += 1;
            right -= 1;
        }
        else
            right -= 1;
        res += 1
    }
    return res
};
