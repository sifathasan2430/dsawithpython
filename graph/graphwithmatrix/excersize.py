class Graph:
    def __init__(self,vertex):
        self.mat=[[0]*vertex for i in range(vertex)]
        self.size=vertex
    def add_edge(self,src,des):
        # if 0<=src<=self.size and 0<=des<=self.size: index start from 0 so =self.size is wrong
        if 0<=src<self.size and 0<=des<self.size:
            print("hit")
            self.mat[src][des]=1
            self.mat[src][des]=1
        else:
            print("invalid number")

    def display(self):
        for row in self.mat:
            
            print(''.join(list(map(str,row))))
    def depth_first_traversal(self,src):
        stack=[src]
        visited=[False]*self.size
        while stack:
            v=stack.pop()
            if visited[v]==False:
                print(v)
                visited[v]=True
            for neigbor in range(self.size):
                if self.mat[v][neigbor]==1 and visited[neigbor]==False:
                    stack.append(neigbor) 

graph=Graph(6)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(2,3)
graph.add_edge(2,4)
graph.add_edge(3,5)
graph.add_edge(4,5)

graph.depth_first_traversal(0)

class Adjacent_graph:
    def __init__(self):
        self.list={}
        