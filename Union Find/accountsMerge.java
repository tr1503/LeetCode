// Use union find to union each email to its owner
// The user id is the index of each user_name and emails in the array
// Create two hashmaps, one for each email used by different user id 
// Another hashmap's key is user id and value is a set contains the email with this user id
// Check https://www.jiuzhang.com/solution/accounts-merge/
class Solution {
    Map<Integer,Integer> father;
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        father = new HashMap<>();
        
        // union
        Map<String,List> emailToId = getEmailToId(accounts);
        for (String email : emailToId.keySet()) {
            List<Integer> ids = emailToId.get(email);
            for (int i = 1; i < ids.size(); i++) {
                union(ids.get(i),ids.get(0));
            }
        }
        
        // merge accounts
        Map<Integer, Set<String>> idToEmail = getIdToEmail(accounts);
        List<List<String>> mergedAccounts = new ArrayList<>();
        for (Integer id : idToEmail.keySet()) {
            List<String> sortedEmails = new ArrayList(idToEmail.get(id));
            Collections.sort(sortedEmails);
            sortedEmails.add(0,accounts.get(id).get(0));
            mergedAccounts.add(sortedEmails);
        }
        
        return mergedAccounts;
    }
    
    private Map<String,List> getEmailToId(List<List<String>> accounts) {
        Map<String, List> emailToId = new HashMap<>();
        for (int id = 0; id < accounts.size(); id++) {
            List<String> account = accounts.get(id);
            for (int i = 1; i < account.size(); i++) {
                List<Integer> ids = emailToId.getOrDefault(account.get(i),new ArrayList<Integer>());
                ids.add(id);
                emailToId.put(account.get(i),ids);
            }
        }
        return emailToId;
    }
    
    private Map<Integer, Set<String>> getIdToEmail(List<List<String>> accounts) {
        Map<Integer, Set<String>> idToEmail = new HashMap<>();
        for (int id = 0; id < accounts.size(); id++) {
            int root_id = find(id);
            Set<String> emailSet = idToEmail.getOrDefault(root_id, new HashSet<String>());
            List<String> account = accounts.get(id);
            for (int i = 1; i < account.size(); i++) {
                emailSet.add(account.get(i));
            }
            idToEmail.put(root_id, emailSet);
        }
        return idToEmail;
    }
    
    private int find(int id) {
        List<Integer> path = new ArrayList<>();
        while (father.containsKey(id)) {
            path.add(id);
            id = father.get(id);
        }
        
        for (Integer i : path) {
            father.put(i, id);
        }
        return id;
    }
    
    private void union(int id1, int id2) {
        int root1 = find(id1);
        int root2 = find(id2);
        if (root1 != root2) 
            father.put(root1,root2);
    }
}
