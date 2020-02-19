import "math"

/**
 * 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
 *
 * push(x) -- 将元素 x 推入栈中。 pop() -- 删除栈顶的元素。 top() -- 获取栈顶元素。 getMin() --
 * 检索栈中的最小元素。 示例:
 *
 * MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0);
 * minStack.push(-3); minStack.getMin(); --> 返回 -3. minStack.pop();
 * minStack.top(); --> 返回 0. minStack.getMin(); --> 返回 -2.
 *
 * 来源：力扣（LeetCode） 链接：https://leetcode-cn.com/problems/min-stack
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

type MinStack struct {
	Val  int
	Min  int
	Next *MinStack
}

func Constructor() MinStack {
	return MinStack{0, 0, nil}
}

func (this *MinStack) Push(x int) {
	Min := x
	if this.Next != nil {
		Min = int(math.Min(float64(x), float64(this.Next.Min)))
	}
	temp := &MinStack{Val: x, Min: Min, Next: this.Next}
	this.Next = temp
}

func (this *MinStack) Pop() {
	if this.Next == nil {
		return 0
	}
	return this.Next.Val
}

func (this *MinStack) GetMin() int {
	if this.Next == nil {
		return 0
	}
	return this.Next.Min
}