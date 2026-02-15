/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let set = new Set(nums1);
    let res = [];

    for (let n of nums2) {
        if (set.delete(n)) {
            res.push(n);
        }
    }
    return res;
};