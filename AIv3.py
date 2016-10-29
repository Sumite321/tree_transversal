class Node(object):
    def __init__(self,id):
        """
        Default constructor

        Parameters
        ----------
        id : int
        """
        self.id = id
        self.children = []
        self.parent=None

    def set_parent(self,parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def add_child(self,child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def set_content(content):
        self.content = content

    def get_content(content):
        return self.content

    def __str__(self):
        child_ids = [c.id for c in self.children]
        if self.get_parent()==None:
            ## More info can be useful for testing
            return "[ROOT {}->{}]".format(self.id,child_ids)
            return "({})".format(self.id)
        else:
            return "[{}->{}->{}]".format(self.parent.id,self.id,child_ids)
            return "({})".format(self.id)

    def __repr__(self):
        return self.__str__()
    

class Tree(object):
    
    
    def __init__(self,description_file):
        self.description_file = description_file
        self.make_tree()

    def make_tree(self):
        ids, edges = self.get_ids_and_edges() # this makes it easier but not strictly required
        
        #all nodes existing in the tree created 
        root = Node(ids[0]) # root
        left_sub = Node(ids[1]) 
        right_sub = Node(ids[2])
        node3 = Node(ids[3])
        node4 = Node(ids[4])
        node5 = Node(ids[5])
        node6 = Node(ids[6])

        root.add_child(left_sub) # add left subtree to root # child = 1
        root.add_child(right_sub) # add right subtree to root child = 1,2


        left_sub.set_parent(root) # left subtree becomes the parent
        left_sub.add_child(node3) # add child to left subtree child = 1,2,3
        left_sub.add_child(node4) # child to left subtree child = 1,2,3,4

        node3.set_parent(left_sub)
        node4.set_parent(left_sub)
        
        right_sub.set_parent(root)
        right_sub.add_child(node5) # child = 1,2,3,4,5
        right_sub.add_child(node6) # child = 1,2,3,4,5,6
        
        node5.set_parent(right_sub)
        #none5.add_child(None)
        node6.set_parent(right_sub)
        
##        print(root)
##        print(left_sub)
##        print(node3)
##        print(node4)
##        print(right_sub)
##        print(node5)
##        print(node6)
##        print(root.children)

        ids1 = [root,left_sub,right_sub,node3,node4,node5,node6]
        return ids1
        
    
    def get_all_nodes_BF(self):
        bf_nodes = []
        
            
             
        ## complete the code here; this is required
        ## return the created list of nodes
        #return bf_nodes

    def get_all_nodes_DF(self):
        ## fill the list with all nodes in Depth-First order
        df_nodes = []
        ## complete the code here; this is required

        ## return the created list of nodes
        return df_nodes

    def get_ids_and_edges(self):
        """read the tree description file and retrieve the nodes 
        and edges in between of them"""
        f = open(self.description_file,"r")
        ids = [] #nodes
        edges = [] #edges
        tmp = [] # list for temp
        parents = []
        children = [] # list for chilren
        increment = 0

        # loop throught the file
        for line in f: 
            tmp = [line.rstrip("\n")] # add lines to the temporary list
            edges.append(tmp) # add tmp list to the main edge list
            # format :  (edge) -> [parent][child]
            child = edges[increment][0][2:3] # get the child node in the edge
            parent = int(edges[increment][0][0:1]) # get the parent node
            if parent not in parents: # check for duplicated parent nodes in parent list
                parents.append(int(parent)) # add parent to the list
            children.append(child) # add children to list
            increment += 1
        

        # loop to find childs from parents 
        for x in parents: # iterates every parent to find for child
            if x not in ids:
                ids.append(int(x)) # check if parent is not repeated in ID list
            increment2 = 0
            print("parent",x)
            for y in edges:
                if int(edges[increment2][0][0:1]) == int(x):
                    ids.append(int(edges[increment2][0][2:3])) # ID list in BF order
                    print("Child",edges[increment2][0][2:3])
                increment2 += 1

            
         
##        print(edges)
##        print(ids)

            
        ## complete the code her

            
        return ids,edges
  
"""This is the code used for testing. 
DO NOT MODIFY.
"""
tree_description = "tree_description_01.txt"
tree = Tree(tree_description)
bf_nodes = tree.get_all_nodes_BF()
print("bf_nodes: {}".format(bf_nodes))

df_nodes = tree.get_all_nodes_DF()
print("df_nodes: {}".format(df_nodes))






"""This partial code is clearly not doing anything but provides the complete code for the Node class and partial code for the Tree class. In the end, your code should return the following:
bf_nodes: [(0), (1), (2), (3), (4), (5), (6)]
df_nodes: [(0), (2), (6), (5), (1), (4), (3)]
I will test the code with another tree description file."""
