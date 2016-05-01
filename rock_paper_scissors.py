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
    # Displays an introduction to the program and describes what it does.
    fluffy_intro()

    return None


# Section Block: Input Validation ------------------------------------------->
# TODO: get_valid_inputs: [menu_options integer, username string len(10)]
# TODO: Can convert to class since I need at least 2 validators.
# TODO:     valid_menu = Validation(menu_request_list)
# TODO:     valid_name = Validation(name_request_list)
# TODO: OR! baseclass Validation. subclasses: valid_name, valid_menu
# get_valid_inputs requests input from the user then tests the input.
#   If invalid, it will alert the user and request the correct input.
# The parameter is a nested List of ordered pair Lists.
#   First value is the validation test and second is the user prompt.
def get_valid_inputs(requestsList):
    # local List to hold user inputs for return to calling module
    userInputs = []

    # Loop through each entry in requestsList assigning each List pair
    #  to request.
    for request in requestsList:
        # untestedInput is a holding variable for testing user input validity.
        # First user prompt before testing loop.
        untestedInput = prompt_user_for_input(request[1])

        # If test_value returns True, Not converts it to False and the While
        #   Loop will not execute.
        # If test_value returns False, the While executes and the user is
        #   prompted to enter a valid value.
        while not test_value(request[0], untestedInput):
            print('!!! Error: {} is not a valid value.'.format(untestedInput))
            untestedInput = (prompt_user_for_input(request[1]))

        # The user input tested valid and is appended to the userInputs List.
        userInputs.append(untestedInput)
    # for loop terminates and userInputs are returned to calling Module.
    # With only a single test run in this program, only the first value
    #   in userInputs is returned.
    return userInputs[0]


# prompt_user_for_item is passed a String to print to screen as part of a user
#   prompt.  Then returns it to the calling module.
def prompt_user_for_input(promptTerm):
    # promptTerm is a local variable to hold the value passed from the
    #   calling module.
    print('Please enter your {}.'.format(promptTerm))
    return input('  >>> ')


# test_value uses the testCondition to select the proper test.
# True or False is returned to the calling Module.
def test_value(testCondition, testItem):
    # The If-Then-Else structure functions as a Switch for test selection.
    if testCondition[1:] == ' menu options':
        # The number of menu items is prepended to the test condition string.
        #   testCondition[1:] strips the first character and then does the
        #   string comparison.
        # If (the number of menu items) is greater than int(testItem) and
        #   int(testItem) is greater than or equal to zero, True is
        #   returned.  If int(testItem) creates an error or fails the other
        #   logic tests, False is returned.
        try:
            if int(testItem) >= 0 and int(testCondition[:1]) > int(testItem):
                valid = True
            else:
                valid = False
        except:
            valid = False
    elif testCondition == 'integer':
        try:
            int(testItem)
            valid = True
        except:
            valid = False
    else:
        valid = None
    return valid
# <<------------ End Block--------------------------------------------------<<

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

# Section Block: Misc ------------------------------------------------------->
# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print("Welcome to RPS sim.")
    return None

# Getto style clear console screen by newline flooding.
def clear(n=50):
    print("\n" * n)
    return None

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

    def __str__(self):
        r = ""
        for p in self.players:
            r += p

    def __pos__(self): # +Game increments the round counter.
        self.round += 1

    def judge(self, attack):
        if len(self.attacks) == 2:
            self.attacks = attack
        else:
            self.attacks += attack

        if self.attacks in self.moves[0:2]: # P1 wins
            self.winner(0)
        elif self.attacks in self.moves[3:5]: # P2 wins
            self.winner(1)
        else: # Tie round
            self.winner(2)

    # Updates player object and match
    # noinspection PyStatementEffect
    def winner(self, w, l=2):
        self.match_score[w] += 1
        if n != 2:
            +self.players[w]
            -self.players[l]


class Tournament:
    """initialized with main menu.  Tracks player stats between games."""
    def __init__(self):
        self.match = 1

    def __pos__(self):
        self.match += 1

class Menu:
    """Base menu class."""
    def __init__(self, cOpts, cVars):
        self.cVars = cVars
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



