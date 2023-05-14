//528
/* 
按权重随机选择

给你一个 下标从 0 开始 的正整数数组 w ，其中 w[i] 代表第 i 个下标的权重。
请你实现一个函数 pickIndex ，它可以 随机地 从范围 [0, w.length - 1] 内（含 0 和 w.length - 1）
选出并返回一个下标。选取下标 i 的 概率 为 w[i] / sum(w) 。
例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），
而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。
*/
/* 

例如输入数组为[1,2,3,4]，则划分：[1,1], [2,3], [4,5,6], [7,8,9,10]，求出前缀和数组[1,3,6,10]。
生成[1,10]之间的一个随机整数，用二分查找在前缀和数组中寻找满足区间条件的最小下标i，并返回。
*/
class Solution {
	constructor(w) {
		this.len = w.length
		this.pre = new Array(this.len).fill(0)
		this.pre[0] = w[0]
		for (let i = 1; i < this.len; i++) {
			this.pre[i] = this.pre[i - 1] + w[i]
		}
		this.total = this.pre[this.len - 1]
	}
	pickIndex() {
		// x 是 1 ~ total 之间的一个随机整数
		const x = Math.floor(Math.random() * this.total) + 1
		const binarySearch = (x) => {
			let low = 0,
				high = this.pre.length - 1
			while (low < high) {
				const mid = Math.floor((high - low) / 2) + low
				if (this.pre[mid] < x) {
					low = mid + 1
				} else {
					high = mid
				}
			}
			return low
		}
		return binarySearch(x)
	}
}
/* 
时间复杂度：初始化的时间复杂度为 O(n)，每次选择的时间复杂度为 O(logn)，其中 nn 是数组 ww 的长度。

空间复杂度:O(n)，即为前缀和数组 pre 需要使用的空间。
 */
