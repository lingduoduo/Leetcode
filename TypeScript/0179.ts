function largestNumber(nums: number[]): string {
    let array: string[] = nums.map(String);
    array.sort((a, b) => (b.repeat(10).localeCompare(a.repeat(10))));
    if (array[0] === "0") {
        return "0";
    }
    return array.join('');
}