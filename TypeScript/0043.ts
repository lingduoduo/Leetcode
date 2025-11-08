function multiply(num1: string, num2: string): string {
    // Edge case: if either is "0", result is "0"
    if (num1 === "0" || num2 === "0") return "0";

    const n1 = num1.length;
    const n2 = num2.length;

    const res: number[] = new Array(n1 + n2).fill(0);

    for (let i = n1 - 1; i >= 0; i--) {
        const d1 = num1.charCodeAt(i) - "0".charCodeAt(0); 
        for (let j = n2 - 1; j >= 0; j--) {
            const d2 = num2.charCodeAt(j) - "0".charCodeAt(0); 

            const posLow = i + j + 1;  
            const posHigh = i + j;     

            const sum = res[posLow] + d1 * d2;

            res[posLow] = sum % 10;
            res[posHigh] += Math.floor(sum / 10);
        }
    }

    let k = 0;
    while (k < res.length && res[k] === 0) k++;

    return res.slice(k).join("");
}
