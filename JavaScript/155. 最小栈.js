/**
 * 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
 * 
 * push(x) -- 将元素 x 推入栈中。 pop() -- 删除栈顶的元素。 top() -- 获取栈顶元素。 getMin() --
 * 检索栈中的最小元素。 示例:
 * 
 * MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0);
 * minStack.push(-3); minStack.getMin(); --> 返回 -3. minStack.pop();
 * minStack.top(); --> 返回 0. minStack.getMin(); --> 返回 -2.
 * 
 * 来源：力扣（LeetCode） 链接：https://leetcode-cn.com/problems/min-stack
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

 /**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.s1 = [];
    this.s2 = [];
  };
  
  /** 
   * @param {number} x
   * @return {void}
   */
  MinStack.prototype.push = function(x) {
    let s2 = this.s2,
        s2Len = s2.length,
        s1 = this.s1;
    
    
    let curMin = s2[s2Len-1];
    if(curMin < x)
      s2.push(curMin);
    else
      s2.push(x);
    s1.push(x);
  };
  
  /**
   * @return {void}
   */
  MinStack.prototype.pop = function() {
    let s1 = this.s1,
        s1Len = s1.length,
        s2 = this.s2,
        s2Len = s2.length;
    
    if(s1Len === 0)
      return undefined;
    
    s2.pop();
    return s1.pop();
  };
  
  /**
   * @return {number}
   */
  MinStack.prototype.top = function() {
     let s1 = this.s1,
        s1Len = s1.length;
    if(s1.length === 0)
      return undefined;
    return s1[s1Len-1];
  };
  
  /**
   * @return {number}
   */
  MinStack.prototype.getMin = function() {
    let s2 = this.s2,
        s2Len = s2.length;
    if(s2Len === 0)
      return undefined;
    
    return s2[s2Len-1];
  };
  
  
  
  /** 
   * Your MinStack object will be instantiated and called as such:
   * var obj = new MinStack()
   * obj.push(x)
   * obj.pop()
   * var param_3 = obj.top()
   * var param_4 = obj.getMin()
   */