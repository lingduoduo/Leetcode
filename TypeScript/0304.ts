class NumMatrix {
  private n: number;
  private m: number;
  private presum: number[][];

  constructor(matrix: number[][]) {
    this.n = matrix.length;
    this.m = this.n > 0 ? matrix[0].length : 0;

    // build (n+1) x (m+1) 2D array filled with 0
    this.presum = Array.from({ length: this.n + 1 }, () =>
      new Array(this.m + 1).fill(0)
    );

    for (let i = 0; i < this.n; i++) {
      for (let j = 0; j < this.m; j++) {
        this.presum[i + 1][j + 1] =
          this.presum[i + 1][j] + this.presum[i][j + 1] + matrix[i][j] - this.presum[i][j];
      }
    }
  }

  sumRegion(row1: number, col1: number, row2: number, col2: number): number {
    // inclusive row1..row2, col1..col2
    return (
      this.presum[row2 + 1][col2 + 1] - this.presum[row1][col2 + 1] - this.presum[row2 + 1][col1] + this.presum[row1][col1]
    );
  }
}
