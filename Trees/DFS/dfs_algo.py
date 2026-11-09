'''
BASIC IMPLEMENTATION OF DFS
'''

'''
APPROACH
1. Initialize a set to keep track of visited nodes
2. Initialize an empty stack (LIFO)
3. Add the start_node to set and also push into stack
4. As long as stack isnt empty (end condition)
    4.1 Pop node and print it (current node)
    4.2 For all neighbors in graph[current_node]
        4.2.1. Check if neighbor already visited if not, add to visited and append in stack
5. This iterates till the stack becomes empty
'''


def dfs(graph, start_node):
    visited=set() # Empty set to keep track of visited nodes (avoids duplicate processing)
    stack=[]

    visited.add(start_node)
    stack.append(start_node)

    while stack:
        current_node=stack.pop()
        print(current_node, end=" ")

        for neighbor in graph[current_node]: # use reversed(graph[current_node]) if you want to process in order
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

