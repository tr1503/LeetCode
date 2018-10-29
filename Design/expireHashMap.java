import java.util.*;

public class expireHashMap {
    private class Node {
        int key;
        int value;
        int expireTime;
        Node(int key, int value, int expireTime) {
            this.key = key;
            this.value = value;
            this.expireTime = expireTime;
        }
    }

    Map<Integer,Node> map;
    TreeMap<Integer, Set<Integer>> expire;
    expireHashMap(){
        this.map = new HashMap<>();
        this.expire = new TreeMap<>();
    }

    public int get(int key, int expireTime) {
        if (!map.containsKey(key))
            return -1;
        if (map.get(key).expireTime < expireTime)
            return map.get(key).value;
        else {
            int time = map.get(key).expireTime;
            expire.get(time).remove(key);
            if (expire.get(time).isEmpty())
                expire.remove(time);
            map.remove(key);
            return -1;
        }
    }

    public void set(int key, int value, int expireTime) {
        Node node = new Node(key,value,expireTime);
        if (map.containsKey(key)) {
            int time = map.get(key).expireTime;
            expire.get(time).remove(key);
            expire.getOrDefault(expireTime,new HashSet<>()).add(key);
        }
        map.put(key,node);
    }

    public void clear(int expireTime) {
        while (expire.firstKey() >= expireTime) {
            for (int key : expire.get(expire.firstKey())) {
                map.remove(key);
            }
            expire.remove(expire.firstKey());
        }
    }
}
