class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
       HashMap<Integer,Integer> winners = new HashMap<Integer,Integer>();
       HashMap<Integer,Integer> losers = new HashMap<Integer,Integer>();
    //    System.out.println(matches.length);
       for (int i=0;i<matches.length;i++){
           int winnerPlayer = matches[i][0];
           int loserPlayer = matches[i][1];
           if (winners.containsKey(winnerPlayer) && losers.containsKey(loserPlayer)){
                int currentValue1 = winners.get(winnerPlayer);
                winners.put(winnerPlayer, currentValue1+1);
                int currentValue2 = losers.get(loserPlayer);
                losers.put(loserPlayer, currentValue2+1);
                }
            else if (winners.containsKey(winnerPlayer) && !losers.containsKey(loserPlayer)){
                int currentValue1 = winners.get(winnerPlayer);
                winners.put(winnerPlayer, currentValue1+1);
                losers.put(loserPlayer,1);
            }

            else if (!winners.containsKey(winnerPlayer) && losers.containsKey(loserPlayer)){
                int currentValue2 = losers.get(loserPlayer);
                losers.put(loserPlayer, currentValue2+1);
                winners.put(winnerPlayer,1);
            }
            else{
                winners.put(winnerPlayer,1);
                losers.put(loserPlayer,1);
            }
       }

       System.out.println(winners);
       System.out.println(losers);
       
       //not lose any match is if in only winners, has to check if exist in winners and not exist in losers
       
       //lose one match if only has value == 1 in losers, only need to check losers and has value ==1 in losers
       List<List<Integer>> outerArray = new ArrayList<>();
       List<Integer> innerArray = new ArrayList<>();
       List<Integer> innerArray2 = new ArrayList<>();
       for (Integer winner: winners.keySet()){
            if (!losers.containsKey(winner)&&winners.containsKey(winner)){
                innerArray.add(winner);
            }
       }
       Collections.sort(innerArray);
       outerArray.add(innerArray);

       for (Integer loser: losers.keySet()){
           int losses = losers.get(loser);
           if(losses==1){
               innerArray2.add(loser);
           }
       }
       Collections.sort(innerArray2);
       outerArray.add(innerArray2);
       return outerArray;

    }
}