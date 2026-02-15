/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let map = new Set(nums);

    if(nums.length !== map.size) return true
    return false
};