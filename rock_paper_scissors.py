# rock_paper_scissors.py
# Exercises selected: Final Project - Rock, Paper, Scissors Game
# Name of program: Rock, Papers, Scissors
# Description of program: Classic game of Rock, Paper, Scissors.  The user
#   will have the option to play against the computer or against another
#   user.
#
# Ivan Boatwright
# April 29, 2016

# For computer's move.
import random

def main():
    # Initialize Tournament.
    j = Tournament() # j is for janken

    # Displays an introduction to the program and describes what it does.
    fluffy_intro()
    main_menu = Menu(j.main_opts)
    main_menu()


    return None





# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print("Welcome to Rock, Paper, Scissors sim.")
    return None

def display_rules(*args):
    print("The rules are as follows:\n"
          "Paper Covers Rock\n"
          "Rock Smashed Scissors\n"
          "Scissors Cut Paper\n\n")
    return None

# Getto style clear console screen by newline flooding.
def clear(n=50):
    print("\n" * n)
    return None




class Player:
    """JKP Player and Computer class"""
    def __init__(self, name=None):
        self.name = name if name != None else "Computer"
        self.score_WLT = [0, 0, 0] # [wins, loses, ties]

    def __repr__(self):
        return self.name, self.score_WLT

    def __str__(self):
        r = "{} has {} wins, {} loses, and {} tie games."
        return r.format(self.name.capitalize(), *self.score_WLT)

    def __pos__(self):  # +Player increments player wins
        self.score_WLT[0] += 1

    def __neg__(self):  # -Player increments player loses
        self.score_WLT[1] += 1

    def __invert__(self):  # ~Player increments player ties
        self.score_WLT[2] += 1


class Game:
    # moves[0:2] player1 wins, moves[3:5] player2 wins, else tie match
    moves = ["RS", "PR", "SP", "SR", "RP", "PS"]
    results = {"RS":"Rock smashes Scissors!", "PR": "Paper covers Rock!",
               "SP": "Scissors cut Paper!", "SR":
               "Scissors are smashed by Rock!", "RP":
               "Rock is smothered by Paper!",
               "PS": "Paper is cut by Scissors!",
               "RR": "", "PP": "", "SS": ""}
    """initialized instance from main menu"""
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.round_count = 1
        self.match_score = [0, 0, 0] # [p1 wins, p2 wins, ties]
        self.attacks = ""
        self.last_winner = None

    # Todo: add a print statement for Game class
    def __str__(self):
        r = ""
        for p in self.players:
            r += p

    # +Game increments the round counter.
    def __pos__(self):
        self.round_count += 1

    def rock(self):
        self.judge("R")

    def paper(self):
        self.judge("P")

    def scissors(self):
        self.judge("S")

    # Called each time an attack is made.  It overwrites previous round
    #   attacks.
    def judge(self, attack):
        if len(self.attacks) == 2:
            self.attacks = attack
        else:
            self.attacks += attack

        if self.attacks in self.moves[0:2]: # P1 wins
            self.winner(0, 1)
            self.last_winner = self.players[0]
        elif self.attacks in self.moves[3:5]: # P2 wins
            self.winner(1, 0)
            self.last_winner = self.players[1]
        else: # Tie round
            self.winner(2)
            self.last_winner = None

    # Updates player object and match after each round.
    # noinspection PyStatementEffect
    def winner(self, W, L=2):
        self.match_score[W] += 1
        if W != 2:
            +self.players[W]
            -self.players[L]
        else:
            ~self.players[0]
            ~self.players[1]


