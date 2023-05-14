/* 
饭馆等座位问题，有不同人数的party，一个桌子，先到先安排。
直接用一个像LRU那样的双向链表就解决了
follow up 是 解决饭馆只想4人桌坐4个人，队里即使只有2人的party也不给安排。
 */

class SeatManager {
	constructor(n) {
		this.data = new Array(n + 1).fill(true)
	}
	reserve = function () {
		let len = this.data.length
		for (let i = 1; i < len; i++) {
			if (this.data[i]) {
				this.data[i] = false
				return i
			}
		}
	}

	unreserve = function (seatNumber) {
		this.data[seatNumber] = true
	}
}

/* 
已知有一张open table，和一个waiting list [{size, name, queue_time},{...},...]
要求返回等候最久且party size <= table size 的 party name
并且把这个party从waiting list中删除

如果当前free table size是3的话，返回小猫组，因为小狗组坐不下，小鸟比小猫后来。如果是4的话，返回小狗组，因为小狗组最先来。

 */
// [{size, party_name, queue_time}]
{
	const tableSize = 5
	const test = [
		{ name: 'dog', size: 4, waitTime: 150 },
		{ name: 'cat', size: 2, waitTime: 200 },
		{ name: 'bird', size: 3, waitTime: 300 },
	]

	function findParty(tableSize, list) {
		list.sort((a, b) => {
			return a.waitTime - b.waitTime
		})
		let res
		let index = 0
		for (let item of list) {
			if (item.size <= tableSize) {
				res = item.name
				list.splice(index, 1) // 删除这个party
				break
			}
			index++
		}
		return res
	}
	console.log(findParty(3, test))
	console.log(findParty(4, test))
}
/* 
follow up 1， 另外一个饭店必须是桌子正好等于party人数才可以入座 if (tableSize === partySize) 
follow up 2， 把上面两个function整合,
 */

{
	// 要求返回等候最久且party size <= table size 的 party name
	const test = [
		{ name: 'dog', size: 4, waitTime: 150 },
		{ name: 'cat', size: 2, waitTime: 200 },
		{ name: 'bird', size: 3, waitTime: 300 },
		{ name: 'customer', size: 3, waitTime: 3000 },
	]

	function findParty(tableSize, list) {
		list.sort((a, b) => {
			return b.waitTime - a.waitTime
		})
		let res
		for (let item of list) {
			if (item.size <= tableSize) {
				res = item.name
				break
			}
		}
		return res
	}
	// console.log(findParty(3, test))
	// console.log(findParty(4, test)) //等候最久
}
{
	// 但是当有一个party的queue_time >= 30min时，优先安排这个party
	// 当没有party size == table size或者等待超过30min的party size > table size时，小餐厅和大餐厅一样，都是优先queue_time
	// 当waiting list为空，或没有party 满足要求时，输出err_msg
	const test = [
		{ name: 'dog', size: 4, waitTime: 150 },
		{ name: 'cat', size: 2, waitTime: 200 },
		{ name: 'bird', size: 3, waitTime: 300 },
		{ name: 'customer', size: 3, waitTime: 3000 },
		{ name: 'customer2', size: 4, waitTime: 3000 },
	]

	function findParty(tableSize, list) {
		list.sort((a, b) => {
			if (b.waitTime !== a.waitTime) {
				return b.waitTime - a.waitTime
			} else {
				return b.size - a.size
			}
		})
		let res
		for (let item of list) {
			if (item.size <= tableSize) {
				res = item.name
				break
			}
		}
		return res
	}
	console.log(findParty(3, test)) //customer
	console.log(findParty(4, test)) //等候最久 customer2
}
