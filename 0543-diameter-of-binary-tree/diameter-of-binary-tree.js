/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    let maxDiameter = 0;
    // calculate the height of the node 
    const getHeight = (node) => {
        if (node === null) return 0;
    //find the height of the left subtree
    const left = getHeight(node.left);
    // find the height of the right subtree
    const right = getHeight(node.right);

    //check if the nodes path is the longest ,if it is update the diameter and then return the height of the node 
    maxDiameter = Math.max(maxDiameter, left + right);

    return 1+ Math.max(left, right);
    };

    getHeight(root);
    return maxDiameter;

};