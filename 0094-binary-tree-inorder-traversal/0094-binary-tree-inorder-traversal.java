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
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> x = new ArrayList<Integer>();
        if(root !=null){
            x.addAll(inorderTraversal(root.left));
            x.add(root.val);
            x.addAll(inorderTraversal(root.right));
            return x;
        }
        else{
            return x;
        }
    }
}