/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isBalanced(root: TreeNode | null): boolean {
    function traverse(root: TreeNode | null): number{
        if (root === null) return 0;

        let left = traverse(root.left);
        if(left === -1) return left;

        let right = traverse(root.right);
        if(right === -1) return right;

        return Math.abs(left - right) > 1 ? -1 : Math.max(left, right) + 1;
    }

    return traverse(root) !== -1
};