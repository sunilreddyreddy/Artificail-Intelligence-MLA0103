1.BFS PSEUDO CODE

1.Create an empty queue Q
2.Mark start as visited
3.Enqueue start into Q
4.While Q is not empty
5.vertex ← Dequeue(Q)
6.Print vertex
7.For each neighbor of vertex
8.If neighbor is not visited
9.Mark neighbor as visited
10.Enqueue neighbor into Q
End While

2.DFS PSEUDO CODE

1.Mark vertex as visited
2.Print vertex
3.For each neighbor of vertex
4.If neighbor is not visited
5.Call DFS(G, neighbor)
End For
