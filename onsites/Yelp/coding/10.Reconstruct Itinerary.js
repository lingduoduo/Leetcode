var findItinerary = function (tickets) {
	var map = {}
	for (const ticket of tickets) {
		const [from, to] = ticket
		if (!map[from]) {
			map[from] = []
		}
		map[from].push(to)
	}
	for (const city in map) {
		map[city].sort()
	}
	const tar = tickets.length
	const ans = ['JFK']

	function dfs(start, n) {
		if (n === tar) {
			return true
		}
		let nextCity = map[start] // arr []
		if (!nextCity || nextCity.length === 0) return false

		for (let i = 0; i < nextCity.length; i++) {
			let city = nextCity[i]
			nextCity.splice(i, 1)
			ans.push(city)
			if (dfs(city, n + 1)) {
				return true
			}
			ans.pop()
			nextCity.splice(i, 0, city)
		}
		return false
	}
	dfs('JFK', 0)
	return ans
}
