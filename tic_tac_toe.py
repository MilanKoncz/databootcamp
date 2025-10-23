#!/usr/bin/env python3
"""
Tic Tac Toe Game
A simple console-based implementation of the classic Tic Tac Toe game.
"""


class TicTacToe:
    """A Tic Tac Toe game class."""
    
    def __init__(self):
        """Initialize the game board and current player."""
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    
    def display_board(self):
        """Display the current state of the board."""
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")
    
    def display_board_with_positions(self):
        """Display the board with position numbers for reference."""
        print("\nPosition numbers:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("\n")
    
    def is_valid_move(self, position):
        """Check if a move is valid."""
        return 0 <= position < 9 and self.board[position] == ' '
    
    def make_move(self, position):
        """Make a move on the board."""
        if self.is_valid_move(position):
            self.board[position] = self.current_player
            return True
        return False
    
    def check_winner(self):
        """Check if there's a winner."""
        # Define winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] 
                and self.board[combo[0]] != ' '):
                return self.board[combo[0]]
        
        return None
    
    def is_board_full(self):
        """Check if the board is full."""
        return ' ' not in self.board
    
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def reset(self):
        """Reset the game board."""
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    
    def play(self):
        """Main game loop."""
        print("=" * 40)
        print("Welcome to Tic Tac Toe!")
        print("=" * 40)
        self.display_board_with_positions()
        
        while True:
            self.display_board()
            print(f"Player {self.current_player}'s turn")
            
            try:
                position = input("Enter position (1-9) or 'q' to quit: ").strip()
                
                if position.lower() == 'q':
                    print("Thanks for playing!")
                    break
                
                position = int(position) - 1  # Convert to 0-based index
                
                if not self.is_valid_move(position):
                    print("Invalid move! That position is either taken or out of range.")
                    continue
                
                self.make_move(position)
                
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"🎉 Player {winner} wins! 🎉")
                    if not self.ask_play_again():
                        break
                    continue
                
                if self.is_board_full():
                    self.display_board()
                    print("It's a tie! 🤝")
                    if not self.ask_play_again():
                        break
                    continue
                
                self.switch_player()
                
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 1 and 9.")
    
    def ask_play_again(self):
        """Ask if players want to play again."""
        while True:
            choice = input("Play again? (y/n): ").strip().lower()
            if choice == 'y':
                self.reset()
                self.display_board_with_positions()
                return True
            elif choice == 'n':
                print("Thanks for playing!")
                return False
            else:
                print("Please enter 'y' or 'n'.")


def main():
    """Main function to run the game."""
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()
