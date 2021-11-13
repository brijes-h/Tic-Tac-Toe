# Tic-Tac-Toe AI Game using Pygame Module

## About the project
In this project I have implemented the MiniMax algorithm and Alpha-Beta pruning in a game of Tic-tac-toe. The project is built using Python language and Pygame Module.

### What is Tic-Tac-Toe?
Tic-tac-toe, also known as Xs and Os is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner.

![image](https://miro.medium.com/max/395/1*mIjIjWIUc45MQjLDVkOC-w.png)

### MiniMax Algorithm
Minimax algorithm is used to develop AI for games that are played using two players, like Chess, Tic-tac-toe, etc. 
The algorithm works by recursively searching for the **best move** that would result in minimizing the chances of the user winning, and maximizing the chances of the AI winning, hence the name “minimax”. This recursive search is done until a terminal node / state is reached.

**Alpha-Beta Pruning**:
Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree.

### Pseudocode:
```
function minimax(position, depth, alpha, beta, maximizingPlayer)
	if depth == 0 or game over in position
		return static evaluation of position
 
	if maximizingPlayer
		maxEval = -infinity
		for each child of position
			eval = minimax(child, depth - 1, alpha, beta false)
			maxEval = max(maxEval, eval)
			alpha = max(alpha, eval)
			if beta <= alpha
				break
		return maxEval
 
	else
		minEval = +infinity
		for each child of position
			eval = minimax(child, depth - 1, alpha, beta true)
			minEval = min(minEval, eval)
			beta = min(beta, eval)
			if beta <= alpha
				break
		return minEval
```

**Reference video for MiniMax and Alpha-Beta pruning:** 
https://youtu.be/l-hh51ncgDI

