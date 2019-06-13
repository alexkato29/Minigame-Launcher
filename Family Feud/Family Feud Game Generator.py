file = open("Original Options.txt", "r")
originalDocument = file.read().split("\n")
file.close()
newDocument = []
oldLocation = -1
for i in range(len(originalDocument)):
    if originalDocument[i] == "~":
        newDocument.append(originalDocument[oldLocation+1:i])
        oldLocation = i

information = []
for i in range(len(newDocument)):
    information.append([newDocument[i][0].upper()])
    information[i].append({})
    del newDocument[i][0]
    del newDocument[i][0]
    del newDocument[i][0]

    for j in range(0, (len(newDocument[i])), 2):
        key = newDocument[i][j][3:]
        value = int(newDocument[i][j+1])
        information[i][1][key.upper()] = value

"""******************************************************************************************************************"""

file = open("Original Options 2.txt", "r")
originalDocument = file.read().split("GAME #")
file.close()
originalDocument.remove(originalDocument[0])
for i in range(len(originalDocument)):
    originalDocument[i] = originalDocument[i].split("\nANSWERS POINTS ANSWERS POINTS\n")

for i in range(len(originalDocument)):
    del originalDocument[i][3]
    del originalDocument[i][3]
    del originalDocument[i][3]
    del originalDocument[i][3]
    del originalDocument[i][3]

for i in range(len(originalDocument)):
    for j in range(len(originalDocument[i])):
        originalDocument[i][j] = originalDocument[i][j].split("\n1.")

for i in range(len(originalDocument)):
    originalDocument[i] = [[originalDocument[i][0][0][2:].strip(), originalDocument[i][-1][-1][1:]], [originalDocument[i][1][0], originalDocument[i][-1][-2][1:]], [originalDocument[i][2], originalDocument[i][-1][-3][1:]]]

newDocument = []

for i in range(len(originalDocument)):
    newDocument.append(originalDocument[i][0])
    newDocument.append(originalDocument[i][1])
    newDocument.append(originalDocument[i][2][0])
    newDocument[(3*i)+2].append(originalDocument[i][2][1])

for i in range(len(newDocument)):
    newDocument[i][0] = newDocument[i][0][8:].replace("\n", " ")
    newDocument[i][1] = newDocument[i][1].split("\n")

for i in range(len(newDocument)):
    del newDocument[i][1][-1]
    for j in range(len(newDocument[i][1])-1):
        newDocument[i][1][j+1] = newDocument[i][1][j+1][3:]

del newDocument[8]
del newDocument[2]

for i in range(len(newDocument)):
    for j in range(len(newDocument[i][1])):
        if newDocument[i][1][j][-2] == " ":
            newDocument[i][1][j] = [newDocument[i][1][j][:-2], int(newDocument[i][1][j][-1])]
        else:
            newDocument[i][1][j] = [newDocument[i][1][j][:-3], int(newDocument[i][1][j][-2:])]

for i in range(len(newDocument)):
    information.append([newDocument[i][0], {}])
    for j in range(len(newDocument[i][1])):
        information[-1][1][newDocument[i][1][j][0]] = newDocument[i][1][j][1]

"""******************************************************************************************************************"""

file = open("Original Options 3.txt", "r")
originalDocument = file.read().split("\n\n")
file.close()

for i in range(len(originalDocument)):
    originalDocument[i] = originalDocument[i].split("\n")

for i in range(len(originalDocument)):
    for j in range(len(originalDocument[i])-1):
        originalDocument[i][j+1] = originalDocument[i][j+1].split("-")

for i in range(len(originalDocument)):
    information.append([originalDocument[i][0].upper(), {}])
    for j in range(len(originalDocument[i])-1):
        information[-1][1][originalDocument[i][j+1][0].upper()] = int(originalDocument[i][j+1][1])

"""******************************************************************************************************************"""

file = open("Original Options 4.txt", "r", encoding="utf8")
originalDocument = file.read().split("\n")
file.close()

for i in range(len(originalDocument)):
    originalDocument[i] = originalDocument[i].split("\t")

deleters = []

for i in range(len(originalDocument)):
    if "" in originalDocument[i]:
        deleters.append(i)

for i in range(len(deleters)-1, -1, -1):
    originalDocument.remove(originalDocument[deleters[i]])

for i in range(len(originalDocument)):
    information.append([originalDocument[i][0].upper(), {}])
    for j in range(0, len(originalDocument[i])-2, 2):
        information[-1][1][originalDocument[i][j+1].upper()] = int(originalDocument[i][j+2])

#team1 = input("What is the name of team 1? ")
team1 = "Team 1"
#team2 = input("What is the name of team 2? ")
team2 = "Team 2"

