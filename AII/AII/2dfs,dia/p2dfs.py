import random
openList=[['Arad']]
closedList=[]
nodeList= {'Arad':['Sibiu','Timisora'],'Sibiu':['Arad','Timisora','Fagarus'],'Timisora':['Arad','Dorbeta'],'Dorbeta':['Timisora','Craiova'],'Fagarus':['Sibiu','Bucharest'],'Bucharest':['Dorbeta','Fagarus']}
def goalTest(some_node):
    return some_node == 'Bucharest'
def moveGen(some_node):
    return nodeList[some_node]
def SS3():
    while len(openList)>0:
        random.shuffle(openList)
        print("Open list Contains", openList)
        seen = openList.pop(0)
        N = seen[0]
        closedList.append(N)
        print("Picked Node: ", N)
        if goalTest(N):
            print("Goal Found")
            print(seen)
            return
        else:
            neighbours=moveGen(N)
            print("Neighbours of ",N," are : ", neighbours)
            for node in neighbours:
                if(node not in openList) and (node not in closedList):
                    l=[node,seen]
                    openList.append(l)
    print("Goal Not Found")
SS3()

