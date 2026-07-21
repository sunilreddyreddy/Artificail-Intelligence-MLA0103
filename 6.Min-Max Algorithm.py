def minimax(depth, node, isMax, values, height):
    if depth == height:
        return values[node]

    if isMax:
        return max(
            minimax(depth+1, node*2, False, values, height),
            minimax(depth+1, node*2+1, False, values, height)
        )
    else:
        return min(
            minimax(depth+1, node*2, True, values, height),
            minimax(depth+1, node*2+1, True, values, height)
        )

values = [3, 5, 2, 9]
height = 2

print("Optimal Value:", minimax(0, 0, True, values, height))
