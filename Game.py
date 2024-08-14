import numpy as np
import Player


def starting_turn(player, computer):
    starting_player()
    roll_dice()
    print(f'Your hand: {player.dice}')
    if P1.start:
        print('You begin!')
        print('Place a bet!')
        player.place_bet(player, computer)
    else:
        print('The opponent begins!')
        computer.first_bet()

def starting_player():
    c = Player.coin_flip()
    P1.starting_player(c)
    C1.starting_player(c)
    if P1.start == True:
        P1.turn = True
    elif C1.start == True:
        C1.turn = True

def switch_turn(player, computer):
    if player.turn:
        player.turn, computer.turn = False, True
    else:
        player.turn, computer.turn = True, False

def roll_dice():
    P1.roll()
    C1.roll()

def show_hand():
    if P1.turn:
        print(f'Your hand: {P1.dice}')

def turn(player, computer):
    played = False
    valid = False
    if player.turn:
         show_hand()
         while played == False:
            action = input("Would you like to raise the bet (Type: \"Bet\"), or call bluff (Type: \"Liar\"): ")
            if action.lower() == 'bet':
                played = True
                while not valid:
                    player.place_bet(player, computer)
                    valid = player.valid_bet(computer)
                    if not valid:
                        print('Invalid bet. Please bet again.')
            if action.lower() == 'liar':
                played = True
                player.call_liar(computer)

    if computer.turn:
        c = np.random.randint(0,4)
        if c < 3:
            computer.place_bet(player)
        if c == 3:
            computer.call_liar(player)


def game_over(player, computer):
    if player.lives == 0 or computer.lives == 0:
        return True
    return False
def end_game(player, computer):
    if player.lives > 0:
        print('Congrats! You win.')
    if computer.lives > 0:
        print('You lost. Better luck next time. ')

def directions():
    d = input('Do you know how to play Liar\'s Dice? [Y/N]: ')
    if d.lower() == 'n':
        print('Directions: 1.) Flip a coin to see who begins the game. \n'
              '2.) At the beginning of each round both you and your opponent will roll dice. \n'
              '3.) You and your opponent will take turns betting on the value and number of ALL the dice (Ex. five six\'s),\n but you will only be able to see your own dice. \n'
              '4.) Each bet must be greater than the bet before. \n'
              '5.) Call "Liar" if you believe that your opponent\'s bet is wrong. If you are right then your opponent loses a life and a die from their collection of dice, \n if you are wrong then you lose a life and a die. \n'
              '6.) Each player begins with 5 lives and 5 dice. The first to zero loses. ')

def game(player, computer):
    directions()
    input('Press any key to begin.')
    while not game_over(player, computer):
        player.start = False
        computer.start = False
        player.turn = False
        computer.turn = False
        player.bet = {'Dice': 0, 'Face': 0}
        player.prevBet = {'Dice': 0, 'Face': 0}
        computer.bet = {'Dice': 0, 'Face': 0}
        computer.prevBet = {'Dice': 0, 'Face': 0}
        pw = False
        cw = False
        starting_turn(player, computer)
        switch_turn(player, computer)
        while (pw or cw) == False:
            turn(player, computer)
            switch_turn(player, computer)
            pw = player.has_won(computer)
            cw = computer.has_won(player)

    end_game(player, computer)


P1 = Player.player()
C1 = Player.computer()
game(P1, C1)