


def dfs_detect_cycle(graph, start_node):
    visited=set() # Empty set to keep track of visited nodes (avoids duplicate processing)
    stack=[]
    parent={}

    visited.add(start_node)
    parent[start_node]=None 
    stack.append((start_node,parent[start_node])) #(node,parent)

    while stack:
        current_node, current_parent=stack.pop()

        for neighbor in graph[current_node]: # use reversed(graph[current_node]) if you want to process in order
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor]=current_node
                stack.append((neighbor, current_node))

            elif neighbor!=current_parent:
                return True
        
    return False

            