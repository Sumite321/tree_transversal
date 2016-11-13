"""
@SumiteR


Version 7 - HpEnd

* re-designed and re-invented version 5
* objects are no longer instantiated using lists
* self.obj removed
* added new feature - Auto Root; Automatically finds the root
* new algorithm implemented; objects are instantiated, assigned and sorted
using a single loop
* removed lists (ID,tmp)
* removed unecessary loops(IDs,inst)
* get_content and set_content no longer used
* major bug fixes


*********************************************************
Older version
Version 5.1 - RollBX

* rollback to version 5

Version 6.2

* temporary bug changed to permanently fixed
* minor pointer fixes


Version 6.1

* Bug fixed (temporary)
* pointer added (set_content -> self.id)
* get_all_nodes_<method> now returns id node with content


Version 6 - ADvd

* New algorithm implemented
* Added ability to transverse a tree with unlimited nodes
* set_content and get_content fixed
* bf_nodes method now uses get_content
* Added ability to read an unordered tree and automatically sort it
* Create objects dynamically

Version 5

* Implemented "linked list" style tree tranversal
* instantiation happens using lists

Version 4 - Majrx

* skips version 3 due to major updates
* nodes are now instantiated dynamically accessing a list
* method to sort using BFS implemented
* tree is built using BFS
* new effecient way to find for ids and edges
* new logical method to recognize parents and edges from txt files


Version 2

* fully new algorithm; 2 classes implemented
* Node class gets ID and nodes from txt file and uses the methods
* Tree class reads txt file, builds and sorts the tree
* Nodes created manually



Version 1 - Initial release

* Initial algorithm reads the file, extrats the ids and edges from it
* Uses BFS and returns the nodes in order

"""
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
        self.bf_nodes = []
        self.parents = []
        self.df_nodes = []
        self.root = None
        self.make_tree()

    def make_tree(self):
        parents,edges = self.get_ids_and_edges() # this makes it easier but not strictly required
  

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
                    self.bf_nodes.append(child)
                increment2 += 1 
            self.parents.append(child.get_parent())

        
        self.bf_nodes.insert(0,self.root)
            
    def get_all_nodes_BF(self):
        """
        make_tree() uses Level order which is similar to the BF search,
        therefore bf_nodes list is appended simultaneous with the loop.
        """
        ## complete the code here; this is required
        ## return the created list of nodes
        return self.bf_nodes

    def get_all_nodes_DF(self):
        ## fill the list with all nodes in Depth-First order
        
        ## complete the code here; this is required

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
        
    ## complete the code here
        # loop throught the file
        for line in f:  # add lines to the temporary list
            edges.append(line.rstrip("\n")) # add tmp list to the main edge list
            parents.append(int(edges[increment][0:1])) # add parent to the list
            increment += 1

        parents = set(parents)
        return parents,edges
  
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
