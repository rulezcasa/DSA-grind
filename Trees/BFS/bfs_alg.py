'''
BASIC IMPLEMENTATION OF BFS
'''

'''
APPROACH
1. Initialize visited as an empty set.
2. Initialize a deque with starting node
3. while queue is not empty :
    3.1 popleft (the oldest node) and retrieve the node
    3.2 index that node in graph to iterate over list of neighbours
        3.2.1 if neighbor not visited
            - add to visited
            - also, append to queue to processes it.
4. This iterates till the queue becomes empty i.e all nodes have been processed.
'''

from collections import deque


def bfs(graph, start_node):
    visited=set() # Empty set to keep track of visited nodes (avoids duplicate processing)

    # Start node initialization
    queue=deque([start_node]) 
    visited.add(start_node)

    # As long as queue isnt empty
    while queue:
        current_node=queue.popleft() # Pull out the oldest node in the queue
        print(current_node, end=" ") 

        # Track the neighbors of processed node (pulled out)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor) 


# --- Example Usage ---
if __name__ == "__main__":
    # Representing a graph using an adjacency list (Python Dictionary)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print("Breadth-First Traversal starting from node 'A':")
    bfs(graph, 'A')