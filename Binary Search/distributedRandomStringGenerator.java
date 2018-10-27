import java.util.*;
public class getWithRandom {
    public static void main(String[] args){
        Map<String, Double> myMap = new HashMap<>();
        myMap.put("a", 0.55);
        myMap.put("b", 0.1);
        myMap.put("c", 0.2);
        myMap.put("d", 0.15);
        DistributedRandomStringGenerator q = new DistributedRandomStringGenerator(myMap);
        List<String> ans = new ArrayList<>();
        for(int i=0; i<10000; i++)
            ans.add(q.getRandomString());
 // verify our result
        Map<String, Integer> countMap = new HashMap<>();
        for(String n : ans)
            countMap.put(n, 1 + countMap.getOrDefault(n, 0));
 
        for(Map.Entry<String, Integer> entry : countMap.entrySet())
            System.out.println(entry.getKey() + ": " + ((double)entry.getValue() / ans.size()));
    }
 
 
}
 
class DistributedRandomStringGenerator{
    private Random rand;
    private double[] cumulative;
    private String[] sArray;
    DistributedRandomStringGenerator(Map<String, Double> probMap){
        rand = new Random();
        cumulative = new double[probMap.size()];
        sArray = new String[probMap.size()];
        int i = 0;
        for(Map.Entry<String, Double> entry : probMap.entrySet()){
            // we don't want those string whose probability is less than or equal to zero
            if(entry.getValue() > 0){
                sArray[i] = entry.getKey();
                cumulative[i] = entry.getValue() + (i > 0 ? cumulative[i - 1] : 0);
                i++;
            }
        }
    }
 
    String getRandomString(){
        double r = rand.nextDouble();
        int index = binarySearch(r);
        return sArray[index];
    }
 
    private int binarySearch(double r){
        int low = 0, high = cumulative.length - 1;
        while(low + 1 < high){
            int mid = low + ((high - low) >> 1);
            if(cumulative[mid] == r)
                return mid;
            else if(cumulative[mid] < r)
                low = mid;
            else
                high = mid;
        }
        if(r > cumulative[low])
            return high;
        return low;
    }
}