"""^^^READING FILE AND CREATING THE LIST AND DICTIONARIES^^^"""
from tkinter import *
import random
import winsound

font = "Arial"
team1Score = 0
team2Score = 0
answerTexts = ["", "", "", "", "", "", "", ""]
answers = ["", "", "", "", "", "", "", ""]
answerPointValues = [0, 0, 0, 0, 0, 0, 0, 0]
Xs = ["gray", "gray", "gray"]
chosenQuestions = []
#question = "Name a Reason That Your Boss Would Give You a Raise (Other Than That You Work Hard)"
question = ""
timeLimit = 10
#"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

class Application3(Frame):
    def __init__(self, master):
        super(Application3, self).__init__(master)
        self.grid()
        self.create_widgets()

    def playOne(self):
        winsound.PlaySound("Commercial Break Complete.wav", winsound.SND_FILENAME)

    def playTwo(self):
        winsound.PlaySound("Theme Song Complete.wav", winsound.SND_FILENAME)

    def playThree(self):
        winsound.PlaySound("Times Up Complete.wav", winsound.SND_FILENAME)

    def playFour(self):
        winsound.PlaySound("Buzz In Complete.wav", winsound.SND_FILENAME)

    def create_widgets(self):
        self.one = Button(self, text="Commercial Break\nMusic", font=(font, 20), width=14, height=5, bg="blue", fg="black", activebackground="lime", command=self.playOne)
        self.one.grid(row=0, column=0)

        self.two = Button(self, text="Theme Song\nMusic", font=(font, 20), width=14, height=5, bg="blue", fg="black", activebackground="lime", command=self.playTwo)
        self.two.grid(row=0, column=1)

        self.three = Button(self, text="Times Up\nSound", font=(font, 20), width=14, height=5, bg="blue", fg="black", activebackground="lime", command=self.playThree)
        self.three.grid(row=1, column=0)

        self.four = Button(self, text="Buzz In\n(Faceoff) Sound", font=(font, 20), width=14, height=5, bg="blue", fg="black", activebackground="lime", command=self.playFour)
        self.four.grid(row=1, column=1)

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def optimize(self, question):

        if len(question) < 20:
            return question

        index1 = len(question)//3
        index2 = (len(question)//3)*2
        character1 = question[index1]
        character2 = question[index2]
        while character1 != " ":
            index1 += 1
            character1 = question[index1]
        while character2 != " ":
            index2 += 1
            character2 = question[index2]

        question = question[:index1] + "\n" + question[index1:index2] + "\n" + question[index2:]

        return question

    def answer1(self):
        answerTexts[0] = answers[0]
        self.updateLabels()

    def updateLabels(self):
        self.team1Score["text"] = str(team1Score)
        self.team2Score["text"] = str(team2Score)
        self.questionLabel["text"] = self.optimize(question)
        if answerTexts[0] == "":
            if answers[0] != "":
                self.answer1["text"] = "1"
            else: self.answer1["text"] = ""
        else: self.answer1["text"] = answerTexts[0] + " (" + str(answerPointValues[0]) + ")"
        if answerTexts[1] == "":
            if answers[1] != "":
                self.answer2["text"] = "2"
            else: self.answer2["text"] = ""
        else: self.answer2["text"] = answerTexts[1] + " (" + str(answerPointValues[1]) + ")"
        if answerTexts[2] == "":
            if answers[2] != "":
                self.answer3["text"] = "3"
            else: self.answer3["text"] = ""
        else: self.answer3["text"] = answerTexts[2] + " (" + str(answerPointValues[2]) + ")"
        if answerTexts[3] == "":
            if answers[3] != "":
                self.answer4["text"] = "4"
            else: self.answer4["text"] = ""
        else: self.answer4["text"] = answerTexts[3] + " (" + str(answerPointValues[3]) + ")"
        if answerTexts[4] == "":
            if answers[4] != "":
                self.answer5["text"] = "5"
            else: self.answer5["text"] = ""
        else: self.answer5["text"] = answerTexts[4] + " (" + str(answerPointValues[4]) + ")"
        if answerTexts[5] == "":
            if answers[5] != "":
                self.answer6["text"] = "6"
            else: self.answer6["text"] = ""
        else: self.answer6["text"] = answerTexts[5] + " (" + str(answerPointValues[5]) + ")"
        if answerTexts[6] == "":
            if answers[6] != "":
                self.answer7["text"] = "7"
            else: self.answer7["text"] = ""
        else: self.answer7["text"] = answerTexts[6] + " (" + str(answerPointValues[6]) + ")"
        if answerTexts[7] == "":
            if answers[7] != "":
                self.answer8["text"] = "8"
            else: self.answer8["text"] = ""
        else: self.answer8["text"] = answerTexts[7] + " (" + str(answerPointValues[7]) + ")"
        self.X1["fg"] = Xs[0]
        self.X2["fg"] = Xs[1]
        self.X3["fg"] = Xs[2]

    def create_widgets(self):
        self.team1Label = Label(self, text=team1, font=(font, 30), width=10, height=1)
        self.team1Label.grid(row=0, column=0, sticky=W)

        self.team1Score = Label(self, text=str(team1Score), font=(font, 30), width=10, height=1)
        self.team1Score.grid(row=1, column=0, sticky=W)

        self.questionLabel = Label(self, text=self.optimize(question), font=(font, 25), width=42, height=3)
        self.questionLabel.grid(row=0, column=1, rowspan=2, columnspan=3)

        self.team2Label = Label(self, text=team2, font=(font, 30), width=10, height=1)
        self.team2Label.grid(row=0, column=4, sticky=E)

        self.team2Score = Label(self, text=str(team2Score), font=(font, 30), width=10, height=1)
        self.team2Score.grid(row=1, column=4, sticky=E)

        Label(self, height=1, width=1).grid(row=3, column=0)

        self.answer1 = Label(self, text=answerTexts[0], font=(font, 20), width=28, height=2, bg="blue", fg="white")
        self.answer1.grid(row=4, column=0, columnspan=2, sticky=E)

        Label(self, height=1, width=1).grid(row=5, column=0)

        self.answer2 = Label(self, text=answerTexts[1], font=(font, 20), width=28, height=2, bg="blue", fg="white")
        self.answer2.grid(row=6, column=0, columnspan=2, sticky=E)

        Label(self, height=1, width=1).grid(row=7, column=0)

        self.answer3 = Label(self, text=answerTexts[2], font=(font, 20), width=28, height=2, bg="blue", fg="white")
        self.answer3.grid(row=8, column=0, columnspan=2, sticky=E)

        Label(self, height=1, width=1).grid(row=9, column=0)

        self.answer4 = Label(self, text=answerTexts[3], font=(font, 20), width=28, height=2, bg="blue", fg="white")
        self.answer4.grid(row=10, column=0, columnspan=2, sticky=E)

        self.timer = Label(self, text="0.0", font=(font, 20), width=2, height=2, fg="black")
        self.timer.grid(row=4, column=2, rowspan=10)

        #Label(self, height=1, width=1).grid(row=7, column=2)

        self.answer5 = Label(self, text=answerTexts[4], font=(font, 20), width=28, height=2, bg="blue", fg="white")
        self.answer5.grid(row=4, column=3, columnspan=2, sticky=W)

        self.answer6 = Label(self, text=answerTexts[5], font=(font, 20), width=28, height=2, bg="blue", fg="white")
        self.answer6.grid(row=6, column=3, columnspan=2, sticky=W)

        self.answer7 = Label(self, text=answerTexts[6], font=(font, 20), width=28, height=2, bg="blue", fg="white")
        self.answer7.grid(row=8, column=3, columnspan=2, sticky=W)

        self.answer8 = Label(self, text=answerTexts[7], font=(font, 20), width=28, height=2, bg="blue", fg="white")
        self.answer8.grid(row=10, column=3, columnspan=2, sticky=W)

        Label(self, height=1, width=1).grid(row=11, column=0)

        self.X1 = Label(self, text="X", font=("Cooper Black", 50), fg=Xs[0])
        self.X1.grid(row=12, column=0, columnspan=2, sticky=E)

        self.X2 = Label(self, text="X", font=("Cooper Black", 50), fg=Xs[1])
        self.X2.grid(row=12, column=2)

        self.X3 = Label(self, text="X", font=("Cooper Black", 50), fg=Xs[2])
        self.X3.grid(row=12, column=3, columnspan=2, sticky=W)

class Application2(Frame):
    def __init__(self, master):
        super(Application2, self).__init__(master)
        self.grid()
        self.create_widgets()

    def answer1s(self):
        answerTexts[0] = answers[0]
        app1.updateLabels()
        winsound.PlaySound("Number One Correct Answer.wav", winsound.SND_FILENAME)

    def answer2s(self):
        answerTexts[1] = answers[1]
        app1.updateLabels()
        winsound.PlaySound("Correct Answer Complete.wav", winsound.SND_FILENAME)

    def answer3s(self):
        answerTexts[2] = answers[2]
        app1.updateLabels()
        winsound.PlaySound("Correct Answer Complete.wav", winsound.SND_FILENAME)

    def answer4s(self):
        answerTexts[3] = answers[3]
        app1.updateLabels()
        winsound.PlaySound("Correct Answer Complete.wav", winsound.SND_FILENAME)

    def answer5s(self):
        answerTexts[4] = answers[4]
        app1.updateLabels()
        winsound.PlaySound("Correct Answer Complete.wav", winsound.SND_FILENAME)

    def answer6s(self):
        answerTexts[5] = answers[5]
        app1.updateLabels()
        winsound.PlaySound("Correct Answer Complete.wav", winsound.SND_FILENAME)

    def answer7s(self):
        answerTexts[6] = answers[6]
        app1.updateLabels()
        winsound.PlaySound("Correct Answer Complete.wav", winsound.SND_FILENAME)

    def answer8s(self):
        answerTexts[7] = answers[7]
        app1.updateLabels()
        winsound.PlaySound("Correct Answer Complete.wav", winsound.SND_FILENAME)

    def addPoints1(self):
        global team1Score
        for i in range(len(answerTexts)):
            if answerTexts[i] != "":
                team1Score += answerPointValues[i]*self.pointsMultiplier.get()
        app1.updateLabels()

    def addPoints2(self):
        global team2Score
        for i in range(len(answerTexts)):
            if answerTexts[i] != "":
                team2Score += answerPointValues[i]*self.pointsMultiplier.get()
        app1.updateLabels()

    def addTheX(self):
        winsound.PlaySound("Incorrect Answer Complete.wav", winsound.SND_FILENAME)
        if Xs[0] == "gray":
            Xs[0] = "red"
        elif Xs[1] == "gray":
            Xs[1] = "red"
        elif Xs[2] == "gray":
            Xs[2] = "red"
        app1.updateLabels()

    def soundBoard(self):
        subSubRoot = Tk()
        app3 = Application3(subSubRoot)
        subSubRoot.mainloop()

    def changeTeam1(self):
        global team1Score
        team1Score += self.teamScoreSlider.get()
        app1.updateLabels()

    def changeTeam2(self):
        global team2Score
        team2Score += self.teamScoreSlider.get()
        app1.updateLabels()

    def advanceRound(self):
        global question
        for i in range(8):
            answerTexts[i] = ""
            answers[i] = ""
            answerPointValues[i] = 0
        app1.updateLabels()
        randint = random.randint(0, len(information)-1)
        question = information[randint][0]
        a = list(information[randint][1].keys())
        for i in range(len(a)):
            answers[i] = a[i]
            answerPointValues[i] = information[randint][1][a[i]]
        Xs[0] = "gray"
        Xs[1] = "gray"
        Xs[2] = "gray"
        self.updateLabels()
        app1.updateLabels()
        winsound.PlaySound("Reveal Question Complete.wav", winsound.SND_FILENAME)

    def updateLabels(self):
        self.question["text"] = app1.optimize(question)
        self.answer1["text"] = answers[0] + " (" + str(answerPointValues[0]) + ")"
        self.answer2["text"] = answers[1] + " (" + str(answerPointValues[1]) + ")"
        self.answer3["text"] = answers[2] + " (" + str(answerPointValues[2]) + ")"
        self.answer4["text"] = answers[3] + " (" + str(answerPointValues[3]) + ")"
        self.answer5["text"] = answers[4] + " (" + str(answerPointValues[4]) + ")"
        self.answer6["text"] = answers[5] + " (" + str(answerPointValues[5]) + ")"
        self.answer7["text"] = answers[6] + " (" + str(answerPointValues[6]) + ")"
        self.answer8["text"] = answers[7] + " (" + str(answerPointValues[7]) + ")"

    def create_widgets(self):
        self.question = Label(self, text=app1.optimize(question), font=(font, 20), width=40, height=3)
        self.question.grid(row=0, column=0, columnspan=4)

        Label(self, width=0, height=1).grid(row=1, column=0)

        self.answer1 = Button(self, text=answers[0] + " (" + str(answerPointValues[0]) + ")", font=(font, 14), width=40, height=1, bg="blue", fg="white", activebackground="lime", command=self.answer1s)
        self.answer1.grid(row=2, column=0, columnspan=4)

        Label(self, width=0, height=1).grid(row=3, column=0)

        self.answer2 = Button(self, text=answers[1] + " (" + str(answerPointValues[1]) + ")", font=(font, 14), width=40, height=1, bg="blue", fg="white", activebackground="lime", command=self.answer2s)
        self.answer2.grid(row=4, column=0, columnspan=4)

        Label(self, width=0, height=1).grid(row=5, column=0)

        self.answer3 = Button(self, text=answers[2] + " (" + str(answerPointValues[2]) + ")", font=(font, 14), width=40, height=1, bg="blue", fg="white", activebackground="lime", command=self.answer3s)
        self.answer3.grid(row=6, column=0, columnspan=4)

        Label(self, width=0, height=1).grid(row=7, column=0)

        self.answer4 = Button(self, text=answers[3] + " (" + str(answerPointValues[3]) + ")", font=(font, 14), width=40, height=1, bg="blue", fg="white", activebackground="lime", command=self.answer4s)
        self.answer4.grid(row=8, column=0, columnspan=4)

        Label(self, width=0, height=1).grid(row=9, column=0)

        self.answer5 = Button(self, text=answers[4] + " (" + str(answerPointValues[4]) + ")", font=(font, 14), width=40, height=1, bg="blue", fg="white", activebackground="lime", command=self.answer5s)
        self.answer5.grid(row=10, column=0, columnspan=4)

        Label(self, width=0, height=1).grid(row=11, column=0)

        self.answer6 = Button(self, text=answers[5] + " (" + str(answerPointValues[5]) + ")", font=(font, 14), width=40, height=1, bg="blue", fg="white", activebackground="lime", command=self.answer6s)
        self.answer6.grid(row=12, column=0, columnspan=4)

        Label(self, width=0, height=1).grid(row=13, column=0)

        self.answer7 = Button(self, text=answers[6] + " (" + str(answerPointValues[6]) + ")", font=(font, 14), width=40, height=1, bg="blue", fg="white", activebackground="lime", command=self.answer7s)
        self.answer7.grid(row=14, column=0, columnspan=4)

        Label(self, width=0, height=1).grid(row=15, column=0)

        self.answer8 = Button(self, text=answers[7] + " (" + str(answerPointValues[7]) + ")", font=(font, 14), width=40, height=1, bg="blue", fg="white", activebackground="lime", command=self.answer8s)
        self.answer8.grid(row=16, column=0, columnspan=4)


        self.teamScoreSlider = Scale(self, from_=-50, to=50, label="Score Changer", font=(font, 20), tickinterval=25, length=250, orient=HORIZONTAL, fg="lime")
        self.teamScoreSlider.grid(row=0, column=4, columnspan=2, rowspan=2)

        self.change1 = Button(self, text="Change %s" % team1, font=(font, 20), width=20, height=1, bg="lime", fg="black", command=self.changeTeam1)
        self.change1.grid(row=0, column=6)

        self.change2 = Button(self, text="Change %s" % team2, font=(font, 20), width=20, height=1, bg="lime", fg="black", command=self.changeTeam2)
        self.change2.grid(row=1, column=6)

        self.team1addPoints = Button(self, text="Add points to %s" % team1, font=(font, 20), width=20, height=1, bg="lime", fg="black", command=self.addPoints1)
        self.team1addPoints.grid(row=3, column=5, rowspan=2, columnspan=2)

        self.team2addPoints = Button(self, text="Add points to %s" % team2, font=(font, 20), width=20, height=1, bg="lime", fg="black", command=self.addPoints2)
        self.team2addPoints.grid(row=5, column=5, rowspan=2, columnspan=2)

        self.addX = Button(self, text="Add 'X'", font=(font, 20), width=20, height=1, bg="lime", fg="black", activebackground="red", command=self.addTheX)
        self.addX.grid(row=7, column=5, rowspan=2, columnspan=2)

        self.pointsMultiplier = Scale(self, from_=1, to=3, label="Points Multiplier", font=(font, 20), tickinterval=1, length=500, orient=HORIZONTAL, fg="lime")
        self.pointsMultiplier.grid(row=9, column=5, rowspan=4, columnspan=2)

        self.startTimer = Button(self, text="Open Soundboard", font=(font, 20), width=20, height=1, bg="lime", fg="black", command=self.soundBoard)
        self.startTimer.grid(row=13, column=5, rowspan=2, columnspan=2)

        self.nextRound = Button(self, text="Next Round", font=(font, 20), width=20, height=1, bg="lime", fg="black", activebackground="black", activeforeground="lime", command=self.advanceRound)
        self.nextRound.grid(row=15, column=5, rowspan=2, columnspan=2)

root = Tk()
windowWidth = root.winfo_screenwidth()
windowHeight = root.winfo_screenheight()
root.geometry("%dx%d" % (windowWidth, windowHeight))
subRoot = Tk()
subRoot.geometry("%dx%d" % (windowWidth, windowHeight))

app1 = Application(root)
app2 = Application2(subRoot)

subRoot.mainloop()
root.mainloop()