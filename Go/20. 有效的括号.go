package main

import "fmt"

/**
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
func isValid(s string) bool {
	flag := false
	m := make(map[byte]byte)
	m['('] = ')'
	m['['] = ']'
	m['{'] = '}'
	sli := make([]byte, 0)
	if len(s) == 0 {
		return true
	}
	if len(s)%2 == 1 {
		return false
	}
	for i, b := range s {
		if i == 0 && (s[i] == ')' || s[i] == ']' || s[i] == '}') {
			return false
		}
		if b == '(' || b == '[' || b == '{' {
			sli = append(sli, byte(b))
		} else if b == ')' || b == ']' || b == '}' {
			left := sli[len(sli)-1]
			sli = sli[:len(sli)-1]
			if m[left] == byte(b) {
				flag = true
			} else {
				return false
			}
		}
		if i == len(s)-1 && len(sli) != 0 {
			flag = false
		}
	}
	return flag
}

func main() {
	fmt.Println(isValid("()[]{}"))
}
