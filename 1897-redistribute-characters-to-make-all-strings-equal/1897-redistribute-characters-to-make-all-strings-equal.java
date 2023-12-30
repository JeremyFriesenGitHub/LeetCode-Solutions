class Solution {
    public boolean makeEqual(String[] words) {
        Map<Character, Integer> map = new HashMap<Character,Integer>();  
        for (int i=0;i<words.length;i++){
            for (int j=0;j<words[i].length();j++){
                char character = words[i].charAt(j);
                if (map.containsKey(character)){
                    int currentValue = map.get(character);
                    map.put(character, currentValue+1);
                }
                else{
                    map.put(character, 1);
                }
            }
        }
        
        //check every character's value can be evenly distributed among the differents words
        for (Integer value : map.values()) {
            if(value % words.length!=0){
                // System.gc();
                return false;
            }
        }
        // System.gc();
        return true;
    }
}