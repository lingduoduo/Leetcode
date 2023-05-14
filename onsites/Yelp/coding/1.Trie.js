class Trie {
	constructor() {
		this.root = {}
	}
	insert(word) {
		let node = this.root
		for (const c of word) {
			if (!node[c]) node[c] = {}
			node = node[c]
		}
		node.isWord = true
	}
	traverse(word) {
		let node = this.root
		for (const c of word) {
			node = node[c]
			if (!node) return null
		}
		return node
	}
	search(word) {
		const node = this.traverse(word)
		return !!node && node.isWord
	}
	startsWith(prefix) {
		return !!this.traverse(prefix)
	}
}
const trie = new Trie()
trie.insert('apple')
trie.search('apple')
trie.search('app')
trie.startsWith('app')
trie.insert('app')
trie.search('app')

const res = {
	a: {
		p: {
			p: {
				isWord: true,
				l: {
					e: {
						isWord: true,
					},
				},
			},
		},
	},
}
