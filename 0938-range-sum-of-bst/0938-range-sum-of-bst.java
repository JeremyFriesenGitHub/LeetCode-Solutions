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
    public int rangeSumBST(TreeNode root, int low, int high) {
        //only issue is that high and low is a range
        //traverse the whole tree
        //compare val if in range
        //add val if in range
        //return sum

        int sum=0;
        if(root !=null){
            if (root.val > low){
                sum =sum+rangeSumBST(root.left,low,high);
            }
            if (root.val>=low && root.val<=high){
                sum=sum+root.val;
            }
            
            if (root.val<high){
                sum =sum+rangeSumBST(root.right,low,high);
            }
        }
        return sum;
    }
}