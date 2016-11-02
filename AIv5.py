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

    def set_content(self,content):
        self.content = content  

    def get_content(self):
        return self.content

    def __str__(self):
        child_ids = [c.id for c in self.children]
        if self.get_parent()==None:
            ## More info can be useful for testing
            #return "[ROOT {}->{}]".format(self.id,child_ids)
            return "({})".format(self.id)
        else:
            #return "[{}->{}->{}]".format(self.parent.id,self.id,child_ids)
            return "({})".format(self.id)

    def __repr__(self):
        return self.__str__()
    

class Tree(object):
    
    
    def __init__(self,description_file):
        self.description_file = description_file
        self.obj = []
        self.make_tree()

    def make_tree(self):
        ids, parents,edges = self.get_ids_and_edges() # this makes it easier but not strictly required

        self.obj = ["a","b","c","d","e","f","g"]
        inc = 0
        for x in self.obj:
            self.obj[inc] = Node(ids[inc])
            #print(self.obj[inc])
            inc += 1
            
        increment = 0
        childinc = 1
        for x in parents: # iterates every parent to find for child
            print("parent",x)
            current = self.obj[increment] # current node
            increment2 = 0
            for y in edges:
                if int(edges[increment2][0][0:1]) == int(x):
                    current.add_child(self.obj[childinc]) # add child to current node
                    self.obj[childinc].set_parent(current) # set current node as parent
                    #print(self.obj[increment])
                    print("Child",edges[increment2][0][2:3])
                    childinc += 1
                increment2 += 1
            increment += 1
    
        
    def get_all_nodes_BF(self):
        bf_nodes = []
        
        for x in self.obj:
            bf_nodes.append(x)
        
            
             
        ## complete the code here; this is required
        ## return the created list of nodes
        return bf_nodes

    def get_all_nodes_DF(self):
        ## fill the list with all nodes in Depth-First order
        df_nodes = []
        ## complete the code here; this is required

        ## return the created list of nodes
        return df_nodes

    def get_ids_and_edges(self):
        """read the tree description file and retrieve the nodes 
        and edges in between of them"""
        f = open(self.description_file)
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
            #print("parent",x)
            for y in edges:
                if int(edges[increment2][0][0:1]) == int(x):
                    ids.append(int(edges[increment2][0][2:3])) # ID list in BF order
                    #print("Child",edges[increment2][0][2:3])
                increment2 += 1

            
         
##        print(edges)
##        print(ids)
            
        ## complete the code her

            
        return ids,parents,edges
  
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
