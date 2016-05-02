# rock_paper_scissors.py
# Exercises selected: Final Project - Rock, Paper, Scissors Game
# Name of program: Rock, Papers, Scissors
# Description of program: Classic game of Rock, Paper, Scissors.  The user
#   will have the option to play against the computer or against another
#   user.
#
# Ivan Boatwright
# April 29, 2016

def main():
    # Initialize Tournament.
    j = Tournament() # j is for janken

    # Customization Variables
    main_opts = [('Read the rules', display_rules),
                 ('Player vs Computer', j.new_PvC),
                 ('Player vs Player', j.new_PvP)]
    game_opts = []
    # Displays an introduction to the program and describes what it does.
    fluffy_intro()

    return None




# Section Block: Menu ------------------------------------------------------->
# TODO: main_menu{1: rules, 2: PvC, 3: PvP, 0: Quit}
# TODO: weapon_menu{1: Rock, 2: Paper, 3: Scissors, 0: Main Menu}
# Menu control options passed to the menu function.  A list with each
#   entry a tuple of [0] the display text and [1] the function to call.
#   Menu numbers start at 1), option 0) defaults to Exit.
cOpts = [('option 1','execute this'), ('option 2', 'etc')]


# main_menu prints a list of options for the user to select from.
def main_menu(cOpts, cVars):
    # Menu control options. A list with each entry a tuple of
    #   [0] the display text and [1] the function to call.
    # TODO: check for cOpts[0], else use this
    menuOptions = [('Exit', exit_menu)]  # Set default menu options.
    menuOptions.extend(cOpts)  # Add custom menu options.
    MENU_COUNT = len(menuOptions)

    # Initialize the loop control variable.
    menuSelection = True

    # While menuSelection does not equal 0 (the default exit option.)
    while menuSelection != 0:
        display_menu(menuOptions, cVars)
        # Calls the input request/validation function and converts the return
        #   value into an integer.  The number of menu elements is prepended
        #   to the input request and used as part of the validation testing.
        menuSelection = int(get_valid_inputs([[str(MENU_COUNT) +
                                               ' menu options', 'selection']]))

        # Use the validated user input to select the function reference and
        #   execute the function with the trailing ().
        menuSelection = menuOptions[menuSelection][1](cVars)

    # By design the exit_menu function runs before the while loop breaks.
    return None

# <<------------ End Block--------------------------------------------------<<

# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print("Welcome to RPS sim.")
    return None

def display_rules():
    print("Rock, Paper, Scissors.")
    return None

# Getto style clear console screen by newline flooding.
def clear(n=50):
    print("\n" * n)
    return None


# Section Block: Misc ------------------------------------------------------->
# todo: pick one or something
# Returns a string used to identify a new part(i.e. page) of the program.
def page_header(title, userName=''):
    return '{0}\n{1:^40}\n{0}\n{2:>40}'.format('=' * 40, title, userName)
def page_header2(title):
    return '{0}\n{1:^40}\n{0}'.format('='*40,title)
# Returns a string used to identify a new part(i.e. page) of the program.
def page_header3(title):
    return '{0:-<62}\n{1:^67}\n{0:_<62}\n'.format('    ', title)


# TODO: ___tablefy___________________
headers2 = ('SAVINGS', 'NOT GREEN', 'GONE GREEN', '  MONTH')
hDesign = '{0:^4}{{0:>10}}{0:^6}{{1:>10}}{0:^6}{{2:>10}}' \
                 '{0:^6}{{3:<8}}\n'.format('')
design = '{0:^3}{{0:>10}}{0:^6}{{1:>10}}{0:^6}{{2:>10}}' \
               '{0:^8}{{3:<8}}\n'.format('')

# tablefy2(title, headers2, hdesign, design, zip(*data))

# Takes a title, a set of headers, a header format string, a body format
#   string, a merged parallel array and returns a print friendly string.
def tablefy2(title, headers, hdesign, design, data):
    title = '{0:-<62}\n\n{1:^67}\n{0:_<62}\n'.format('    ', title)
    head = hdesign.format(*headers)
    division = '{0:4}{0:_<58}\n'.format('')
    body = ''.join([design.format(j[0], j[1], j[2], j[3]) for j in data])
    return '{}{}{}{}'.format(title, head, division, body)
# =======================================
# <<------------ End Block--------------------------------------------------<<

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
    """initialized instance from main menu"""
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.round = 1
        self.match_score = [0, 0, 0] # [p1 wins, p2 wins, ties]
        self.attacks = ""

    # Todo: add a print statement for Game class
    def __str__(self):
        r = ""
        for p in self.players:
            r += p

    # +Game increments the round counter.
    def __pos__(self):
        self.round += 1

    # Called each time an attack is made.  It overwrites previous match
    #   attacks.
    def judge(self, attack):
        if len(self.attacks) == 2:
            self.attacks = attack
        else:
            self.attacks += attack

        if self.attacks in self.moves[0:2]: # P1 wins
            self.winner(0, 1)
        elif self.attacks in self.moves[3:5]: # P2 wins
            self.winner(1, 0)
        else: # Tie round
            self.winner(2)

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
        self.match = 1
        computer = Player()
        player1 = Player('player1')
        player2 = Player('player2')
        self.players = [computer, player1, player2]

    def new_PvC(self):
        self.PvC = Game(self.players[1], self.players[0])

    def new_PvP(self):
        self.PvP = Game(self.players[1], self.players[2])

    def __pos__(self):
        self.match += 1

class Menu:
    """Base menu class."""
    def __init__(self, cOpts, *args):
        self.cVars = args
        self.mOpts = "" if exit_menu in [i[1] for i in cOpts] \
            else [('Exit', exit_menu)]
        self.mOpts.extend(cOpts)
        self.mCount = str(len(self.mOpts))
        self.select = True

    def __call__(self, *args, **kwargs):
        while self.select != 0:
            self.display_menu()
            self.do_select()

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
        self.select = int(get_valid_inputs([self.mCount + ' menu options',
                                           'selection']))
        self.mOpts[self.select][1](self.cVars)


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
                if int(item) >= 0 and int(condition[:1]) > int(item):
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