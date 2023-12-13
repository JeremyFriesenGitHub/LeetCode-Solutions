/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0; // The depth of an empty tree is 0.
        }

        int leftDepth = minDepth(root.left);   // Calculate the depth of the left subtree using recursion
        int rightDepth = minDepth(root.right); // Calculate the depth of the right subtree using recursion

        // If one of the branches is empty, return the depth of the non-empty branch plus 1.
        if (leftDepth == 0) {
            return rightDepth + 1;
        }
        if (rightDepth == 0) {
            return leftDepth + 1;
        }
        
        return Math.min(leftDepth, rightDepth) + 1;
    }
}