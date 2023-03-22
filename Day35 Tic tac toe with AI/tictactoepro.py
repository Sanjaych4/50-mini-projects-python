import random

def draw_board(board):
   
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def get_player_move(board):
   
    while True:
        move = input("Enter a number (1-9) to make your move: ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == ' ':
            return int(move) - 1
        print("Invalid move, try again.")

def get_computer_move(board, computer_letter, player_letter):

    print("Computer is thinking...")
    best_score = -1000
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = computer_letter
            score = minimax(board, False, computer_letter, player_letter)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def minimax(board, is_maximizing, computer_letter, player_letter):
 
    result = check_winner(board, computer_letter, player_letter)
    if result is not None:
        return result

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = computer_letter
                score = minimax(board, False, computer_letter, player_letter)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = player_letter
                score = minimax(board, True, computer_letter, player_letter)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

def check_winner(board, computer_letter, player_letter):
 
    winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == computer_letter:
            return 1
        elif board[combo[0]] == board[combo[1]] == board[combo[2]] == player_letter:
            return -1
    if ' ' not in board:
        return 0
    return None

# Main program
if __name__ == '__main__':

    # Print the instructions
    print("Welcome to Tic Tac Toe!")
    print("The board is numbered from 1 to 9 as follows:")
    draw_board(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    print("You will be playing against the computer. The computer is O and you are X.")
    print("Enter a number (1-9) to make your move.")

    # Set up the game
    board = [' '] * 9
    computer_letter = 'O'
    player_letter = 'X'

    # Determine who goes first
    if random.randint(0, 1) == 0:
        current_player = 'computer'
    else:
        current_player = 'player'

    # Play the game
    while True:
        if current_player == 'player':
            draw_board(board)
            move = get_player_move(board)
            board[move] = player_letter
            if check_winner(board, computer_letter, player_letter) is not None:
                draw_board(board)
                print("You win!")
                break
            current_player = 'computer'
        else:
            move = get_computer_move(board, computer_letter, player_letter)
            board[move] = computer_letter
            if check_winner(board, computer_letter, player_letter) is not None:
                draw_board(board)
                print("Computer wins!")
                break
            current_player = 'player'
        if ' ' not in board:
            draw_board(board)
            print("It's a tie!")
            break

