/** 
 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
*/

var moveZeroes = function (nums) {
    var i = 0,
        j = 1;
    while (i < nums.length && j < nums.length) {
        if (nums[i] === 0 && nums[j] !== 0) {
            nums[i] = nums[j];
            nums[j] = 0;
            i++; j++;
        } else if (nums[i] === 0 && nums[j] === 0) {
            j++;
        } else if (nums[i] !== 0 && nums[j] !== 0) {
            i += 2;
            j += 2;
        } else {
            i = j;
            j++;
        }
    }
};
