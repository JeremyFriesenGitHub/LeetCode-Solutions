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
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> x = new ArrayList<Integer>();
        if (root!=null){
        x.add(root.val);
        x.addAll(preorderTraversal(root.left));
        x.addAll(preorderTraversal(root.right));
       
        return x;
        }else{
            return x;
        }
    }
}