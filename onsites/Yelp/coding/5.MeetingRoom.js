/* 
LeetCode 252
输入：intervals = [[0,30],[5,10],[15,20]]
输出：false
请你判断一个人是否能够参加这里面的全部会议。
*/
var canAttendMeetings = function (intervals) {
	// 将传入的数组按照 第一个数字升序排列
	intervals.sort((a, b) => {
		return a[0] - b[0]
	})
	const len = intervals.length
	for (let i = 0; i < len - 1; i++) {
		if (intervals[i][1] > intervals[i + 1][0]) {
			return false
		}
	}
	return true
}
/* 
时间复杂度 : O(nlogn) 。时间复杂度由排序决定。一旦排序完成，只需要 O(n) 的时间来判断交叠。
空间复杂度 : O(1)。没有使用额外空间。
 */

/* 
leetCode 253
给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回所需会议室的最小数量 
输入：intervals = [[0,30],[5,10],[15,20]]
输出：2
*/
/* 
上车：[0, 1], [5, 1], [15, 1]
下车：[10, -1], [20, -1], [30, -1]

=>  [0, 1], [5, 1],[10, -1], [15, 1], [20, -1],[30, -1]
*/
var minMeetingRooms = function (intervals) {
	const nums = []
	for (const [start, end] of intervals) {
		nums.push([start, 1])
		nums.push([end, -1])
	}
	nums.sort((a, b) => {
		if (a[0] === b[0]) {
			return a[1] - b[1]
		} else {
			return a[0] - b[0]
		}
	})
	let maxRoom = 0
	let cur = 0
	for (let i = 0; i < nums.length; i++) {
		cur += nums[i][1]
		maxRoom = Math.max(maxRoom, cur)
	}
	return maxRoom
}

{
	var minMeetingRooms = function (intervals) {
		if (intervals.length === 0) return 0
		intervals.sort((a, b) => a[0] - b[0])
		let rooms = []
		rooms.push(intervals[0])
		let maxRoom = 1
		for (let i = 1; i < intervals.length; i++) {
			if (intervals[i][0] >= rooms[0][1]) {
				rooms.shift()
			}
			rooms.push(intervals[i])
			maxRoom = Math.max(maxRoom, rooms.length)
			rooms.sort((a, b) => a[1] - b[1])
		}
		return maxRoom
	}
}

{
	//找meetingRooms数组中的交集
	var intervalIntersection = function (firstList, secondList) {
		let i, j
		i = j = 0

		let res = []

		while (i < firstList.length && j < secondList.length) {
			let a1 = firstList[i][0]
			let a2 = firstList[i][1]
			let b1 = secondList[j][0]
			let b2 = secondList[j][1]

			//  两个区间存在交集
			if (b2 >= a1 && a2 >= b1) {
				// 计算出交集，加入 res
				res.push([Math.max(a1, b1), Math.min(a2, b2)])
			}
			// 指针前进
			if (b2 < a2) {
				j += 1
			} else {
				i += 1
			}
		}
		return res
	}
	//
}

{
	const test = [
		[0, 30],
		[5, 10],
		[15, 20],
		[20, 30],
		[31, 40],
		[41, 43],
		[46, 50],
	]
	//问如果想把不重叠的interval分别写出来怎么办，就用个pq，按end time排

	function findNoOverlayRoom(arr) {
		arr.sort((a, b) => {
			if (a[0] == b[0]) {
				return b[1] - a[1]
			}
			return a[0] - b[0]
		})
		//
		let start = arr[0][0]
		let end = arr[0][1]
		let res = []
		for (let [nextStart, nextEnd] of arr) {
			// 情况一，找到覆盖区间
			if (nextStart >= start && nextEnd <= end) {
				//res++
			}
			// 情况二，找到相交区间，合并
			if (end >= nextStart && end <= nextEnd) {
				end = nextEnd
			}
			// 情况三，完全不相交，更新起点和终点
			if (end < nextStart) {
				start = nextStart
				end = nextEnd
				res.push([start, end])
			}
		}
		return res
	}
	// console.log(findNoOverlayRoom(test))
}

{
	//合并区间
	const test = [
		[0, 30],
		[5, 10],
		[15, 20],
		[20, 30],
		[31, 40],
		[41, 43],
		[46, 50],
	]
	function mergeRoom(arr) {
		arr.sort((a, b) => {
			if (a[0] == b[0]) {
				return b[1] - a[1]
			}
			return a[0] - b[0]
		})
		let start = arr[0][0]
		let end = arr[0][1]
		let res = []
		for (let [nextStart, nextEnd] of arr) {
			// 情况一，找到覆盖区间
			if (nextStart >= start && nextEnd <= end) {
				//res++
				// res.push([start, end])
			}
			// 情况二，找到相交区间，合并
			if (end >= nextStart && end <= nextEnd) {
				end = nextEnd
				const existFlag = res.find((v) => v[0] == start && v[1] == end) //arr
				if (!existFlag) {
					res.push([start, end])
				}
			}
			// 情况三，完全不相交，更新起点和终点
			if (end < nextStart) {
				start = nextStart
				end = nextEnd
				res.push([start, end])
			}
		}
		//remove duplicate room in res

		return res
	}

	console.log(mergeRoom(test))
}
/* 
1. find if there are any overlaps between those intervals
2. find the minimum of meeting rooms to hold of those meetings (greedy, sort first, 
  then merge intervals in the same meeting room into one interval,
   and then use a BST to find by end time when you insert th‍‌‍‌‍‌‌‌‌‍‌‍‌‌‍‍‍‌‌‌e new intervals).

follow up:
问如果想把不重叠的interval分别写出来怎么办，就用个pq，按end time排
*/
