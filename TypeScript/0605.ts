function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    for (let i = 0; i < flowerbed.length; i++){
        if (flowerbed[i] === 1) continue;
        if (i > 0 && flowerbed[i - 1] === 1) continue;
        if (i < flowerbed.length - 1 && flowerbed[i + 1] === 1) continue;
        flowerbed[i] = 1;
        n -= 1
    }
    return (n <= 0)
};