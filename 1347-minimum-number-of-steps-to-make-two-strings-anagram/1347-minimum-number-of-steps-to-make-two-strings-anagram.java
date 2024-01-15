class Solution {
    public int minSteps(String s, String t) {
    

        Map<Character, Integer> map1 = new HashMap<Character,Integer>();
        Map<Character, Integer> map2 = new HashMap<Character,Integer>();
        
        for (int i =0;i<s.length();i++){
            char character1=s.charAt(i);
            char character2=t.charAt(i);
            if (map1.containsKey(character1) && map2.containsKey(character2)){
                int currentValue1 = map1.get(character1);
                map1.put(character1, currentValue1+1);
                int currentValue2 = map2.get(character2);
                map2.put(character2, currentValue2+1);
                }
            else if (map1.containsKey(character1) && !map2.containsKey(character2)){
                int currentValue1 = map1.get(character1);
                map1.put(character1, currentValue1+1);
                map2.put(character2,1);
            }

            else if (!map1.containsKey(character1) && map2.containsKey(character2)){
                int currentValue2 = map2.get(character2);
                map2.put(character2, currentValue2+1);
                map1.put(character1,1);
            }
            else{
                map1.put(character1,1);
                map2.put(character2,1);
            }
        }


        // System.out.println(map1);
        // System.out.println(map2);
        //count=0;
        //loop over hashmaps
        //if map2.get(character) is in map1 (i.e. map1 has that character):
            //count=count+Math.abs(value of map1 from that character - value of map2 from that character);
        //else:
            //count=cont+ value of map 2 from that character;

        //return count
       int count = 0;

        // Compare the counts in s and t
        for (Character c : map1.keySet()) {
            if (map2.containsKey(c)) {
                // If the character is in both strings, add the positive difference
                count += Math.max(map1.get(c) - map2.get(c), 0);
            } else {
                // If the character is only in s, add its count
                count += map1.get(c);
            }
        }

        return count;

    }
}