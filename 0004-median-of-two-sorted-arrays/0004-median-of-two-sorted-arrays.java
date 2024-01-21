class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        //merge the array and get the median

        //problem is merge two sorted arrays (can add, then sort, but would take nlogn)
        //one pointer, two arrays, only issue is the index numberings
        //will create two index variables that are to compare each other
        //and increment

        //found O(n + m) solution, but this isnt log n+m
        
        //have to use binary search to make faster

        //this program uses 3rd array to merge the sorted arrays in (O(n+m) time, where n is length of 1st array and m the 2nd)
        //inits 3rd array by comparing valid indexes and sorting them into 3rd array

        int length1 = nums1.length;
        int length2 = nums2.length;

        int[] nums3 = new int[length1+length2];

        int index1=0;
        int index2=0;

        for (int i = 0; i < nums3.length; i++) {
            if (index1 < nums1.length && (index2 >= nums2.length || nums1[index1] <= nums2[index2])) {
                nums3[i] = nums1[index1];
                index1++;
            } else if (index2 < nums2.length) {
                nums3[i] = nums2[index2];
                index2++;
            }
        }

        //math formula for median
        double median;
        if (nums3.length % 2 == 0){median = ((double)nums3[nums3.length/2] + (double)nums3[nums3.length/2 - 1])/2;
        }
        else{
            median = (double) nums3[nums3.length/2];
            }
        return median;
    }
}