
def earliest_ancestor(ancestors, starting_node):   
    #make a copy of the ancestors
    #also make a set of nodes
    nodes={}
    copy = ancestors.copy()
    
    #loop through each item in the copy of ancestors
    while len(copy)>0:
        #pop ancestor-node off and check
        current = copy.pop()
        #see if the first node's edge is in nodes variable
        if not nodes.get(current[1]):
            #if nah, add it with defaults.
            nodes[current[1]]={
                'key':current[1],
                'distance':None,
                'parent':set()
            }
        #once it is, mark the parent set with it.
        nodes.get(current[1]).get('parent').add(current[0])
    
    #if it aint in the node set after the loop, it dont exist.
    if not nodes.get(starting_node):
        return -1

    #check the path lengths and see which is longest
    check=[starting_node]

    while len(check)>0:
        #pop off the node we're checking.
        current = nodes.get(check.pop())

        #have we already assigned a distance?
        if not current.get('distance'):
            current['distance']=0 #set to a zero to start

        #check if the parent is in nodes
        for parent in current.get('parent'):
            
            #add it if not. same defaults as before.
            if not nodes.get(parent):
                nodes[parent]={
                    'key':parent,
                    'distance':None,
                    'parent':set()
                }
            #assign the parent distance
            nodes.get(parent)['distance']=current.get('distance')+1
            #do the same with parent nodes, all the way down the chain
            check.append(parent)

    #variable to store the answer.
    largest = (None,0)

    #loop through each node in resulting nodes set
    for node in nodes.values():
        #grab the node with the largest distance
        if node.get('distance') and node.get('distance')>largest[1]:
            largest=(node['key'],node['distance'])
        #also, if there is a tie, smallest ID wins.
        elif node.get('distance') and node.get('distance')==largest[1] and node.get('key') < largest[0]:
            largest=(node['key'],node['distance'])

    #return the answer, as the expected value.
    return largest[0]