from tkinter import *
import random

class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.usedMoves = []
        self.bonusYahtzees = []
        for i in range(games):
            self.bonusYahtzees.append(0)
        self.dieCount = {"Aces": [], "Twos": [], "Threes": [], "Fours": [], "Fives": [], "Sixes": []}
        self.complexCount = {"3 of a Kind": [], "4 of a Kind": [], "Full House": [], "Small Straight": [], "Large Straight": [], "Yahtzee": [], "Chance": []}
        self.keys = list(self.dieCount.keys())
        for i in range(len(self.keys)):
            for j in range(games):
                self.dieCount[self.keys[i]].append([])
        self.keys = list(self.complexCount.keys())
        for i in range(len(self.keys)):
            for j in range(games):
                self.complexCount[self.keys[i]].append([])
        print(self.dieCount)
        print(self.complexCount)


    def addScore(self, score):
        self.score += score

class Application(Frame):
    def __init__(self, master, playerNames):
        super(Application, self).__init__(master)
        self.grid()
        self.images = [image1, image2, image3, image4, image5, image6]
        self.players = []
        for i in range(len(playerNames)):
            self.players.append(Player(playerNames[i]))
        self.currentPlayer = 0
        self.game = 1
        self.round = 1
        self.rounds = 13
        self.rolls = 0
        self.selectedDie = [True, True, True, True, True]
        self.dieNumbers = [image0, image0, image0, image0, image0]
        self.getScores()

        self.bind("<Button-3>", self.showScores)
        self.create_widgets()

    def showScores(self, event):
        root2 = Tk()
        app2 = Scores(root2, self.players, self.currentPlayer)
        root2.mainloop()

    def rollAll(self):
        if self.rolls < 3 and True in self.selectedDie:
            self.rolls += 1
            self.rollAllDie["text"] = "Roll Selected Die (Remaining: %d)" % (3 - self.rolls)
            for i in range(len(self.dieNumbers)):
                if self.selectedDie[i]:
                    self.dieNumbers[i] = random.choice(self.images)

            if self.selectedDie[0]:
                self.dice1["image"] = self.dieNumbers[0]
            if self.selectedDie[1]:
                self.dice2["image"] = self.dieNumbers[1]
            if self.selectedDie[2]:
                self.dice3["image"] = self.dieNumbers[2]
            if self.selectedDie[3]:
                self.dice4["image"] = self.dieNumbers[3]
            if self.selectedDie[4]:
                self.dice5["image"] = self.dieNumbers[4]

            for i in range(len(self.selectedDie)):
                self.selectedDie[i] = False

            self.dice1["bg"] = "white"
            self.dice2["bg"] = "white"
            self.dice3["bg"] = "white"
            self.dice4["bg"] = "white"
            self.dice5["bg"] = "white"

            self.getPossibleMoves()

    def roll1(self):
        if self.selectedDie[0] == False:
            self.selectedDie[0] = True
            self.dice1["bg"] = "red"
        else:
            self.selectedDie[0] = False
            self.dice1["bg"] = "white"

    def roll2(self):
        if self.selectedDie[1] == False:
            self.selectedDie[1] = True
            self.dice2["bg"] = "red"
        else:
            self.selectedDie[1] = False
            self.dice2["bg"] = "white"

    def roll3(self):
        if self.selectedDie[2] == False:
            self.selectedDie[2] = True
            self.dice3["bg"] = "red"
        else:
            self.selectedDie[2] = False
            self.dice3["bg"] = "white"

    def roll4(self):
        if self.selectedDie[3] == False:
            self.selectedDie[3] = True
            self.dice4["bg"] = "red"
        else:
            self.selectedDie[3] = False
            self.dice4["bg"] = "white"

    def roll5(self):
        if self.selectedDie[4] == False:
            self.selectedDie[4] = True
            self.dice5["bg"] = "red"
        else:
            self.selectedDie[4] = False
            self.dice5["bg"] = "white"

    def getPossibleMoves(self):
        self.possibleMoves = {}
        self.rolledDie = []
        for i in range(len(self.dieNumbers)):
            self.rolledDie.append(int(self.dieNumbers[i].name[-1])-1)
        for i in range(1, 7):
            if self.rolledDie.count(i) >= 3:
                self.possibleMoves["3 of a Kind"] = i
                for j in range(1, 7):
                    if self.rolledDie.count(j) == 2 and j != i:
                        self.possibleMoves["Full House"] = [i, j]
            if self.rolledDie.count(i) >= 4:
                self.possibleMoves["4 of a Kind"] = i
            if self.rolledDie.count(i) == 5:
                self.possibleMoves["Yahtzee"] = i
                if "Yahtzee" in self.players[self.currentPlayer].usedMoves:
                    self.players[self.currentPlayer].bonusYahtzees[self.game-1] += 1

        self.rolledDie2 = []
        self.rolledDie2.append(self.rolledDie)
        self.rolledDie2.append(self.rolledDie[:4])
        self.rolledDie2.append(self.rolledDie[1:])
        self.rolledDie2.append([self.rolledDie[0], self.rolledDie[2], self.rolledDie[3], self.rolledDie[4]])
        self.rolledDie2.append([self.rolledDie[0], self.rolledDie[1], self.rolledDie[3], self.rolledDie[4]])
        self.rolledDie2.append([self.rolledDie[0], self.rolledDie[1], self.rolledDie[2], self.rolledDie[4]])

        for i in range(len(self.rolledDie2)):
            if sorted(self.rolledDie2[i]) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]:
                if i == 0:
                    self.possibleMoves["Large Straight"] = sorted(self.rolledDie2[i])
                else:
                    self.possibleMoves["Small Straight"] = sorted(self.rolledDie2[i])

        self.moves = list(self.possibleMoves.keys())
        if "3 of a Kind" in self.moves and not("3 of a Kind" in self.players[self.currentPlayer].usedMoves):
            self.threeKindButton["bg"] = "blue"
        else:
            if "3 of a Kind" in self.players[self.currentPlayer].usedMoves:
                self.threeKindButton["bg"] = "lime"
            else:
                self.threeKindButton["bg"] = "gray"
        if "4 of a Kind" in self.moves and not("4 of a Kind" in self.players[self.currentPlayer].usedMoves):
            self.fourKindButton["bg"] = "blue"
        else:
            if "4 of a Kind" in self.players[self.currentPlayer].usedMoves:
                self.fourKindButton["bg"] = "lime"
            else:
                self.fourKindButton["bg"] = "gray"
        if "Yahtzee" in self.moves and not("Yahtzee" in self.players[self.currentPlayer].usedMoves):
            self.yahtzeeButton["bg"] = "blue"
        else:
            if "Yahtzee" in self.players[self.currentPlayer].usedMoves:
                self.yahtzeeButton["bg"] = "lime"
            else:
                self.yahtzeeButton["bg"] = "gray"
        if "Full House" in self.moves and not("Full House" in self.players[self.currentPlayer].usedMoves):
            self.fullHouseButton["bg"] = "blue"
        else:
            if "Full House" in self.players[self.currentPlayer].usedMoves:
                self.fullHouseButton["bg"] = "lime"
            else:
                self.fullHouseButton["bg"] = "gray"
        if "Small Straight" in self.moves and not("Small Straight" in self.players[self.currentPlayer].usedMoves):
            self.smallStraightButton["bg"] = "blue"
        else:
            if "Small Straight" in self.players[self.currentPlayer].usedMoves:
                self.smallStraightButton["bg"] = "lime"
            else:
                self.smallStraightButton["bg"] = "gray"
        if "Large Straight" in self.moves and not("Large Straight" in self.players[self.currentPlayer].usedMoves):
            self.largeStraightButton["bg"] = "blue"
        else:
            if "Large Straight" in self.players[self.currentPlayer].usedMoves:
                self.largeStraightButton["bg"] = "lime"
            else:
                self.largeStraightButton["bg"] = "gray"
        if not("Chance" in self.players[self.currentPlayer].usedMoves):
            self.chanceButton["bg"] = "blue"
        else:
            if "Chance" in self.players[self.currentPlayer].usedMoves:
                self.chanceButton["bg"] = "lime"
            else:
                self.chanceButton["bg"] = "gray"
        if not("Aces" in self.players[self.currentPlayer].usedMoves):
            self.acesButton["bg"] = "blue"
        else:
            if "Aces" in self.players[self.currentPlayer].usedMoves:
                self.acesButton["bg"] = "lime"
            else:
                self.acesButton["bg"] = "gray"
        if not("Twos" in self.players[self.currentPlayer].usedMoves):
            self.twosButton["bg"] = "blue"
        else:
            if "Twos" in self.players[self.currentPlayer].usedMoves:
                self.twosButton["bg"] = "lime"
            else:
                self.twosButton["bg"] = "gray"
        if not("Threes" in self.players[self.currentPlayer].usedMoves):
            self.threesButton["bg"] = "blue"
        else:
            if "Threes" in self.players[self.currentPlayer].usedMoves:
                self.threesButton["bg"] = "lime"
            else:
                self.threesButton["bg"] = "gray"
        if not("Fours" in self.players[self.currentPlayer].usedMoves):
            self.foursButton["bg"] = "blue"
        else:
            if "Fours" in self.players[self.currentPlayer].usedMoves:
                self.foursButton["bg"] = "lime"
            else:
                self.foursButton["bg"] = "gray"
        if not("Fives" in self.players[self.currentPlayer].usedMoves):
            self.fivesButton["bg"] = "blue"
        else:
            if "Fives" in self.players[self.currentPlayer].usedMoves:
                self.fivesButton["bg"] = "lime"
            else:
                self.fivesButton["bg"] = "gray"
        if not("Sixes" in self.players[self.currentPlayer].usedMoves):
            self.sixesButton["bg"] = "blue"
        else:
            if "Sixes" in self.players[self.currentPlayer].usedMoves:
                self.sixesButton["bg"] = "lime"
            else:
                self.sixesButton["bg"] = "gray"

        print(self.rolledDie)
        print(self.possibleMoves)
        return self.possibleMoves

    def newGame(self):
        self.game += 1
        self.round = 1
        self.showScores(self)

    def nextPlayer(self):
        self.currentPlayer = (self.currentPlayer + 1) % len(self.players)
        self.rolls = 0
        self.rollAllDie["text"] = "Roll Selected Die (Remaining: %d)" % (3 - self.rolls)

        if self.currentPlayer == 0:
            self.round += 1

        if self.round > self.rounds:
            self.newGame()

        self.dice1["image"] = image0
        self.dice2["image"] = image0
        self.dice3["image"] = image0
        self.dice4["image"] = image0
        self.dice5["image"] = image0

        if "Aces" in self.players[self.currentPlayer].usedMoves:
            self.acesButton["bg"] = "lime"
        else:
            self.acesButton["bg"] = "gray"
        if "Twos" in self.players[self.currentPlayer].usedMoves:
            self.twosButton["bg"] = "lime"
        else:
            self.twosButton["bg"] = "gray"
        if "Threes" in self.players[self.currentPlayer].usedMoves:
            self.threesButton["bg"] = "lime"
        else:
            self.threesButton["bg"] = "gray"
        if "Fours" in self.players[self.currentPlayer].usedMoves:
            self.foursButton["bg"] = "lime"
        else:
            self.foursButton["bg"] = "gray"
        if "Fives" in self.players[self.currentPlayer].usedMoves:
            self.fivesButton["bg"] = "lime"
        else:
            self.fivesButton["bg"] = "gray"
        if "Sixes" in self.players[self.currentPlayer].usedMoves:
            self.sixesButton["bg"] = "lime"
        else:
            self.sixesButton["bg"] = "gray"

        if "3 of a Kind" in self.players[self.currentPlayer].usedMoves:
            self.threeKindButton["bg"] = "lime"
        else:
            self.threeKindButton["bg"] = "gray"
        if "4 of a Kind" in self.players[self.currentPlayer].usedMoves:
            self.fourKindButton["bg"] = "lime"
        else:
            self.fourKindButton["bg"] = "gray"
        if "Yahtzee" in self.players[self.currentPlayer].usedMoves:
            self.yahtzeeButton["bg"] = "lime"
        else:
            self.yahtzeeButton["bg"] = "gray"
        if "Full House" in self.players[self.currentPlayer].usedMoves:
            self.fullHouseButton["bg"] = "lime"
        else:
            self.fullHouseButton["bg"] = "gray"
        if "Small Straight" in self.players[self.currentPlayer].usedMoves:
            self.smallStraightButton["bg"] = "lime"
        else:
            self.smallStraightButton["bg"] = "gray"
        if "Large Straight" in self.players[self.currentPlayer].usedMoves:
            self.largeStraightButton["bg"] = "lime"
        else:
            self.largeStraightButton["bg"] = "gray"
        if "Chance" in self.players[self.currentPlayer].usedMoves:
            self.chanceButton["bg"] = "lime"
        else:
            self.chanceButton["bg"] = "gray"

        self.selectedDie[0] = True
        self.dice1["bg"] = "red"
        self.selectedDie[1] = True
        self.dice2["bg"] = "red"
        self.selectedDie[2] = True
        self.dice3["bg"] = "red"
        self.selectedDie[3] = True
        self.dice4["bg"] = "red"
        self.selectedDie[4] = True
        self.dice5["bg"] = "red"

        self.titleLabel["text"] = "Yahtzee!  |  Player: " + self.players[self.currentPlayer].name + "  |  Round: " + str(self.round) + "  |  Game: " + str(self.game)

    def aces(self):
        if self.acesButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Aces")
            self.players[self.currentPlayer].dieCount["Aces"][self.game - 1] = (self.rolledDie)
            self.acesButton["bg"] = "gray"
            self.nextPlayer()

    def twos(self):
        if self.twosButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Twos")
            self.players[self.currentPlayer].dieCount["Twos"][self.game - 1] = (self.rolledDie)
            self.twosButton["bg"] = "gray"
            self.nextPlayer()

    def threes(self):
        if self.threesButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Threes")
            self.players[self.currentPlayer].dieCount["Threes"][self.game - 1] = (self.rolledDie)
            self.threesButton["bg"] = "gray"
            self.nextPlayer()

    def fours(self):
        if self.foursButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Fours")
            self.players[self.currentPlayer].dieCount["Fours"][self.game - 1] = (self.rolledDie)
            self.foursButton["bg"] = "gray"
            self.nextPlayer()

    def fives(self):
        if self.fivesButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Fives")
            self.players[self.currentPlayer].dieCount["Fives"][self.game - 1] = (self.rolledDie)
            self.fivesButton["bg"] = "gray"
            self.nextPlayer()

    def sixes(self):
        if self.sixesButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Sixes")
            self.players[self.currentPlayer].dieCount["Sixes"][self.game - 1] = (self.rolledDie)
            self.sixesButton["bg"] = "gray"
            self.nextPlayer()

    def yahtzee(self):
        if self.yahtzeeButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Yahtzee")
            self.players[self.currentPlayer].complexCount["Yahtzee"][self.game-1] = (self.rolledDie)
            self.yahtzeeButton["bg"] = "gray"
            self.nextPlayer()

    def chance(self):
        if self.chanceButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Chance")
            self.players[self.currentPlayer].complexCount["Chance"][self.game-1] = (self.rolledDie)
            self.chanceButton["bg"] = "gray"
            self.nextPlayer()

    def smallStraight(self):
        if self.smallStraightButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Small Straight")
            self.players[self.currentPlayer].complexCount["Small Straight"][self.game-1] = (self.rolledDie)
            self.smallStraightButton["bg"] = "gray"
            self.nextPlayer()

    def largeStraight(self):
        if self.largeStraightButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Large Straight")
            self.players[self.currentPlayer].complexCount["Large Straight"][self.game-1] = (self.rolledDie)
            self.largeStraightButton["bg"] = "gray"
            self.nextPlayer()

    def threeKind(self):
        if self.threeKindButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("3 of a Kind")
            self.players[self.currentPlayer].complexCount["3 of a Kind"][self.game - 1] = (self.rolledDie)
            self.threeKindButton["bg"] = "gray"
            self.nextPlayer()

    def fourKind(self):
        if self.fourKindButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("4 of a Kind")
            self.players[self.currentPlayer].complexCount["4 of a Kind"][self.game-1] = (self.rolledDie)
            self.fourKindButton["bg"] = "gray"
            self.nextPlayer()

    def fullHouse(self):
        if self.fullHouseButton["bg"] == "blue":
            self.players[self.currentPlayer].usedMoves.append("Full House")
            self.players[self.currentPlayer].complexCount["Full House"][self.game-1] = (self.rolledDie)
            self.fullHouseButton["bg"] = "gray"
            self.nextPlayer()

    def getScores(self):
        self.scores = ""
        for i in range(len(self.players)):
            self.scores += self.players[i].name + ":\t" + str(self.players[i].score) + "\n"
        self.scores = self.scores[:-1]
        return self.scores

    def create_widgets(self):
        self.titleLabel = Label(self, text="Yahtzee!  |  Player: " + self.players[self.currentPlayer].name + "  |  Round: " + str(self.round) + "  |  Game: " + str(self.game), width=41, height=1, bg="red", fg="black", font=("Cooper Black", 30))
        self.titleLabel.grid(row=0, column=0, columnspan=10, sticky=E)

        Label(self, width=1, height=1).grid(row=1, column=0)

        self.acesButton = Button(self, width=12, text="Aces", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.aces)
        self.acesButton.grid(row=2, column=1, columnspan=3, sticky=W)

        self.twosButton = Button(self, width=12, text="Twos", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.twos)
        self.twosButton.grid(row=2, column=4, columnspan=3)

        self.threesButton = Button(self, width=12, text="Threes", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.threes)
        self.threesButton.grid(row=2, column=7, columnspan=3, sticky=E)

        Label(self, width=1, height=1).grid(row=3, column=0)

        self.foursButton = Button(self, width=12, text="Fours", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.fours)
        self.foursButton.grid(row=4, column=1, columnspan=3, sticky=W)

        self.fivesButton = Button(self, width=12, text="Fives", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.fives)
        self.fivesButton.grid(row=4, column=4, columnspan=3)

        self.sixesButton = Button(self, width=12, text="Sixes", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.sixes)
        self.sixesButton.grid(row=4, column=7, columnspan=3, sticky=E)

        Label(self, width=1, height=1).grid(row=5, column=0)

        self.threeKindButton = Button(self, width=10, text="3 of a Kind", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.threeKind)
        self.threeKindButton.grid(row=6, column=1, columnspan=2, sticky=W)

        self.fourKindButton = Button(self, width=10, text="4 of a Kind", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.fourKind)
        self.fourKindButton.grid(row=6, column=3, columnspan=2, sticky=W)

        self.smallStraightButton = Button(self, width=14, text="Small Straight (4)", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.smallStraight)
        self.smallStraightButton.grid(row=6, column=5, columnspan=3, sticky=W)

        self.largeStraightButton = Button(self, width=14, text="Large Straight (5)", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.largeStraight)
        self.largeStraightButton.grid(row=6, column=7, columnspan=3, sticky=E)

        Label(self, width=1, height=1).grid(row=7, column=0)

        self.fullHouseButton = Button(self, width=12, text="Full House", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.fullHouse)
        self.fullHouseButton.grid(row=8, column=1, columnspan=3, sticky=W)

        self.yahtzeeButton = Button(self, width=12, text="Yahtzee!", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.yahtzee)
        self.yahtzeeButton.grid(row=8, column=4, columnspan=3)

        self.chanceButton = Button(self, width=12, text="Chance", font=("Cooper Black", 24), bg="gray", fg="white", activebackground="gray", command=self.chance)
        self.chanceButton.grid(row=8, column=7, columnspan=3, sticky=E)

        Label(self, width=1, height=1).grid(row=9, column=0)

        self.rollAllDie = Button(self, width=31, text="Roll Selected Die (Remaining: %d)" % (3-self.rolls), font=("Cooper Black", 24), bg="blue", fg="white", activebackground="blue", command=self.rollAll)
        self.rollAllDie.grid(row=10, column=1, columnspan=6, sticky=W)

        self.advancePlayer = Button(self, width=15, text="Next Player", font=("Cooper Black", 24), bg="blue", fg="white", activebackground="blue", command=self.nextPlayer)
        self.advancePlayer.grid(row=10, column=7, columnspan=3, sticky=E)

        Label(self, width=1, height=1).grid(row=11, column=0)

        Label(self, width=12, height=1).grid(row=12, column=0)

        self.dice1 = Button(self, image=image0, bd=5, activebackground="red", bg="red", command=self.roll1)
        self.dice1.grid(row=12, column=1)

        Label(self, width=10, height=1).grid(row=12,  column=2)

        self.dice2 = Button(self, image=image0, bd=5, activebackground="red", bg="red", command=self.roll2)
        self.dice2.grid(row=12, column=3)

        Label(self, width=10, height=1).grid(row=12, column=4)

        self.dice3 = Button(self, image=image0, bd=5, activebackground="red", bg="red", command=self.roll3)
        self.dice3.grid(row=12, column=5)

        Label(self, width=10, height=1).grid(row=12, column=6)

        self.dice4 = Button(self, image=image0, bd=5, activebackground="red", bg="red", command=self.roll4)
        self.dice4.grid(row=12, column=7)

        Label(self, width=10, height=1).grid(row=12, column=8)

        self.dice5 = Button(self, image=image0, bd=5, activebackground="red", bg="red", command=self.roll5)
        self.dice5.grid(row=12, column=9)

        Label(self, width=10, height=1).grid(row=13, column=8)

