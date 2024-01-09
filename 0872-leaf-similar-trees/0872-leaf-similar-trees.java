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
    //break down to collect leaves of one tree
    //use method for both trees
    //return
    void collectLeafNodes(TreeNode node, List<Integer> leaves) {
    if (node != null) {
        if (node.left == null && node.right == null) {
            leaves.add(node.val);
        } else {
            collectLeafNodes(node.left, leaves);
            collectLeafNodes(node.right, leaves);
        }
    }
}

boolean leafSimilar(TreeNode root1, TreeNode root2) {
    List<Integer> leaves1 = new ArrayList<>();
    List<Integer> leaves2 = new ArrayList<>();
    collectLeafNodes(root1, leaves1);
    collectLeafNodes(root2, leaves2);
    return leaves1.equals(leaves2);
}
}