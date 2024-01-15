class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length()!=word2.length()){
            return false;
        }
        //chars
        char[] chars1 = word1.toCharArray();

        Arrays.sort(chars1);

        String sortedString1 = new String(chars1);

        char[] chars2 = word2.toCharArray();

        Arrays.sort(chars2);

        String sortedString2 = new String(chars2);
        word1=sortedString1;
        word2=sortedString2;

        System.out.println(word1);
        System.out.println(word2);

        Map<Character,Integer> map1= new HashMap<Character,Integer>();
        Map<Character,Integer> map2= new HashMap<Character,Integer>();
        for (int i =0;i<word1.length();i++){
            char character1=word1.charAt(i);
            char character2=word2.charAt(i);
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

        System.out.println(map1);
        System.out.println(map2);

        ArrayList<Integer> array1 = new ArrayList<Integer>();
        ArrayList<Integer> array2 = new ArrayList<Integer>();

        //first check for same array of letters
        for (Character c: map1.keySet()){
            if (!map2.containsKey(c)&&map1.containsKey(c)){
                return false;
            }
            else{
                array1.add(map1.get(c));
                array2.add(map2.get(c));
            }
        }
        System.out.println(array1);
        System.out.println(array2);

        Collections.sort(array1);
        Collections.sort(array2);

        
        return array1.equals(array2);
    }
}