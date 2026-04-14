class Graph:
    def __init__(self,vertex):
        self.mat=[[0]*vertex for i in range(vertex)]
        self.size=vertex
    def add_edge(self,row,col):
    
        if 0<=row<self.size and 0<=col<self.size:
            self.mat[row][col]=1
            self.mat[col][row]=1
        else:
            print("invalid value")
    def display(self):
        for row in self.mat:
            matrix=list(map(str,row))
            print(str(''.join(list(matrix))))
            # print(' '.join(matrix))
    def depth_first_search(self,src):
        stack=[src]
        visited=[False]*self.size
        while stack:
            v=stack.pop()
            if visited[v]==False:
                print(v)
                visited[v]=True
            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:
                    stack.append(i)
    def breath_first_search(self,src):
        visited=[False]*self.size
        queue=[src]
        while queue:
            v=queue.pop(0)
            if visited[v]==False:
                print(v,end=' ')
                visited[v]=True
            # for i in self.mat:wrong need index not the 
            for i in range(self.size):
                
                if self.mat[v][i]==1 and visited[i]==False:
                    queue.append(i) 

graph=Graph(7)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(2,5)
graph.add_edge(3,4)
graph.add_edge(3,6)

graph.display()
# graph.depth_first_search(1)
graph.breath_first_search(0)


# why this is problem because it takes unnessary space .good for sparse graph (number of graphs high)