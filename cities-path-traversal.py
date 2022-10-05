import csv
from collections import deque

class System:
    steps = [   
        [-1,0], # Top Step #up 
        [0,1],  # Right Step
        [1,0], # Bottom Step #down
        [0,-1] # Left Step
    ]
    
    def __init__(self):
        self.star_city = list()
        self.star_city_rows = 0
        self.star_city_cols = 0
        self.dest=0
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.reader(data_file)
        self.star_city=list()
        for row in reader:
            self.star_city.append(row)
        self.star_city_rows=len(self.star_city)
        self.star_city_cols=len(self.star_city[0])

    def check_limits(self,row_num, col_num):
        if 0 <= row_num < self.star_city_rows and 0 <= col_num < self.star_city_cols:
            return True
        return False

    def get_neighbours(self,row,col):
        neighbours=[]
        #loop through top, right, bottom and left adjacent nodes to get the neighbor
        # only if the altitude of adjacent node is lower or equal to the current node 
        # and is not already present in neighbors list
        for i in System.steps:
            if self.check_limits(row+i[0], col+i[1]):
                if self.star_city[row+i[0]][col+i[1]] <= self.star_city[row][col] and (row+i[0],col+i[1]) not in neighbours:
                    neighbours.append((row+i[0],col+i[1]))
        return neighbours
    
    def find_route(self,source,destination):
        visited=[]
        queue=deque()
        path={}
        if type(destination) is not list:
            destination=[destination]
        
        #add 1st node in visited and que lists
        visited.append(source)
        queue.append(source)
        
        #traverse all the nodes from queue till the queue is not empty
        # and destination is not found
        while queue:
            #remove current node from queue
            curr = queue.pop()
                
            #check if current node has neighbours
            if len(System.get_neighbours(self,curr[0],curr[1]))>0:
                
                #temporary list which will have all neighbour nodes of current node 
                # which are added in visited list
                neighb=[]
                #get each neighbor of current node
                neighb=System.get_neighbours(self,curr[0],curr[1])
                
                for item in neighb:
                    #if neighbor is not visited then mark it visited by adding in visited 
                    # and also add it in queue
                    queue.append(item)
                    
                    if item not in visited:
                        visited.append(item)
                        
                        i,j=item[0]-curr[0],item[1]-curr[1]
                        path.update({item : (i,j)})
                        
                        # if neighbour is the destination node 
                        # then extract all the nodes from visited till the current node 
                        # and break the loop
                        if item in destination:
                            route=[]
                            self.dest=item
                            o,p=path.popitem()
                            while o != source:
                                o=o[0]-p[0], o[1]-p[1]
                                route.insert(0, o)
                                if o==source:
                                    return route
                                p=path.pop(o)
                        
                    #if neighbour already in visited list, 
                    # so no need  to keep the current node and 
                    # the neighbours (already added in visited) of current node
                    # in the visited list and queue list
                    else:
                        for item in neighb:
                            visited.remove(item)
                            queue.remove(item)
                            path.pop(item)
                        visited.remove(curr)
                        path.pop(curr)
                        
                                           
            # if current node has no neighbour then no need to keep it in visited list 
            else:
                visited.remove(curr)
                path.pop(curr)
        return None
        #pass

    def Bluevalley_to_Smallville_route(self):
        
        #list of indices of source and destination cities:
        bluev=[]
        smallv=[]
        
        l=self.star_city_cols-1
        
        for k in range(self.star_city_rows):
            b=(k,0)
            s=(k,l)
            bluev.append(b)
            smallv.append(s)
        
        for item in bluev:
            route=System.find_route(self,bluev.pop(),smallv)
            if route != None:
                break
        print("\nTo reach city Smallville from city Blue Valley the nodes traversed are- \n")
        if route==None:
            print("Route does not exist")
        else:
            for node in route:
                print(f"({node[0]},{node[1]}) ---->", end=" ")
            print(self.dest)
        #pass
    
if __name__ == "__main__":
    test_system1 = System()
    
    #Getting data in 2D matrix
    test_system1.config_system('city_data.csv')
    
    #Finding path between Source node to Destination node
    route = test_system1.find_route((3,0),(4,2))
    print(f"\n\nTo reach Node (4,2) from Node (3,0) the nodes traversed are-")
    for node in route:
        print(f"({node[0]},{node[1]}) ---->", end=" ")
    print((4,2))
    
#Finding path between Bluevalley to Smallville   
    test_system1.Bluevalley_to_Smallville_route()