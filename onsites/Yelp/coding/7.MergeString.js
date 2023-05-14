/* 
（输入）abc + bcd = （输出）abcd。
消除第一个字符串结尾和第二个字符串开头的重复部分并合并字符串。
 */

function mergeString(s1, s2) {
	let i = 0
	let j = 0
	while (i < s1.length) {
		while (i < s1.length && j < s2.length && s1[i] == s2[j]) {
			i++
			j++
			if (i == s1.length) {
				return s1 + s2.substring(j)
			}
		}
		i++
		j = 0
	}
	return false
}

console.log(mergeString('abc', 'bcd'))
