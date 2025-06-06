import TicTacToe as ttt

def test_getReward():
    rlAgent = ttt.createPlayer('X', ttt.RL_AGENT)
    
    board = ttt.TicTacToe()
    board.setPlayers(rlAgent, ttt.createPlayer('O', ttt.RANDOM_AGENT))
    board.board = ['X', 'X', 'X', '*', '*', '*', '*', '*', '*']
    board.moveCount = 3
    reward = rlAgent.getReward(board)
    if reward == 10:
        print("Test 1 Passed: RL Agent wins (Reward = 10)")
    else:
        print(f"Test 1 Failed: Expected 10 for win, but got {reward}")

    board.board = ['O', 'O', 'O', '*', '*', '*', '*', '*', '*']
    board.moveCount = 3
    reward = rlAgent.getReward(board)
    if reward == -10:
        print("Test 2 Passed: Opponent wins (Reward = -10)")
    else:
        print(f"Test 2 Failed: Expected -10 for loss, but got {reward}")

    board.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
    board.moveCount = 9
    reward = rlAgent.getReward(board)
    if reward == 5:
        print("Test 3 Passed: Draw (Reward = 5)")
    else:
        print(f"Test 3 Failed: Expected 5 for draw, but got {reward}")

    board.board = ['X', 'O', 'X', '*', '*', 'O', '*', 'X', '*']
    board.moveCount = 5
    reward = rlAgent.getReward(board)
    if reward == 0:
        print("Test 4 Passed: Ongoing game (Reward = 0)")
    else:
        print(f"Test 4 Failed: Expected 0 for ongoing game, but got {reward}")

test_getReward()