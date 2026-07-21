1.BFS PSEUDO CODE
BEGIN
Create an empty Queue Q
Mark start node as visited
Enqueue(start)
WHILE Q is not empty DO
    node ← Dequeue(Q)
    Print node
    FOR each neighbor of node DO
        IF neighbor is not visited THEN
            Mark neighbor as visited
            Enqueue(neighbor)
        END IF
    END FOR
END WHILE
END

2.DFS PSEUDO CODE
BEGIN
Mark current node as visited
Print current node
FOR each neighbor of current node DO
    IF neighbor is not visited THEN
        DFS(neighbor)
    END IF
END FOR
END

3.UCS PSEUDO CODE
BEGIN
Create a Priority Queue PQ
Insert start node with cost 0
WHILE PQ is not empty DO
    Remove node with minimum cost
    IF node is goal THEN
        Print total cost
        STOP
    END IF
    FOR each neighbor of node DO
        Calculate new cost
        Insert neighbor with new cost into PQ
    END FOR
END WHILE
END

4.A* Search
BEGIN
Create a priority queue PQ
Insert start node into PQ
WHILE PQ is not empty DO
    Remove node with minimum f(n)
    IF node = goal THEN
        Print node
        STOP
    END IF
    FOR each neighbor DO
        f(n) = g(n) + h(n)
        Insert neighbor into PQ
    END FOR
END WHILE
END

5.Greedy Best-First Search (GBFS)
BEGIN
Create a priority queue PQ
Insert start node into PQ using heuristic value
WHILE PQ is not empty DO
    Remove node with smallest heuristic value
    Print node
    IF node = goal THEN
        STOP
    END IF
    FOR each unvisited neighbor DO
        Insert neighbor into PQ
    END FOR
END WHILE
END

6.Min-Max
FUNCTION MINIMAX(node, depth, isMax)
IF node is terminal OR depth = 0 THEN
    RETURN node value
END IF
IF isMax THEN
    best = -∞
    FOR each child of node DO
        best = MAX(best, MINIMAX(child, depth-1, FALSE))
    END FOR
    RETURN best
ELSE
    best = +∞
    FOR each child of node DO
        best = MIN(best, MINIMAX(child, depth-1, TRUE))
    END FOR
    RETURN best
END IF
END FUNCTION

7.Alpha-Beta Pruning
BEGIN
Apply Min-Max
Update Alpha and Beta values
IF Alpha ≥ Beta
    Prune remaining branches
Return best value
END
