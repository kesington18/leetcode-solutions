/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let indexPos = 0;

    for (let ind = 0; ind < nums.length; ind++){
        if(nums[ind] !== 0){
            nums[indexPos++] = nums[ind];
        }
    }

    while(indexPos < nums.length){
        nums[indexPos++] = 0;
    }

    return nums;
};