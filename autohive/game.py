from player import Player
from board import Board

class Game (object):
    @staticmethod
    def _show_game_rules():
        print('Game Rules: ')
        # TODO: Print game rules and how to move pieces


    def __init__(self, player1_name, player1_color, player2_name, player2_color):
        self._reset_game_state(player1_name, player1_color, player2_name, player2_color)

    def _reset_game_state (self, player1_name, player1_color, player2_name, player2_color):
        # Create players and game state
        self._b  = Board()
        self._p1 = Player(player1_name, player1_color, self._b)
        self._p2 = Player(player2_name, player2_color, self._b)

    def run_game_loop(self) -> bool:
        """
        """
        # Start game
        current_p = None
        winner = None
        is_p1_turn = True

        while True:
            if is_p1_turn:
                current_p = self._p1
            else:
                current_p = self._p2
            current_p.take_turn()

            winner = self._b.check_win_condition()
            if winner is not None:
                break
            is_p1_turn = ~is_p1_turn

        # Show winnner and ask to play again.
        print(f'*** {winner.name} ({winner.color}) has won! ***\n')

        play_again = _get_player_menu_choice(
            msg = 'Play Again (yes or no)? ',
            choices = ('yes', 'no'))
        return play_again == 'yes'

    def get_players_names_and_colors(self):
        return self._p1.name, self._p1.color, self._p2.name, self._p2.color

def _create_game():
    player1_name = input("Player 1's name: ")
    player1_color = input("Player 1's color (black or white): ")
    player2_name = input("Player 2's name: ")
    player2_color = input("Player 2's color (black or white): ")
    return Game(player1_name, player1_color, player2_name, player2_color)

def _get_player_menu_choice(msg, choices = ('yes', 'no')):
    choice = ''
    while choice not in choices:
        choice = input(msg)
    return choice

if __name__ == '__main__':
    # Start game
    game = None
    play_again = True
    while play_again:
        if game is None:
            game = _create_game()
        else:
            same_players = _get_player_menu_choice(
                msg = 'Replay with same players and colors (yes or no?)? ',
                choices = ('yes', 'no'))
            if same_players == 'no':
                game = _create_game()
            else:
                game = Game(*game.get_players_names_and_colors())

        print('\n------------- AUTOHIVE --------------\n')
        play_again = game.run_game_loop()

    # End game
    print('Thanks for playing Autohive. Goodbye!')
    print('\n------------- AUTOHIVE --------------\n')
