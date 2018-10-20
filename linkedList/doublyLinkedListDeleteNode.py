    def deleteNode(self, dele): 
          
        # Base Case 
        if self.head is None or dele is None: 
            return 
          
        # If node to be deleted is head node 
        if self.head == dele: 
            self.head = dele.next
  
        # Change next only if node to be deleted is NOT 
        # the last node 
        if dele.next is not None: 
            dele.next.prev = dele.prev 
      
        # Change prev only if node to be deleted is NOT  
        # the first node 
        if dele.prev is not None: 
            dele.prev.next = dele.next
