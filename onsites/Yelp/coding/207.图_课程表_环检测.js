var canFinish = function (numCourses, prerequisites) {
	let hasCycle = false
	let visited // boolean[]
	let onPath //boolean[]
	let graph = buildGraph(prerequisites, numCourses)
	visited = new Array(numCourses).fill(false)
	onPath = new Array(numCourses).fill(false)
	for (let i = 0; i < numCourses; i++) {
		if (!visited[i]) {
			dfs(graph, i)
		}
	}

	function dfs(graph, s) {
		// 判断当前要处理的节点是否在 onPath 中 如果在，则存在环
		if (onPath[s]) {
			hasCycle = true
		}
		// 判断是否访问过 以及 是否已经检测出了环
		if (visited[s] || hasCycle) {
			return
		}
		visited[s] = true
		onPath[s] = true
		for (let v of graph[s]) {
			dfs(graph, v)
		}
		onPath[s] = false
	}
	return !hasCycle // hasCycle means cannot finish
}

function buildGraph(prerequisites, numCourses) {
	let graph = new Array(numCourses).fill(0)
	for (let i = 0; i < numCourses; i++) {
		graph[i] = []
	}
	for (let edge of prerequisites) {
		let from = edge[1],
			to = edge[0]
		graph[from].push(to)
	}
	return graph
}
