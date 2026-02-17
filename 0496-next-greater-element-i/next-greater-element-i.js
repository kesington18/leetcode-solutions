/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
    let res = []
    let getInd;
    let newInd;
    for (let num = 0; num < nums1.length; num++){
        getInd = nums2.includes(nums1[num])
        newInd = nums2.indexOf(nums1[num])
        
        let nextGreater = -1

        for (let i = newInd + 1; i < nums2.length; i++){
            if(nums2[i] > nums2[newInd]){
                nextGreater = nums2[i]
                break
            }
            
        }
        res.push(nextGreater)
        // console.log(newInd, getInd)
    }
    // console.log(res)
    return res;
}