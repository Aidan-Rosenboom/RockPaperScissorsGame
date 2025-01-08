#Rock paper scissors game
import random
#initualized list and variables
itemList = []
botList = []
myChoice = ""
myWins = 0
totalWins = 0
myInput = ""
#code takes rockPaperScissors file and selects each word from each line and adds it too the itemList
f = open("rockPaperScissors.txt", "r")
for line in f:
	for word in line.split():
		itemList.append(word)
#Test print(itemList)
#class that is used to get different AI players to play the game
class AiPlayers(object):
	
	def __init__(self, name, botWins = 0, botTotalWins = 0, guess = ""):
		"""Initualizes the values of the class"""
		self.name = name
		self.botWins = botWins
		self.botTotalWins = botTotalWins
		self.guess = guess
		
	def getName(self):
		"""Method that returns the name of the AI"""
		return self.name
		
	def addRoundWin(self):
		"""adds a win to the bots win counter"""
		self.botWins += 1
		
	def addGameWin(self):
		"""Counts how many times the Ai won in total"""
		self.botTotalWins += 1
		
	def resetBotWins(self):
		"""Resets the bot round wins"""
		self.botWins = 0
		
	def getGuess(self):
		"""returns the Ai's guess"""
		guess = random.randint(0, 2)
		self.guess = itemList[guess]
		return self.guess

#functions
def userRPS(i,lyst):
	"""Goes through the users input and sets the choice to rock paper or scissors"""
	if i == "R":
		return lyst[0]
	elif i == "P":
		return lyst[1]
	elif i == "S":
		return lyst[2]
	else:
		return False
	
def checkWinner(choice, aObject):
	"""Checks weather the user beats the Ai in rock paper scissors game and returns a boolean to prove if you won or not"""
	botGuess = aObject.getGuess()
	if choice == botGuess:
		print("You chose " + choice + " and " + aObject.getName() + " Chose " + botGuess + ", you Tie!")
		return None
	elif choice == "Rock" and botGuess == "Scissors":
		print("You chose " + choice + " and " + aObject.getName() + " Chose " + botGuess + ", you Win!")
		return True
	elif choice == "Paper" and botGuess == "Rock":
		print("You chose " + choice + " and " + aObject.getName() + " Chose " + botGuess + ", you Win!")
		return True
	elif choice == "Scissors" and botGuess == "Paper":
		print("You chose " + choice + " and " + aObject.getName() + " Chose " + botGuess + ", you Win!")
		return True
	else:
		print("You chose " + choice + " and " + aObject.getName() + " Chose " + botGuess + ", you Lose!")
		return False

def userInput():
	"""Simple function to set get the users input"""
	i = input("Enter R for rock, P for paper, S for scissors, or QUIT to quit: ")
	i = i.upper()
	return i

#Initualizes three bot players to play Rock paper scissors
Bob = AiPlayers("Bob")
Joe = AiPlayers("Joe")
Billy = AiPlayers("Billy")
#adds these players to a List
botList.append(Bob)
botList.append(Joe)
botList.append(Billy)
#cycles through each item in the bot list
for item in botList:
	print("You VS. " + str(item.getName()))
	#this loops through the code until either the player or bot gets 2 wins
	while True:
		myInput = userInput()
		if myInput == "QUIT":
			quit()
		#Test print(myInput)
		#Test print(itemList)
		myChoice = userRPS(myInput, itemList)
		#Test print(myChoice)
		winnerCheck = checkWinner(myChoice, item)
		#if statements here check weather or not you won, tied, or lost
		if winnerCheck == None:
			print("Score: " + "You: " + str(myWins) + " " + item.getName() + " " + str(item.botWins) + "\n")
		elif winnerCheck == True:
			myWins += 1
			print("Score: " + "You: " + str(myWins) + " " + item.getName() + " " + str(item.botWins) + "\n")
		else:
			item.addRoundWin()
			print("Score: " + "You: " + str(myWins) + " " + item.getName() + " " + str(item.botWins)+ "\n")
		#this if elif statment checks weather or not you or the bot has won multiple games.
		if myWins == 2:
			print("You won against " + str(item.getName()))
			totalWins += 1
			myWins = 0
			item.resetBotWins()
			break
		elif item.botWins == 2:
			print("You Lost To " + str(item.getName()))
			item.addGameWin()
			myWins = 0
			item.resetBotWins()
			break
#after facing all the Ai's These statments will return the total amount of games that you and each Ai won.
print("You won" , str(totalWins), "games of rock paper scissors")
for item in botList:
	print(str(item.getName()), "won" , str(item.botTotalWins), "games of rock paper scissors")
