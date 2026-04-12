class Graph:
    def __init__(self):
        self.adjust={}
    def add_vertex(self,vertex):
        if vertex not in self.adjust:
            self.adjust[vertex]=[]
    def add_edge(self,src,dest):
        #    Ensure BOTH nodes are created as keys in the dictionary if a node has
        # no child then it also add to the object 
        # if i do not write the self.add_vertex(dest) then it not create as a key
           self.add_vertex(src)
           self.add_vertex(dest)
        #    for on way connection
           self.adjust[src].append(dest)
        #    self.adjust[dest].append(src)
    def display(self):
        #  print(self.adjust.items())
        for node,dest in self.adjust.items():
             print(f"node:{node},keys:{dest}")
    def depth_first_search(self,src):
         visited=[]
         stack=[src]
         while stack:
              v=stack.pop()
              if v not in visited:
                   print(v,end=" => ")
                   visited.append(v)
              for neighbar in self.adjust[v]:
                   if neighbar not in visited:
                        stack.append(neighbar)
            

graph=Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "F")
graph.display()
graph.depth_first_search("A")