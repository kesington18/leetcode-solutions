/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let numsLength = nums.length;
    let expectedValue = (numsLength * (numsLength + 1))/ 2;
    let actual = nums.reduce((a,b) => a + b, 0);
    return expectedValue - actual;
};