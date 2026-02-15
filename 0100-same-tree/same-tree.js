/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    // check if both nodes are null
    if (p === null && q === null) {
         return true;
    }
    // check if one node is null and the other isnt and subtrees on the left hnd side are the same
    if (p === null || q === null || p.val !== q.val) {
        return false ;
    }
    
// check right trees are the same and left subtrees are the same 
let sameLeftTree = isSameTree(p.left, q.left);

let sameRightTree = isSameTree(p.right, q.right);

return sameLeftTree && sameRightTree
};