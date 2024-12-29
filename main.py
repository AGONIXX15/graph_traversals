import json
from collections import deque


def dfs_recursive(graph, node, visited):

    print(node, end=" ")
    visited.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)


def dfs_iterative(graph, start):
    stack, visited = [start], []

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)


def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            queue.append(neighbour)
    bfs_recursive(graph, queue, visited)


def bfs_iterative(graph, start):
    queue, visited = deque([start]), []
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)


if __name__ == '__main__':
    with open('graph1.json', 'r') as f:
        data = json.load(f)
    graph = data['graph']

    print("this is dfs recursive:", end=" ")
    dfs_recursive(graph, "A", [])
    print()
    print("this is dfs iterative:", end=" ")
    dfs_iterative(graph, "A")
    print()
    print("this is bfs recursive:", end=" ")
    bfs_recursive(graph, deque(["A"]), [])
    print()
    print("this is bfs iterative:", end=" ")
    bfs_iterative(graph, "A")
    print()
