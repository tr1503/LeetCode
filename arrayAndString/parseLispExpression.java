class Solution {
    public int evaluate(String expression) {
        return calc(expression,new HashMap<>());
    }
    private int calc(String expr, Map<String,Integer> parent){
        if(expr.charAt(0)!='('){
            if(Character.isDigit(expr.charAt(0))||expr.charAt(0)=='-'){
                //this is a single number so return it
                return Integer.parseInt(expr);
            }
            else{
                //this is a single variable so return it
                return parent.get(expr);
            }
        }
        //remove the )
        String s = expr.substring(1,expr.length()-1);
        char c = s.charAt(0);
        Map<String,Integer> map = new HashMap<>();
        map.putAll(parent);
        List<String> tokens = parse(s);
        if(c=='a'){
            return calc(tokens.get(1),map) + calc(tokens.get(2),map);
        }
        else if(c=='m'){
            return calc(tokens.get(1),map)*calc(tokens.get(2),map);
        }
        else{
            //let statement
            for(int i=1; i<tokens.size()-1;i+=2){
                map.put(tokens.get(i),calc(tokens.get(i+1),map));
            }
            return calc(tokens.get(tokens.size()-1),map);
        }
    }
    //The first argument will always be the command (add, etc.) returns a list of the parameters, either single elements or clauses on this level
    private List<String> parse(String s){
        int open = 0;
        List<String> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<s.length();++i){
            char c = s.charAt(i);
            if(c=='('){
                ++open;
            }
            else if(c==')'){
                --open;
            }
            if(open==0 && c==' '){
                res.add(sb.toString());
                sb = new StringBuilder();
            }
            else{
                sb.append(c);
            }
        }
        if(sb.length()>0){
            res.add(sb.toString());
        }
        return res;
    }
}
