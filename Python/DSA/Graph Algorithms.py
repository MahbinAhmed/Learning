# GRAPH ALGORITHMS--->>>

class Graph():
    def __init__(self,num_nodes,nodes) -> None:
        self.num_nodes = num_nodes
        self.nodes = nodes
        self.routes = [[] for _ in range(num_nodes)]
        for i,j in self.nodes:
            self.routes[i].append(j)
            self.routes[j].append(i)

    def matrix_output(self):
        table = [[0 for i in range(self.num_nodes)] for _ in range(self.num_nodes)]
        for i in range(self.num_nodes):
            for j in self.routes[i]:
                table[i][j]=1
        return table

    def bfs(self,root):
        queue = []
        checked = [False]*self.num_nodes
        checked[root]=True
        parents = [None]*self.num_nodes
        queue.append(root)
        i = 0
        while i < self.num_nodes:
            current = queue[i]
            for j in self.routes[current]:
                if not checked[j]:
                    queue.append(j)
                    checked[j]=True
                    parents[j]=current
            i += 1
        return queue,parents
    
    def dfs(self,root):
        stack = []
        result = []
        checked = [False]*self.num_nodes
        stack.append(root)

        while len(stack)>0:
            current = stack.pop()
            if not checked[current]:
                checked[current]=True
                result.append(current)
                for nodes in self.routes[current]:
                    if not checked[nodes]:
                        stack.append(nodes)
        return result


    def __repr__(self):
        result = []
        for i,j in enumerate(self.routes):
            result.append(f"node: {i} :- {j}")
        return "\n\n".join(result)
    
    def __str__(self) -> str:
        return self.__repr__()


nodes = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
g1 = Graph(5,nodes)
# print(g1)
# print(g1.matrix_output())
# print(g1.bfs(0))
# print(g1.dfs(0))

# DIRECTED & WEIGHTED GRAPH--->>>

class Graph_with_dir_and_wgt():
    def __init__(self,num_nodes,nodes,weighted=False,directed=False) -> None:
        self.num_nodes = num_nodes
        self.weighted = weighted
        self.directed = directed
        self.nodes = nodes
        self.routes = [[] for _ in range(self.num_nodes)]
        self.weights = [[] for _ in range(self.num_nodes)]
        for i in self.nodes:
            if self.weighted:
                j,k,l = i
                self.routes[j].append(k)
                self.weights[j].append(l)
                if not directed:
                    self.routes[k].append(j)
                    self.weights[k].append(l)
            else:
                j,k = i
                self.routes[j].append(k)
                if not directed:
                    self.routes[k].append(j)

    def  weight_finder(self,current,target):
        weight_list = self.routes[current]
        index = weight_list.index(target)
        result = self.weights[current][index]
        return result

    # def dijkstra_sp(self,start,target):
    #     visited = [False]*self.num_nodes
    #     distance = [float("inf")]*self.num_nodes
    #     stack = []

    #     stack.append(start)
    #     distance[start]=0
    #     idx = 0
    #     while idx<len(stack) and not visited[target]:
    #         current = stack[idx]
    #         visited[current] = True
    #         relative_nodes = self.routes[current]
    #         relative_weights = self.weights[current]
    #         # for i in relative_nodes:
    #         #     weight = self.weight_finder(current,i)
    #         #     if distance[current] + weight < distance[i]:
    #         #         distance[i]=distance[current] + weight
    #         for i,j in enumerate(relative_nodes):
    #             weight = relative_weights[i]
    #             if distance[current] + weight < distance[j]:
    #                 distance[j]=distance[current] + weight
            
    #         min_distance = float("inf")
    #         next_node = None
    #         for i in range(self.num_nodes):
    #             if not visited[i] and distance[i]<min_distance:
    #                 next_node = i
    #                 min_distance = distance[i]
    #         stack.append(next_node)
    #         idx += 1
    #     return distance[target]

    def dijkstra_theory(self,source,target):
        visited = [None]*self.num_nodes
        distance = [float("inf")]*self.num_nodes
        queue = []
        queue.append(source)
        distance[source]=0
        idx = 0
        while idx<len(queue):
            current = queue[idx]
            visited[current]=True
            relative_nodes = self.routes[current]
            for i,node in enumerate(relative_nodes):
                weight = self.weights[current][i]
                if distance[current]+weight<distance[node]:
                    distance[node]=distance[current]+weight
            next_node = None
            min_distance = float("inf")
            for i in range(self.num_nodes):
                if not visited[i] and distance[i]<min_distance:
                    next_node = i
                    min_distance = distance[i]
            if next_node is not None:
                queue.append(next_node)
            idx += 1
        return distance[target]

    def __repr__(self) -> str:
        result = []
        if self.weighted:
            for i,(routes,weights) in enumerate(zip(self.routes,self.weights)):
                result.append(f"node |{i}| : routes-{routes}, weight-{weights}")
        else:
            for i,j in enumerate(self.routes):
                result.append(f"node |{i}| : routes-{routes}")
        return "\n".join(result)

    def __str__(self) -> str:
        return self.__repr__()
graph = [[0,1,2],[0,4,4],[1,4,8],[1,3,1],[2,1,7],[3,4,5],[3,2,6],[4,3,5]]
graph2 = [[0,1,4],[0,4,8],[1,4,11],[1,2,8],[4,8,7],[4,5,1],[2,8,2],[2,6,4],[8,5,6],[5,6,2],[2,3,7],[3,6,14],[3,7,9],[6,7,10]]
g2 = Graph_with_dir_and_wgt(5,graph,weighted=True,directed=True)
# print(g2)
print(g2.dijkstra_theory(0,2))