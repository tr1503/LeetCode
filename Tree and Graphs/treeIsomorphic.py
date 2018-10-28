def isIsomorphic(n1, n2): 
      
    # Both roots are None, trees isomorphic by definition 
    if n1 is None and n2 is None: 
        return True
  
    # Exactly one of the n1 and n2 is None, trees are not 
    # isomorphic 
    if n1 is None or n2 is None: 
        return False
  
    if n1.data != n2.data : 
        return False
    # There are two possible cases for n1 and n2 to be isomorphic 
    # Case 1: The subtrees rooted at these nodes have NOT 
    # been "Flipped". 
    # Both of these subtrees have to be isomorphic, hence the && 
    # Case 2: The subtrees rooted at these nodes have 
    # been "Flipped" 
    return ((isIsomorphic(n1.left, n2.left)and 
            isIsomorphic(n1.right, n2.right)) or
            (isIsomorphic(n1.left, n2.right) and 
            isIsomorphic(n1.right, n2.left)) 
            
