import math

def alphabeta(depth, node, isMax, values, alpha, beta, height):
    if depth == height:
        return values[node]

    if isMax:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, False,
                            values, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, True,
                            values, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 2, 9]
height = 2

print("Optimal Value:",
      alphabeta(0, 0, True, values, -math.inf, math.inf, height))