import time

class Scores(Frame):
    def __init__(self, master, players, playerLocation):
        super(Scores, self).__init__(master)
        self.grid()
        self.players = players
        self.playerLocation = playerLocation
        self.create_widgets()

    def change_scoreCard(self, event):
        if event.keycode == 37:
            self.playerLocation = (self.playerLocation - 1 + len(self.players)) % len(self.players)
            print(self.playerLocation)
            self.nameLabel["text"] = "Name: " + self.players[self.playerLocation].name
            self.fill_grid(self.players[self.playerLocation])
            time.sleep(0.25)
        elif event.keycode == 39:
            self.playerLocation = (self.playerLocation + 1) % len(self.players)
            print(self.playerLocation)
            self.nameLabel["text"] = "Name: " + self.players[self.playerLocation].name
            self.fill_grid(self.players[self.playerLocation])
            time.sleep(0.25)

    def create_widgets(self):
        self.bind("<Key>", self.change_scoreCard)
        self.focus_set()

        self.font = ("Cooper Black", 7)
        Label(self, text="Yahtzee", font=("Cooper Black", 16), relief="solid").grid(row=0, column=0, columnspan=3)
        self.nameLabel = Label(self, text="Name: " + self.players[self.playerLocation].name, font=("Cooper Black", 16), relief="solid")
        self.nameLabel.grid(row=0, column=3, columnspan=5)

        self.headings = ["UPPER SECTION", "HOW TO\nSCORE"]
        for i in range(games):
            self.headings.append("GAME\n#" + str(i+1))

        for i in range(len(self.headings)):
            if i <= 1:
                Label(self, text=self.headings[i], font=self.font, relief="solid", height=2, width=20).grid(row=1, column=i)
            else:
                Label(self, text=self.headings[i], font=self.font, relief="solid", height=2, width=8).grid(row=1, column=i)

        self.headings = ["ACES = 1", "TWOS = 2", "THREES = 3", "FOURS = 4", "FIVES = 5", "SIXES = 6", "TOTAL SCORE", "BONUS\n(IF SCORE>=63)", "TOTAL\n(OF UPPER SECTION)", "LOWER SECTION", "3 OF A KIND", "4 OF A KIND", "FULL HOUSE", "SMALL STRAIGHT\n(SEQUENCE OF FOUR)", "LARGE STRAIGHT\n(SEQUENCE OF FIVE)", "YAHTZEE\n(5 OF A KIND)", "CHANCE", "YAHTZEE\nBONUS", "TOTAL\n(OF LOWER SECTION)", "TOTAL\n(OF UPPER SECTION)", "GRAND TOTAL"]

        for i in range(len(self.headings)):
            if i < 17:
                Label(self, text=self.headings[i], font=self.font, relief="solid", width=20, height=2).grid(row=2+i, column=0)
            elif i > 17:
                Label(self, text=self.headings[i], font=self.font, relief="solid", width=20, height=2).grid(row=3+i, column=0)
            else:
                Label(self, text=self.headings[i], font=self.font, relief="solid", width=20, height=5).grid(row=2+i, column=0, rowspan=2)
                i += 1

        self.headings = ["COUNT AND ADD\nONLY ACES", "COUNT AND ADD\nONLY TWOS", "COUNT AND ADD\nONLY THREES", "COUNT AND ADD\nONLY FOURS", "COUNT AND ADD\nONLY FIVES", "COUNT AND ADD\nONLY SIXES", "---------->", "SCORE 35", "---------->", "", "ADD TOTAL\nOF ALL DICE", "ADD TOTAL\nOF ALL DICE", "SCORE 25", "SCORE 30", "SCORE 40", "SCORE 50", "SCORE TOTAL\nOF ALL 5 DICE", chr(10003) + " FOR\nEACH BONUS", "SCORE 100\nPER " + chr(10003), "---------->", "---------->", "---------->"]

        for i in range(len(self.headings)):
            Label(self, text=self.headings[i], font=self.font, relief="solid", width=20, height=2).grid(row=2+i, column=1)

        self.fill_grid(self.players[self.playerLocation])

    def fill_grid(self, gridPlayer):
        self.boxFillers = []
        for i in range(games):
            self.boxFillers.append([])

            self.boxFillers[i].append(gridPlayer.dieCount["Aces"][i].count(1)*1)
            self.boxFillers[i].append(gridPlayer.dieCount["Twos"][i].count(2)*2)
            self.boxFillers[i].append(gridPlayer.dieCount["Threes"][i].count(3)*3)
            self.boxFillers[i].append(gridPlayer.dieCount["Fours"][i].count(4)*4)
            self.boxFillers[i].append(gridPlayer.dieCount["Fives"][i].count(5)*5)
            self.boxFillers[i].append(gridPlayer.dieCount["Sixes"][i].count(6)*6)

            self.boxFillers[i].append(sum(self.boxFillers[i][0:6]))
            if self.boxFillers[i][6] >= 63:
                self.boxFillers[i].append(35)
            else:
                self.boxFillers[i].append(0)
            self.boxFillers[i].append(self.boxFillers[i][6] + self.boxFillers[i][7])

            self.boxFillers[i].append("")

            self.boxFillers[i].append(sum(gridPlayer.complexCount["3 of a Kind"][i]))
            self.boxFillers[i].append(sum(gridPlayer.complexCount["4 of a Kind"][i]))
            if len(gridPlayer.complexCount["Full House"][i]) != 0:
                self.boxFillers[i].append(25)
            else:
                self.boxFillers[i].append(0)
            if len(gridPlayer.complexCount["Small Straight"][i]) != 0:
                self.boxFillers[i].append(30)
            else:
                self.boxFillers[i].append(0)
            if len(gridPlayer.complexCount["Large Straight"][i]) != 0:
                self.boxFillers[i].append(40)
            else:
                self.boxFillers[i].append(0)
            if len(gridPlayer.complexCount["Yahtzee"][i]) != 0:
                self.boxFillers[i].append(50)
            else:
                self.boxFillers[i].append(0)
            self.boxFillers[i].append(sum(gridPlayer.complexCount["Chance"][i]))

            self.boxFillers[i].append(chr(10003)*gridPlayer.bonusYahtzees[i])
            self.boxFillers[i].append(self.boxFillers[i][17].count(chr(10003))*100)
            self.boxFillers[i].append(sum(self.boxFillers[i][10:17])+self.boxFillers[i][18])
            self.boxFillers[i].append(self.boxFillers[i][8])
            self.boxFillers[i].append(self.boxFillers[i][19]+self.boxFillers[i][20])

        for i in range(games):
            for j in range(len(self.boxFillers[i])):
                Label(self, text=self.boxFillers[i][j], font=("Cooper Black", 12), width=5, height=1, relief="solid").grid(row=2+j, column=2+i)


root = Tk()
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
image0 = PhotoImage(file="Dice0.png")
image1 = PhotoImage(file="Dice1.png")
image2 = PhotoImage(file="Dice2.png")
image3 = PhotoImage(file="Dice3.png")
image4 = PhotoImage(file="Dice4.png")
image5 = PhotoImage(file="Dice5.png")
image6 = PhotoImage(file="Dice6.png")
playerNames = ["Tyler", "Dad"]
games = 6

app1 = Application(root, playerNames)

root.mainloop()