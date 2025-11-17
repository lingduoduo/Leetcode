function hasSameDigits(s: string): boolean {
    let digits: number[] = s.split('').map(Number);

    while (digits.length > 2) {
        const newDigits: number[] = [];
        for (let i = 0; i < digits.length - 1; i++) {
            newDigits.push((digits[i] + digits[i + 1]) % 10);
        }
        digits = newDigits;
    }

    return digits[0] === digits[1];
};
