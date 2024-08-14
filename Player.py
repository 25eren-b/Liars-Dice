import numpy as np
import random

class player():
    def __init__(self):
        self.dice = []
        self.start = False
        self.turn = False
        self.prevTurn = False
        self.bet = {'Dice': 0, 'Face': 0}
        self.prevBet = {'Dice': 0, 'Face': 0}
        self.lives = 5
        self.win = False

    def roll(self):
        self.dice = []
        oneList = [1] * self.lives
        for n in range(0, self.lives):
            self.dice.append(oneList[n] * np.random.randint(1, 7))

    def starting_player(self, coin):
        if coin == 'head':
            self.start = True
        if coin == 'tail':
            self.start = False
        return self.start

    def place_bet(self, player, computer):
        if self.turn:
            F = int(input('Dice Value: '))
            D = int(input('Number of Dice: '))
            self.bet['Face'] = F
            self.bet['Dice'] = D
            if self.valid_bet(computer):
                print(f'You bet that there are {self.bet["Dice"]} {self.bet["Face"]}\'s')


    def call_liar(self, computer):
        totalDice = self.dice + computer.dice
        sortedDice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        call = computer.bet
        for n in range(1, 7):
            for d in totalDice:
                if n == d:
                    sortedDice[n] += 1

        if call['Dice'] <= sortedDice[int(call['Face'])]:
            computer.win = True
        if call['Dice'] > sortedDice[call['Face']]:
            self.win = True
    def valid_bet(self, computer):
        previousBet = computer.bet
        newBet = self.bet
        if int(previousBet['Dice']) < int(newBet['Dice']):
            return True
        if int(previousBet['Dice']) == int(newBet['Dice']) and int(previousBet['Face']) < int(newBet['Face']):
            return True
        return False

    def has_won(self, computer):
        if self.win:
            computer.lives -= 1
            print(f'You have won the round. You have {self.lives} lives and the opponent has {computer.lives} lives.')
            self.win = False
            return True
        return False






class computer(player):
    def __init__(self):
        self.dice = []
        self.start = False
        self.turn = False
        self.prevTurn = False
        self.bet = {'Dice': 0, 'Face': 0}
        self.lives = 5
        self.win = False

    def starting_player(self, coin):
        if coin == 'tail':
            self.start = True
        if coin == 'head':
            self.start = False
        return self.start

    def first_bet(self):
        print('The opponent is placing a bet.')
        hand = self.dice
        dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for n in range(1,7):
            for d in hand:
                if d == n:
                    dice[n] += 1
        self.bet['Dice'] = max(dice[1], dice[2], dice[3], dice[4], dice[5], dice[6])
        self.bet['Face'] = list(dice.keys())[list(dice.values()).index(self.bet['Dice'])]
        print(f'The opponents bets there are {self.bet["Dice"]} {self.bet["Face"]}\'s')

    def place_bet(self, player):
        prevBet = player.bet
        newBet = {'Dice': 0, 'Face': 0}
        valid = False
        while not valid:
            bidType = np.random.randint(0, 3)
            if prevBet['Dice'] >= player.lives + self.lives and prevBet['Face'] >= 6:
                self.call_liar(player)
                return False
            elif bidType == 0:
                newBet['Dice'] = int(prevBet['Dice']) + 1
                newBet['Face'] = int(prevBet['Face'])
            elif bidType == 1:
                newBet['Dice'] = int(prevBet['Dice']) + 1
                x = int(prevBet['Face'])
                newBet['Face'] = x + random.randint(1-x, 7-x)
            elif bidType == 2:
                newBet['Dice'] = int(prevBet['Dice'])
                x = int(prevBet['Face'])
                newBet['Face'] = x + random.randint(1, 7 - x)
            self.bet = newBet
            valid = self.valid_bet(player)
        print(f'The opponents bets there are {self.bet["Dice"]} {self.bet["Face"]}\'s')

    def valid_bet(self, player):
        if int(self.bet['Face']) <= 6 and int(self.bet['Dice'] <= self.lives + player.lives):
            return True
        return False

    def has_won(self, player):
        if self.win:
            player.lives -= 1
            print(f'The opponent has won the round. You have {player.lives} lives and the opponent has {self.lives} lives.')
            self.win = False
            return True
        return False

    def call_liar(self, player):
        print('The opponent calls bluff.')
        totalDice = self.dice + player.dice
        sortedDice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        call = player.bet
        for n in range(1, 7):
            for d in totalDice:
                if n == d:
                    sortedDice[n] += 1

        if int(call['Dice']) <= int(sortedDice[int(call['Face'])]):
            player.win = True
        if int(call['Dice']) > int(sortedDice[int(call['Face'])]):
            self.win = True


def coin_flip():
    face = ''
    c = np.random.randint(0,2)
    if c == 1:
        face = 'head'
    else:
        face = 'tail'
    return face










