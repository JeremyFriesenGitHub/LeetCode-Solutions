class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {

        //init 
        int numRows = points.length;
        int maxDistance=-1;
        int[] xCoordinates = new int[numRows];

        //put xCoordinates into 1D array 
        for (int i = 0; i < numRows; i++) {
            xCoordinates[i] = points[i][0];
        }

        //sort all xCoordinates
        Arrays.sort(xCoordinates);
        
        //get maxDistance from the difference of side-by-side xCoordinates
        for (int j=0;j< xCoordinates.length;j++){
            if (j+1<xCoordinates.length){
                int k = j+1;
                if(maxDistance<(xCoordinates[k]-xCoordinates[j])){
                    maxDistance=xCoordinates[k]-xCoordinates[j];
                }
            }
        }

        //return maxDistance
        return maxDistance;
    }
}