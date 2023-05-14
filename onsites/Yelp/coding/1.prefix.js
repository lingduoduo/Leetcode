const rawData = [
	{ business_name: "McDonald's" },
	{ business_name: "Bob's Burgers" },
	{ business_name: 'Five Guys' },
	{ business_name: 'Super Duper Burgers' },
	{ business_name: 'Burger King' },
	{ business_name: 'Wahlburgers' },
]

/* 

1.brute force
2.string.indexOf
3.Trie tree 字典树
*/
/* 搜索query: "bur"
找到  {"business_name": "Burger King"}, 
 {"business_name": "Bob’s Burgers"},  
{"business_name": "Super Duper Burgers"} 带前缀有“bur”的
 */
{
	function getPrefix(data, k) {
		const res = []
		for (let item of data) {
			if (k === 0) {
				break
			}
			const name = item.business_name
			const nameArr = name.toLowerCase().split(' ')
			for (let childName of nameArr) {
				if (childName.startsWith('bur')) {
					res.push(item)
					k--
					break
				}
			}
		}
		res.sort((a, b) => {
			return (
				a.business_name.toLowerCase().indexOf('bur') -
				b.business_name.toLowerCase().indexOf('bur')
			)
		})
		return res
	}
	console.log(getPrefix(rawData, 3))
}
//follow up: 1.不限制prefix
{
	function getPrefix(data) {
		const res = []
		data?.map((item) => {
			const name = item.business_name
			const nameArr = name.toLowerCase().split(' ')
			for (let childName of nameArr) {
				if (childName.includes('bur')) {
					res.push(item)
					break
				}
			}
		})
		return res
	}
	console.log(getPrefix(rawData))
}

// 怎么优化？
// 可以把prefix放在前面，然后把前缀放在后面，这样就不用每次都去比较了
