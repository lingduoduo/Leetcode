/* 
人名的List
两两配对
*/
const people1 = [
	{ id: 'Alan', team: 'a' },
	{ id: 'Da', team: 'a' },
	{ id: 'Jen', team: 'c' },
	{ id: 'Kevin', team: 'd' },
	{ id: 'Neha', team: 'm' },
	{ id: 'Rachel', team: 'q' },
	{ id: 'Tom', team: 'a' },
]
const people2 = [
	{ id: 'Alan', team: 'a' },
	{ id: 'Da', team: 'a' },
]

console.log('result=', matchBeans(people1))
// console.log('result=', matchBeans(people2))
/* 
result= [
  [ { id: 'Rachel', team: 'q' }, { id: 'Alan', team: 'a' } ],
  [ { id: 'Da', team: 'a' }, { id: 'Neha', team: 'm' } ],
  [ { id: 'Kevin', team: 'd' }, { id: 'Jen', team: 'c' } ],
  [ { id: 'Tom', team: 'a' }, null ]
]
result= [
  [ { id: 'Alan', team: 'a' }, null ],
  [ { id: 'Da', team: 'a' }, null ]
]
*/
//user有一个team属性，同一个team的人不能分为同一组
{
	/* 
  大概感觉就是一个长度为n的arraylist，选一个random index作为随机user，然后把这个元素和最后一个元素交换，删除最后一个元素。
  之后再从新的arraylist里面选random index，所以可以保证不会重复
 */
	function randGetPeople(people, lastIdx, team) {
		const restDistinctArr = people.filter((p, idx) => p.team !== team && idx <= lastIdx)
		if (restDistinctArr.length <= 0) {
			return null
		}
		let p = Math.floor(Math.random() * (lastIdx + 1))
		while (people[p].team === team) {
			p = Math.floor(Math.random() * (lastIdx + 1))
		}
		const v = people[p]
		;[people[lastIdx], people[p]] = [people[p], people[lastIdx]]
		return v
	}

	function matchBeans(people) {
		const res = []
		let lastIdx = people.length - 1
		while (lastIdx > 0) {
			const one = randGetPeople(people, lastIdx--)
			const two = randGetPeople(people, lastIdx--, one.team)
			res.push([one, two])
			if (!two) lastIdx++ //有单个的存在
		}
		if (lastIdx === 0) {
			res.push([people[lastIdx], null])
		}
		return res
	}
}

// 洗牌算法
// shuffle后按顺序抽取
function shuffle(arr) {
	let n = arr.length
	for (let i = 0; i < arr.length; i++) {
		const random = Math.floor(Math.random() * (n - i) + i) // [i,n]才能保证是可能性是n!，因为i要小于length, 正常时是需要+1的，此时不用
		;[arr[random], arr[i]] = [arr[i], arr[random]]
	}
	return arr
}

{
	/* 
第一问直接相邻两个配对
第二问同一组的不能配对 我用了一个map和一个pq
 */
}
