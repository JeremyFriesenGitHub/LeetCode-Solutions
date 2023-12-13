class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        //i have an array of strings garbage[i] at ith house.
        //garbage[i]='Metal' or 'Paper' or 'Glass'
        //picking up one metal or paper or glass = 1 minute

        //travel array = , = time between houses
        //thats a good one
        //three trucks approach

        
        //calculate what garbage to pick up from end to begginng, then account for traveling
        //to calculate metal garbage route: 
        //need to iterate from last house to first house
        //once you find garbage in a house that isnt the first one:
        //increment minute counter for every instance of letter in string
        //once done, if i am traveling to house i, time to travel = travel[i]
        //travel[i]+minutes = minutes
        //repeat until house[0];
    int lastMetal = -1, lastPaper = -1, lastGlass = -1;
    int metalTime = 0, paperTime = 0, glassTime = 0;

    // Find the last occurrence of each garbage type
    for (int i = garbage.length - 1; i >= 0; i--) {
        if (garbage[i].contains("M") && lastMetal == -1) lastMetal = i;
        if (garbage[i].contains("P") && lastPaper == -1) lastPaper = i;
        if (garbage[i].contains("G") && lastGlass == -1) lastGlass = i;
    }

    // Calculate collection time for each garbage type
    for (int i = 0; i <= lastMetal; i++) {
        metalTime += garbage[i].length() - garbage[i].replace("M", "").length();
        if (i < lastMetal) metalTime += travel[i];
    }
    for (int i = 0; i <= lastPaper; i++) {
        paperTime += garbage[i].length() - garbage[i].replace("P", "").length();
        if (i < lastPaper) paperTime += travel[i];
    }
    for (int i = 0; i <= lastGlass; i++) {
        glassTime += garbage[i].length() - garbage[i].replace("G", "").length();
        if (i < lastGlass) glassTime += travel[i];
    }

    // Return total time
    return metalTime + paperTime + glassTime;

    }
}