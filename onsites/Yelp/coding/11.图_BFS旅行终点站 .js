// 1436. 旅行终点站
/* 
输入：paths = [["B","C"],["D","B"],["C","A"]]
输出："A"
解释：所有可能的线路是：
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
显然，旅行终点站是 "A" 。

 */

/* 
follow up： loop : 

2: ["b","c","F","D"]


*/
//直到当前城市无法到达下一个城市,就是终点
{
	//单个出口，无环
	//BFS
	const destCity = function (paths) {
		if (paths == null || paths.length == 0) {
			return ''
		}
		//构建图
		const map = {}
		for (let path of paths) {
			const [from, to] = path
			if (!map[from]) {
				map[from] = []
			}
			map[from].push(to)
		}
		//
		let queue = [] // []string
		queue.push(paths[0][1]) //end point
		while (queue.length !== 0) {
			let pos = queue.shift()
			if (map[pos]) {
				for (let next of map[pos]) {
					// 针对多点也试用
					queue.push(next)
				}
			} else {
				return pos
			}
		}
		return ''
	}
	console.log(
		destCity([
			['B', 'C'],
			['D', 'B'],
			['C', 'A'],
		])
	)
}

//有环, 需要从每个点出发，找到终点
/* 
时间复杂度：O(n)
空间复杂度：O(n)
 */

{
	//判断是否有环
	const destCityCircle = function (paths) {
		if (paths == null || paths.length == 0) {
			return false
		}
		const map = {}
		const pointArr = new Set()
		for (let path of paths) {
			for (let item of path) {
				pointArr.add(item)
			} // count all points
			const from = path[0]
			const to = Array.from(path).splice(1)
			if (!map[from]) {
				map[from] = []
			}
			map[from].push(...to)
		}
		// 打乱数组？无所谓
		//构建入度map
		const inDegree = {}
		for (let path of paths) {
			for (let i = 1; i < path.length; i++) {
				const to = path[i]
				if (!inDegree[to]) {
					inDegree[to] = 0
				}
				inDegree[to]++
			}
		}

		let queue = []
		// let visited = new Set()
		for (let start of Object.keys(map)) {
			if (!inDegree[start]) {
				queue.push(start) // 入度点
			}
		}
		let count = 0
		while (queue.length !== 0) {
			let pos = queue.shift()
			count++
			if (map[pos]) {
				for (let next of map[pos]) {
					inDegree[next]--
					if (inDegree[next] === 0) {
						queue.push(next)
					}
				}
			}
		}
		console.log(count, pointArr.size)
		return count !== pointArr.size
		// return false // OK
	}
	console.log(
		'should be true, exist circle==>' +
			destCityCircle([
				['A', 'B'],
				['B', 'C'],
				['C', 'D'],
				['D', 'E'],
				['E', 'B'],
			])
	)
	console.log(
		'should be false==>' +
			destCityCircle([
				['D', 'B'],
				['B', 'C'],
				['C', 'A'],
				['A', 'E'],
			])
	)
}

/* 
如果一个节点有多个边怎么办，答用bfs，hashmap的值用来存储所有出度的终点，循环到没有出度的点时，把它加进答案list里。
 */

{
	const findAllEndpoint = function (paths) {
		if (paths == null || paths.length == 0) {
			return []
		}
		//构建图
		const map = {}
		const pointArr = new Set()
		for (let path of paths) {
			for (let item of path) {
				pointArr.add(item)
			} // count all points
			const from = path[0]
			const to = Array.from(path).splice(1)
			if (!map[from]) {
				map[from] = []
			}
			map[from].push(...to)
		}
		//构建入度map

		const inDegree = {}
		for (let path of paths) {
			for (let i = 1; i < path.length; i++) {
				const to = path[i]
				if (!inDegree[to]) {
					inDegree[to] = 0
				}
				inDegree[to]++
			}
		}
		// console.log(inDegree)
		let res = []
		let queue = []
		let visited = new Set()
		for (let start of Object.keys(map)) {
			if (!inDegree[start]) {
				queue.push(start) // 入度为0的点
			}
		}
		while (queue.length !== 0) {
			let pos = queue.shift()
			if (map[pos]?.length > 0) {
				for (let next of map[pos]) {
					if (visited.has(next)) {
						continue
					}
					visited.add(next)
					queue.push(next)
				}
			} else {
				res.push(pos) // end point
			}
		}
		return res
	}
	console.log(
		'Exit points includes: ==>' +
			findAllEndpoint([
				['C', 'D', 'F', 'G'],
				// ['C', 'D'],
				['A', 'B'],
				['B', 'C', 'R'],
				['D', 'E'],
				['E', 'B'],
			])
	)
}
