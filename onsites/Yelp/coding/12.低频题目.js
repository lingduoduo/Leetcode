{
	//leetCode 255  设计推特

	/* 
  写一个post的类，里面只存userId和tweetId
  将所有用户的post用一个链表存起来，采用头插法来保证时间近的在前
  用哈希表维护用户关系，key是用户id，value是 所关注用户的集合，follow和un-follow实际上就是去操作这个集合
  查询用户post时，就从链表里面找出10个 用户自己和所关注用户的post 就行了
 */
	class Post {
		constructor(userId, tweetId) {
			this.userId = userId
			this.tweetId = tweetId
		}
	}
	class Twitter {
		constructor() {
			this.allPost = [] // 所有用户的推文
			this.map = {} //id:int[]   userId -> 关注的用户Id[]
		}

		postTweet(userId, tweetId) {
			let set = this.map[userId] || new Set()
			set.add(userId)
			this.map[userId] = set
			this.allPost.unshift(new Post(userId, tweetId)) // 时间近的在前
		}

		getNewsFeed(userId) {
			let set = this.map[userId]
			let res = []
			for (let post of this.allPost) {
				if (set.has(post.userId)) res.push(post.tweetId)
				if (res.length == 10) break
			}
			return res
		}

		follow(owner, fan) {
			let set = this.map[owner] || new Set()
			set.add(fan)
			this.map[owner] = set
		}

		unfollow(owner, fan) {
			let set = this.map[owner] || new Set()
			set.delete(fan)
			this.map[owner] = set
		}
	}
}
/* 
数据量很大怎么办？  
分到多个node上，进行topK操作，然后merge
*/

const test = [{ walmart: 2 }, { facebook: 1 }, { starbucks: 1 }]
function sortArr(test) {
	test.sort((a, b) => {
		if (Object.values(a)[0] !== Object.values(b)[0]) {
			return Object.values(a)[0] - Object.values(b)[0]
		} else {
			return Object.keys(a)[0].localeCompare(Object.keys(b)[0])
		}
	})
	return test
}
// printArr(test)
function printArr(test) {
	// console.log(Reflect.ownKeys(test[0]))
}
console.log(sortArr(test))

// Jaccard similarity
//两个集合A和B的交集元素在A，B的并集中所占的比例，称为两个集合的Jaccard相似系数，用符号J(A,B)表示。​
//
// Jaccard相似系数是衡量两个集合的相似度一种指标。
/* 
num_intersection= len( set_A & set_B )
num_union= len(set_A)+ len(set_B)- num_intersection.
 */

function get_jaccard_similarity(list1, list2) {
	let intersection = len(list(set(list1).intersection(list2)))
	let union = len(set(list1)) + len(set(list2)) - intersection
	return intersection / union
}
/* 
第二道题给一个target object, 和一个 object list, 找到object list 里面和target object相似度最高的object.
题目都很简单．他问我set求intersection　的worst complexity. 我没想到应该考虑 collision resolution...没答上来

A: Hash set 的实现用到了hash function. Worst case, 就是set 里面所有的key都发生了collision. 
在这种情况下, 如果collision resolution是基于chaining (linked list), 则需要访问linked list 里面的每一个key.
 比如说求 set1  和set2 的 intersection, 则对于每个set1 里面的元素, 
 判断它是不是交集里面的一个元素需要复杂度是O( len(set2) ). 所以求set1 & set2 复杂度变成了 O( len(set1)* len(set2) ).
 */
