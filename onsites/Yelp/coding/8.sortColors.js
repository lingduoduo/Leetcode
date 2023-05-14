// 75. 颜色分类
/* 
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

 */
function sortColors(nums) {
	let n = nums.length
	// let p0 = 0,
	// 	p2 = n - 1
	// for (let i = 0; i <= p2; ++i) {
	// 	while (i <= p2 && nums[i] == 2) {
	// 		;[nums[i], nums[p2]] = [nums[p2], nums[i]]
	// 		p2--
	// 	}
	// 	if (nums[i] == 0) {
	// 		;[nums[i], nums[p0]] = [nums[p0], nums[i]]
	// 		p0++
	// 	}
	// }
	let p = 0,
		q = n - 1
	for (let i = 0; i <= q; ++i) {
		if (nums[i] == 0) {
			nums[i] = nums[p]
			nums[p] = 0
			p++
		}
		if (nums[i] == 2) {
			nums[i] = nums[q]
			nums[q] = 2
			q--
			if (nums[i] != 1) {
				i--
			}
		}
	}
	return
}

/* 
时间复杂度O(n)
空间复杂度：O(1)。
 */
