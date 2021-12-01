

    def levelOrder(self,root):
        #Write your code here
        queue = []
        if root != None:
            queue.append(root)
        
        while len(queue)>0:
            node = queue.pop(0)
            print(node.data, end=' ')
            
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            
        

