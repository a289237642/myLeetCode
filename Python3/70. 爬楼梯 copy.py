假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for i in range(n):
            a, b = b, a + b
        return a




https://leetcode-cn.com/problems/sliding-window-maximum/
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/

https://leetcode-cn.com/problems/min-stack/
https://leetcode-cn.com/problems/valid-parentheses/description/


https://leetcode-cn.com/problems/design-circular-deque/
https://leetcode-cn.com/problems/trapping-rain-water/

https://leetcode-cn.com/problems/valid-anagram/description/
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

https://leetcode-cn.com/problems/valid-anagram/description/
https://leetcode-cn.com/problems/group-anagrams/
https://leetcode-cn.com/problems/two-sum/description/





class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        se = set(s)
        if se == set(t):
            for i in se:
                # 直接比较字符元素个数比较字符的个数
                if s.count(i) != t.count(i):return False
            return True
        else:
            return False


root = [1,null,3,2,4,null,5,6]



