# -*- coding: utf-8 -*-

from typing import Tuple

from hivegame.board import Board
from hivegame.player import Player, PlayerColor


class Game(object):
    @staticmethod
    def _show_game_rules():
        print("Game Rules: ")
        # TODO: Print game rules and how to move pieces

    def __init__(
        self,
        player1_name: str,
        player1_color: PlayerColor,
        player2_name: str,
        player2_color: PlayerColor,
    ):
        """Game

        Parameters
        ----------
        player1_name : str
            Player 1's name.
        player1_color : PlayerColor
            Player 1's color.
        player2_name : str
            Player 2's name.
        player2_color : PlayerColor
            Player 2's color.
        """
        self._reset_game_state(player1_name, player1_color, player2_name, player2_color)

    def _reset_game_state(
        self,
        player1_name: str,
        player1_color: PlayerColor,
        player2_name: str,
        player2_color: PlayerColor,
    ):
        """Resets the game state and clears the board.

        Parameters
        ----------
        player1_name : str
            Player 1's name.
        player1_color : PlayerColor
            Player 1's color.
        player2_name : str
            Player 2's name.
        player2_color : PlayerColor
            Player 2's color.
        """
        # Create players and game state
        self._b = Board()
        self._p1 = Player(player1_name, player1_color, self._b)
        self._p2 = Player(player2_name, player2_color, self._b)

    def run_game_loop(self) -> bool:
        """Runs the primary game loop.

        Returns
        -------
        bool
            True if the players decided to play a new game, false otherwise.
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
        print(f"*** {winner.name} ({winner.color}) has won! ***\n")

        play_again = _get_player_prompt_choice(
            prompt="Play Again (yes or no)? ", choices=("yes", "no")
        )
        return play_again == "yes"

    def get_players_names_and_colors(self) -> Tuple[str, PlayerColor, str, PlayerColor]:
        """Get player names and colors.

        Returns
        -------
        Tuple[str, PlayerColor, str, PlayerColor]
            A 4-tuple containing (player 1 name, player 1 color, player 2 name, player 2 color).
        """
        return self._p1.name, self._p1.color, self._p2.name, self._p2.color


def _create_game() -> Game:
    """Get the players' names and colors. Create and return the game object.

    Returns
    -------
    Game
        The new game object with players' names and colors.
    """
    player1_name = input("Player 1's name: ")
    player1_color = _get_player_prompt_choice(
        "Player 1's color (black or white): ", choices=("black", "white")
    )
    player1_color = PlayerColor.Black if player1_color == "black" else PlayerColor.White
    player2_name = input("Player 2's name: ")
    player2_color = (
        PlayerColor.Black if player1_color == PlayerColor.White else PlayerColor.White
    )
    return Game(player1_name, player1_color, player2_name, player2_color)


def _get_player_prompt_choice(prompt: str, choices: Tuple = ("yes", "no")) -> str:
    """Show a prompt on screen and return the result from the list of available choices.

    Parameters
    ----------
    pormpt : str
        Player prompt to show on-screen.
    choices : Tuple, optional
        The available choices, by default ("yes", "no").

    Returns
    -------
    str
        Player's choice
    """
    choice = ""
    while choice not in choices:
        choice = input(prompt)
    return choice


def start_game_menu():
    """The primary game menu."""
    # Start game
    game = None
    play_again = True
    while play_again:
        if game is None:
            game = _create_game()
        else:
            same_players = _get_player_prompt_choice(
                prompt="Replay with same players and colors (yes or no?)? ",
                choices=("yes", "no"),
            )
            if same_players == "no":
                game = _create_game()
            else:
                game = Game(*game.get_players_names_and_colors())

        print("\n------------- AUTOHIVE --------------\n")
        play_again = game.run_game_loop()

    # End game
    print("Thanks for playing Autohive. Goodbye!")
    print("\n------------- AUTOHIVE --------------\n")
