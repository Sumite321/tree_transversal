
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
        self.bf_nodes = []
        self.parents = []
        self.df_nodes = []
        self.root = None
        self.make_tree()

    def make_tree(self):
        parents,edges = self.get_ids_and_edges()
  

        for x in parents: # iterates every parent to find for child
            increment2 = 0
            parent = Node(x)
            parent.set_parent(self.root)
            for y in edges:
                if int(edges[increment2][0:1]) == int(x):
                    child = Node(edges[increment2][2:4])
                    child.set_parent(parent) # set current node as parent 
                    parent.add_child(child) # add child to current node
                    if parent.get_parent() == None:
                        self.root = parent
 #                   self.bf_nodes.append(child)
                increment2 += 1 
            self.parents.append(child.get_parent())

        
       # self.bf_nodes.insert(0,self.root)
        self.BFS_method(self.parents)

    



        
            
    def BFS_method(self,node):
 
        for x in node:
            if type(x.get_children())==list:
                self.bf_nodes.append(x)
                self.BFS_method(x.get_children())
    
        ## return the created list of nodes
        return self.bf_nodes

    def get_BFS(self):
        
        
        
        return self.bf_nodes

    def get_all_nodes_DF(self):


        self.parents.remove(self.root)# root removed from list
        inc = 0
        for y in reversed(self.parents):
            inc2 = 0
            self.df_nodes.append(y)
            for x in reversed(y.get_children()):
                self.df_nodes.append(x)
                inc2 += 1
            inc += 1
        self.df_nodes.insert(0,self.root) # root added back
        
        ## return the created list of nodes
      
        return self.df_nodes

    def get_ids_and_edges(self):
        """read the tree description file and retrieve the nodes 
        and edges in between of them"""
        f = open(self.description_file)
        edges = [] #edges
        parents = []
        increment = 0
    
        # loop throught the file
        for line in f:  # add lines to the temporary list
            edges.append(line.rstrip("\n")) # add tmp list to the main edge list
            parents.append(int(edges[increment][0:1])) # add parent to the list
            increment += 1

        parents = set(parents)
        return parents,edges

  
"""This is the code used for testing.
"""
tree_description = "tree_description_01.txt"
tree = Tree(tree_description)

bf_nodes = tree.get_BFS()
print("bf_nodes: {}".format(bf_nodes))

df_nodes = tree.get_all_nodes_DF()
print("df_nodes: {}".format(df_nodes))




