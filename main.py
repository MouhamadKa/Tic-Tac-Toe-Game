import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

class Player:
    def __init__(self):
        self.name = ''
        self.symbol = ''
        
    def choose_name(self):
        while True:
            name = input('Enter your name (letters only): ')
            if name.isalpha():
                self.name = name.capitalize()
                break        
            print('Invalid name. Please use letters only.')
            
    def choose_symbol(self):
        while True:
            symbol = input(f'{self.name}, choose your symbol (a single letter): ')
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print('Invalid symbol. Please choose one letter only.')

class Menu:
    def display_main_menu(self):
        main_menu_message = '''Welcone to X-O game!
1. Start the game
2. Quit the game
'''

        while True:
            user_choice = input(main_menu_message)
            if user_choice == '1' or user_choice == '2':
                return user_choice
            print('Please enter 1 or 2')
            
    def display_endgame_menu(self):
        main_menu_message = '''Game ended!! What do you want to do??
1. Restart the game
2. Quit the game
'''

        while True:
            user_choice = input(main_menu_message)
            if user_choice == '1' or user_choice == '2':
                return int(user_choice)
            print('Please enter 1 or 2')

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print(' | '.join(self.board[i : i+3]))
            if i < 6:
                print('-'*10)
        print()
        print()
                
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False
        
    def reset_board(self):
        self.__init__()

    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()
     
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.menu = Menu()
        self.curr_player_index = 0
    
    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
            
        else:
            self.quit_game()
            
            
    def restart_game(self):
        self.board.reset_board()
        self.curr_player_index = 0
        self.play_game()
        
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == '1':
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            self.switch_player()
    
    def switch_player(self):
        self.curr_player_index = 1 - self.curr_player_index        
    
    def play_turn(self):
        player = self.players[self.curr_player_index]
        self.board.display_board()
        print(f'{player.name}\'s turn, ({player.symbol})')
        while True:
            try:
                choice = int(input('Enter your choice between 1 and 9: '))
                if 0 < choice < 10 and self.board.update_board(choice=choice, symbol=player.symbol):
                    break
                else:                     
                    print('Invalid input. Please enter a number of an empty cell between 1 and 9.')
            except:
                print('Invalid input. Please enter a valid choice between 1 and 9.')
                
    def check_win(self):
        win_combinations = [
            [0,1,2], [3,4,5], [6,7,8], # Rows Combinations
            [0,3,6], [1,4,7], [2,5,8], # Columns Combinations
            [0,4,8], [2,4,6] # Diagonals
        ]
        for combination in win_combinations:
            if self.board.board[combination[0]] == self.board.board[combination[1]] == self.board.board[combination[2]]:
                self.congratulate_winner(self.board.board[combination[0]])
                return True
        return False
    
    def congratulate_winner(self, symbol):
        winner_name = self.players[0].name if symbol == self.players[0].symbol else self.players[1].name
        print(f'Congratulation {winner_name}, you won the game.')
        
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
        # for cell in self.board.board:
        #     if cell.isdigit():
        #         return False
        # return True
            
    def setup_players(self):
        for index, player in enumerate(self.players, start=1):
            print(f'Player {index}, enter your details')
            player.choose_name()
            player.choose_symbol()
            clear_screen()
            
    def quit_game(self):
        print('Thank you for playing!')


game = Game()
game.start_game()