class Tournament:
    """initialized with main menu.  Tracks player stats between games."""

    def __init__(self):
        self.match_count = 1
        computer = Player()
        player1 = Player('player1')
        player2 = Player('player2')
        self.players = [computer, player1, player2]
        self.main_opts = [('Read the rules', display_rules),
                     ('Player vs Computer', self.new_PvC),
                     ('Player vs Player', self.new_PvP)]



    def new_PvC(self):
        self.start_match(self.players[1], self.players[0])

    def new_PvP(self):
        self.start_match(self.players[1], self.players[2])

    # Runs the actual match loop.
    def start_match(self, p1, p2):
        self.match = Game(p1, p2)
        game_opts = [('Rock', self.match.rock), ('Paper', self.match.paper),
                     ('Scissors', self.match.scissors)]
        game_menu = Menu(game_opts, "Return to main menu")
        while game_menu.select != 0:
            print("Round {}. {}'s turn.".format(self.match.round_count,
                                                p1.name))
            game_menu.display_menu()
            game_menu.do_select()
            print(p1)
            print(p2)
            if game_menu.select == 0:
                continue
            if p2.name.lower() == "computer":
                self.match.judge(random.choice("RPS"))
            else:
                print("\n"*50)
                print("Round {}. {}'s turn.".format(self.match.round_count,
                                                    p1.name))
                game_menu.display_menu()
                game_menu.do_select()
            print(self.match.results[self.match.attacks])
            if self.match.last_winner == None:
                print("This round was a tie. No winners.")
                print("Current Score: {} - {} wins, {} - {} wins, {} ties."
                      "".format(p1.name, self.match.match_score[0],
                                p2.name, self.match.match_score[1],
                                self.match.match_score[2],))



    # Increment the match counter
    def __pos__(self):
        self.match_count += 1

class Menu:
    """Base menu class."""
    def __init__(self, cOpts, arg="Exit"):
        self.mOpts = ''
        # silliness to ensure the class exit_menu function is used.
        if cOpts[-1][1] == self.exit_menu:
            self.mOpts = []
        elif cOpts[-1][1] == 'X':
            self.mOpts = [(cOpts[-1][0], self.exit_menu)]
        else:
            self.mOpts = [(arg, self.exit_menu)]
        print(self.mOpts)
        self.mOpts.extend(cOpts)
        self.mCount = str(len(self.mOpts))
        self.select = True
        self.v_menu = Valid_Menu()
        self.v_name = Valid_Name()

    def __call__(self, *args, **kwargs):
        while self.select != 0:
            self.display_menu()
            self.do_select() # user picks weapon and it's stored

    # Prints the menu header and menu options to stdout.  The menuOptions list
    #   is the parameter and used to generate the option strings.
    def display_menu(self):
        # todo: print(page_header('Main Menu'))
        # This loops through the list starting at [1] and prints [0] (Exit)
        #   at the end.
        for l in range(1, len(self.mOpts)):
            print('  {0}) {1}'.format(l, self.mOpts[l][0]))
        print('  {0}) {1}'.format(0, self.mOpts[0][0]))
        return None

    # noinspection PyCallingNonCallable
    def do_select(self):
        self.select = int(self.v_menu('selection', self.mCount +
                                       ' menu options'))
        self.mOpts[self.select][1]()


    # Sets the loop control variable to 0 which ends the while loop.
    def exit_menu(self):
        print("Rock on mate!")
        self.select = 0
        return None


class Validate:
    def __init__(self, base_prompt=("Please enter your {}.", "  >>> "),
                 base_error="!!! Error: {} is not a valid value."):
        self.base_prompt = base_prompt
        self.base_error = base_error

    def __call__(self, prompt_term, condition='integer'):
        raw_input = self.get_inputs(prompt_term)
        while not self.test_value(condition, raw_input):
            print(self.base_error.format(raw_input))
        return raw_input

    def get_inputs(self, prompt_term):
        print(self.base_prompt[0].format(prompt_term))
        return input(self.base_prompt[1])

    def test_value(self, condition, item):
        if condition == 'integer':
            try:
                int(item)
                valid = True
            except:
                valid = False
        else:
            valid = None
        return valid


class Valid_Menu(Validate):
    """Validates user menu selection."""
    def __init__(self):
        base_error = "!!! Error: {} is not a valid selection."
        Validate.__init__(self, base_error=base_error)

    def test_value(self, condition, item):
        if condition == 'integer':
            valid = Validate.test_value(self, condition, item)
        elif condition[1:] == ' menu options':
            try:
                if len(item) > 0 and int(item) >= 0 and \
                                int(condition[:1]) > int(item):
                    valid = True
                else:
                    valid = False
            except:
                valid = False
        else:
            valid = False
        return valid

class Valid_Name(Validate):
    """Validates user name input."""
    def __init__(self):
        base_error = "!!! Error: {} is not a valid username."
        Validate.__init__(self, base_error=base_error)

    def get_inputs(self):
        prompt_term = "username"
        return Validate.get_inputs(self, prompt_term)

    def test_value(self, condition, item):
        if condition == 'username':
            if item.isalnum() and len(item) <= 10:
                valid = True
            else:
                valid = False
        else:
            valid = False
        return valid


main()
