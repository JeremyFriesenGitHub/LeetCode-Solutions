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
    public List<Integer> postorderTraversal(TreeNode root) {
        ArrayList<Integer> x = new ArrayList<Integer>();
        if(root !=null){
            x.addAll(postorderTraversal(root.left));
            x.addAll(postorderTraversal(root.right));
            x.add(root.val);
            return x;
        }
        else{
            return x;
        }
    }
}