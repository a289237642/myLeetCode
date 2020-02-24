/**
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	charCounts := make([][]int, 2)
	charCounts[0] = make([][]int, 26)
	charCounts[1] = make([][]int, 26)

	for i:=0;i<len(s);i++{
		charCounts[0][s[i]-'a']+=1
		charCounts[1][t[i]-'a']+=1
	}

	for i:=0;i<26;i++{
		if charCounts[0][i]！=charCounts[1][i]{
			return false
		}
	}
	return true
}