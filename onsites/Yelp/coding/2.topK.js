/* 
输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
 */

// https://leetcode.cn/problems/top-k-frequent-words/
const topKFrequent = function (words, k) {
	if (k <= 0) {
		return []
	}
	const map = new Map()
	for (const word of words) {
		map.set(word, (map.get(word) || 0) + 1)
	}
	const res = []
	for (const word of map.keys()) {
		res.push(word)
	}
	res.sort((word1, word2) => {
		if (map.get(word1) === map.get(word2)) {
			return word1.localeCompare(word2) //字典顺序
		} else {
			return map.get(word2) - map.get(word1) //频率降序
		}
	})
	return res.slice(0, k)
}

/*
时间复杂度： O(l×n+l× mlogm)
空间复杂度： O(l×m)

l 表示字符串的平均长度，
m 表示实际字符串种类数。
n 表示arr长度
mlogm 表示字符串比较的次数
时间复杂度:我们需要 l×n 的时间将字符串插入到哈希表中，
以及 l*mlogm 的时间完成字符串比较（最坏情况下所有字符串出现频率都相同，我们需要将它们两两比较）。
*/
/* 
- follow up：如何处理 spam？数据结构是否能更优化？
- 时间空间复杂度？
 */

/* 
coding一轮，love msg.  follow up有怎么处理spam:用set记录发送者，排序用size排。又问:如果spam在内容里面咋办，答把关键字存数据库里面，或者存tire里面，过滤。
 */

/* 

给你一个 Love Class
class Love {
    String sender;
    String receiver;
    String message;
    public Log(String s, String r, String m) {
        sender = s;
        receiver = r;
        message = m;
    }
}
input = new Love[] {new Love("aaa", "bbbb", "message1"), 
new Love("aaa","dddd", "message2"), 
new Love("aaa","cccc", "message2"), 
new Love("cccc",“bbbb", "message2")}

让你求收到love message Top k的 比如过这个例子就是就是 bbbb， 2次， dddd 1次， cccc 一次， 如果收到次数相同不需要二次排序，任意顺序返回即可。

解法： 用最小堆 维护优先级队列，

注意：一些edge case看你有没有写，比如过input == null， 比如说 k 小于 0， 比如说 k 等于 0


follow up：
如
发送方，接收方和message
new Love("aaa", "bbbb", "message1")
new Love("aaa", "bbbb", "message2")
同一个 sender send 到同一个 reveiver 多次，算作spam，这个时候只能算一次，怎么求top K。


用一个hashmap<sender, HashSet<String>> 存sender send 了哪些receiver，如果这个receiver已经有了， continue就好
换成sender，boundary case譬如两人频率都是10
*/

class Love {
	constructor(s, r, m) {
		this.sender = s
		this.receiver = r
		this.message = m
	}
}

const input = [
	new Love('A', 'great', 'X'),
	new Love('A', 'great1', 'X'),
	new Love('A', 'great2', 'X'),
	new Love('B', 'great3', 'X'),
	new Love('B', 'great4', 'Y'),
	new Love('B', 'great5', 'Z'),
	new Love('C', 'great5', 'X'),
	new Love('C', 'great5', 'Y'),
]
//output : ['A', 'B', 'C']

//如果spam在receiver中
function topKLoveMessage(input, k) {
	if (k <= 0) {
		return []
	}
	const map = new Map()
	for (const love of input) {
		if (!love) {
			continue
		}
		map.set(love.sender, (map.get(love.sender) || new Set()).add(love.receiver))
	}
	const res = []
	for (const love of map.keys()) {
		res.push(love)
	}
	res.sort((s1, s2) => {
		if (map.get(s1).size === map.get(s2).size) {
			return s1.localeCompare(s2)
		} else {
			return map.get(s2).size - map.get(s1).size
		}
	})
	return res.slice(0, k)
}

console.log(topKLoveMessage(input, 2))

//处理message 的spam, 防止相同消息灌水  （答把关键字存数据库里面，或者存tire里面，过滤）
function topKLoveMessage2(input, k) {
	if (k <= 0) {
		return []
	}
	const map = new Map()
	for (const love of input) {
		if (!love) {
			continue
		}
		map.set(love.sender, (map.get(love.sender) || new Set()).add(love.message))
	}
	const res = []
	for (const love of map.keys()) {
		res.push(love)
	}
	res.sort((s1, s2) => {
		if (map.get(s1).size === map.get(s2).size) {
			return s1.localeCompare(s2)
		} else {
			return map.get(s2).size - map.get(s1).size
		}
	})
	return res.slice(0, k)
}
/* 
最优解
#  用min heap，维护一个大小为k的priorityQueue，最后把所有的节点都poll出来，Collections reveres即可。
*/
