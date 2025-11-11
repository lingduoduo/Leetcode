class ParkingSystem {
    private spaces: Record<number, number>;

    constructor(big: number, medium: number, small: number) {
        this.spaces = {
            1: big,
            2: medium,
            3: small
        };
    }

    addCar(carType: number): boolean {
        if (this.spaces[carType] === 0) {
            return false;
        }
        this.spaces[carType]--;
        return true;
    }
}