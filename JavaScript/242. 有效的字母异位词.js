/***
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

 /**
 * 1. 排序法
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) {
      return false;
    }

    var arrS = s.split('').sort();
    var arrT = t.split('').sort();

    return arrS.join('') === arrT.join('');
};

/**
 * 2. Hash
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    var map = new Map();
    var arrS = s.split('');
    var arrT = t.split('');

    if (arrS.length !== arrT.length) {
      return false;
    }

    for (var value of arrS) {
      var count = map.get(value);

      if (count) {
        map.set(value, count + 1);
      } else {
        map.set(value, 1);
      }
    }
};