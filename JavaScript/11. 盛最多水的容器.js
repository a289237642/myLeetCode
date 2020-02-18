/** 
 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
*/
/**
 * @param {number[]} height
 * @return {number}
 */
// 方法一  O(N)
var maxArea = function(arr) {
    let low=0;
    let high=arr.length-1;
    let res=0;
    while(low<high){
        let s=(high-low)*Math.min(arr[low],arr[high]);
        res=Math.max(res,s);
        if(arr[low]<arr[high]){
            low++;
        }else{
            high--;
        }
    }
    return res
};

方法二 --时间复杂度：O(n^2)
var maxArea = function(arr) {
    let s;
    let temp=[];
    for(let low=0;low<arr.length;low++){
        for(let high=low+1;high<arr.length;high++){
            s=(high-low)*Math.min(arr[low],arr[high]);
            temp.push(s)
        }
    }
    let res=0;
    for(let i=0;i<temp.length;i++){
        res=Math.max(res,temp[i])
    }
    return res
};