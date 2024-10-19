#Time Complexity: O(n) — where n is the number of nodes in the tree, as each node is processed once.
#Space Complexity: O(n) — space is used by the queue (q) and the result list, which in the worst case could hold all nodes at a given level of the tree.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #List in which all nodes of a level are sotred in as another list
        result=[]
        #Base Case
        if(root==None):
            return result #Empty List
        #Assign a deque: A queue which can add and remove elements from both ends
        q = deque([root])
        while len(q)!=0:
            size = len(q) #Size of nodes in queue of each level
            level=[] #List in which all nodes of a level are stored
            #Loop to add nodes to queue of at each level
            for i in range(size):
                curr = q.popleft() 
                level.append(curr.val)
                #Add left child of current node to queue
                if(curr.left!=None):
                    q.append(curr.left)
                #Add right child of current node to queue
                if(curr.right!=None):
                    q.append(curr.right)
            #Append level list in the result
            result.append(level)
        return result