function myPow(x: number, n: number): number {
    if (n === 0) return 1
    if (n === 1) return x
    
    if (n < 0){
        x = 1/x
        n = -n
    }

        
    let p = myPow(x, Math.floor(n/2))
    if (n % 2 === 1)
        return x * p * p
    else
        return p * p
};