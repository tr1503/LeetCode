public void validTree(TreeNode root){
        if(root == null) return;
         
        Deque<TreeNode> queue = new ArrayDeque<>();     
        // if a node has been visited twice, then delete that edge
        Set<TreeNode> visited = new HashSet<>();
         
        queue.offer(root);
         
        while(!queue.isEmpty()){
            TreeNode cur = queue.poll();
             
            if(cur.left != null){
                if(visited.contains(cur.left)){
                    // left child has been pointed by other node
                    // delete that edge
                    cur.left = null;
                }else{
                    visited.add(cur.left);
                    queue.offer(cur.left);
                }
            }
             
            if(cur.right != null){
                if(visited.contains(cur.right)){
                    // right child has been pointed by other node
                    // delete that edge
                    cur.right = null;
                }else{
                    visited.add(cur.right);
                    queue.offer(cur.right);
                }
            }
        }   
    }
