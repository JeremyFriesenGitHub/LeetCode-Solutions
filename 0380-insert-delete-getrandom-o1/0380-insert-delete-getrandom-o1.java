class RandomizedSet {
    
    private Map<Integer,Integer> map;
    private Random random;
    private ArrayList<Integer> list;
    
    
    public RandomizedSet() {
        this.map= new HashMap<Integer,Integer>();
        this.random = new Random();
        this.list = new ArrayList<Integer>();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)){
            return false;
        }
        map.put(val, list.size());
        list.add(val);
        return true;
    }
    
    public boolean remove(int val) {
         if (!map.containsKey(val)) {
            return false;
        }

        int index = map.get(val);
        int lastElement = list.get(list.size() - 1);
        list.set(index, lastElement);
        map.put(lastElement, index);
        list.remove(list.size() - 1);
        map.remove(val);
        return true;

    }
    
    public int getRandom() {
        return list.get(random.nextInt(list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */