public void deleteLastNode(TreeNode root){
    // base case
    if(root == null) return;
     
    deleteLastNodeHelper(root);
}
 
private TreeNode deleteLastNodeHelper(TreeNode root){
    if(root == null) return null;
     
    if(root.left == null && root.right == null){
        // find the last node 
        return null;
    }
     
    int leftHight = calHeight(root.left);
    int rightHight = calHeight(root.right);
     
    if(leftHight > rightHight){
        // the last node must in left subtree
        root.left = deleteLastNodeHelper(root.left);
    }else{
        // the last node must in right subtree
        root.right = deleteLastNodeHelper(root.right);
    }
     
    return root;
}
 
// calculate the height of the left most branch
private int calHeight(TreeNode root){
    if(root == null) return 0;
     
    int height = 1;
    while(root.left != null){
        root = root.left;
        height++;
    }
    return height;
}
