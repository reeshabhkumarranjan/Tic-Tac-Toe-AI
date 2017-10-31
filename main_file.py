###############################################################################################################
#																										      #
#																										      #
#																										      #
#																										      #
# 	   NAME: REESHABH KUMAR RANJAN																	 	      #
# 	   ROLL NUMBER: 2017086																		 	 	      #
# 												 	      													  #
#        		       																						  #
#																										      #
#																										      #
#																										      #
#																										      #
###############################################################################################################

#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

########################################################################
#        M O D U L E S _ I M P O R T E D                               #
########################################################################

import random
import variables

########################################################################
#        F U N C T I O N : V A L I D M O V E                           #
########################################################################

def validmove(move):

	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tiles.tile for the move is not ticked.
	"""

	if get(move)==0:
		return True
	else:
		return False

########################################################################
#        F U N C T I O N : W I N                                       #
########################################################################

def win():

	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""

	cond1=variables.tile1==variables.tile2==variables.tile3!=0
	cond2=variables.tile1==variables.tile4==variables.tile7!=0
	cond3=variables.tile3==variables.tile6==variables.tile9!=0
	cond4=variables.tile7==variables.tile8==variables.tile9!=0
	cond5=variables.tile2==variables.tile5==variables.tile8!=0
	cond6=variables.tile4==variables.tile5==variables.tile6!=0
	cond7=variables.tile1==variables.tile5==variables.tile9!=0
	cond8=variables.tile3==variables.tile5==variables.tile7!=0

	if cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7 or cond8:
		return True
	else:
		return False

########################################################################
#        F U N C T I O N : T A K E  N A I V E  M O V E                 #
########################################################################

def takeNaiveMove():

	""" Returns a tiles.tile number randomly from the set of unchecked tiles.tiles with uniform probability distribution.    
	"""

	x=random.randint(1,9)

	while not validmove(x):
		x=random.randint(1,9)

	return x

########################################################################
#        F U N C T I O N : T A K E  S T R A T E G I C  M O V E         #
########################################################################

def takeStrategicMove():

	""" Returns a tiles.tile number from the set of unchecked tiles.tiles
	using some rules.
	
	"""

	if emptyboard():

		firstmove=random.randint(1,5)

		if firstmove==1:
			return 1

		if firstmove==2:
			return 3

		if firstmove==3:
			return 5

		if firstmove==4:
			return 7

		if firstmove==5:
			return 9

	check=win_soon(variables.turn)
	if check.isdigit():
		for i in check:
			if get(int(i))==0:
				return int(i)

	check=danger(variables.turn)
	if check.isdigit():
		for i in check:
			if get(int(i))==0:
				return int(i)

	if variables.tile5==0:
		return 5

	if may_win(variables.turn)!="not yet":
		return may_win(variables.turn)

	if variables.tile1*variables.tile3*variables.tile7*variables.tile9==0:
		for i in "1379":
			if get(int(i))==0:
				return int(i)

	final=takeNaiveMove()
	return final

########################################################################
#        F U N C T I O N : V A L I D B O A R D                         #
########################################################################

def validBoard():

	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""

	if variables.player1_counter==variables.player2_counter or variables.player1_counter==variables.player2_counter+1:
		return True
	else:
		return False

########################################################################
#        F U N C T I O N : G A M E                                     #
########################################################################

def game(gametype=1):

	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	
	if gametype==1:
		result=noob_vs_noob()

	elif gametype==2:
		result=noob_vs_pro()

	elif gametype==3:
		result=pro_vs_pro()

	return result

########################################################################
#        F U N C T I O N : G A M E 1                                   #
########################################################################

def game1(n):

	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""

	counter=0

	for i in range(n):
		if game(1)==1:
			counter+=1

	return float(counter)/n

########################################################################
#        F U N C T I O N : G A M E 2                                   #
########################################################################

def game2(n):

	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""

	counter=0

	for i in range(n):
		if game(2)==1:
			counter+=1

	return float(counter)/n

########################################################################
#        F U N C T I O N : G A M E 3                                   #
########################################################################

def game3(n):

	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""

	counter=0

	for i in range(n):
		if game(3)==1:
			counter+=1
			
	return float(counter)/n

########################################################################
#        F U N C T I O N : R E S E T                                   #
########################################################################

def reset():
	"""Resets all the variables in the imported variables file."""
	variables.tile1=variables.tile2=variables.tile3=variables.tile4=variables.tile5=variables.tile6=variables.tile7=variables.tile8=variables.tile9=0

########################################################################
#        F U N C T I O N : O P P O N E N T                             #
########################################################################

def opponent(Player):

	"""Returns the opponent's id (0,1)=(1,0) of the Player."""

	if Player==1:
		return variables.player2
	else:
		return variables.player1

########################################################################
#        F U N C T I O N : F U L L B O A R D                           #
########################################################################

def fullboard():

	"""Checks if the board is fully occupied or not."""

	if variables.tile1*variables.tile2*variables.tile3*variables.tile4*variables.tile5*variables.tile6*variables.tile7*variables.tile8*variables.tile9!=0:
		return True
	else:
		return False

########################################################################
#        F U N C T I O N : E M P T Y B O A R D                         #
########################################################################

def emptyboard():

	"""Checks if the board is untouched or not."""

	if variables.tile1+variables.tile2+variables.tile3+variables.tile4+variables.tile5+variables.tile6+variables.tile7+variables.tile8+variables.tile9==0:
		return True
	else:
		return False

########################################################################
#        F U N C T I O N : S E T                                       #
########################################################################

def set(tile,data):

	"""Sets the data into the tile corresponding to the tile number."""

	if tile==1:
		variables.tile1=data

	elif tile==2:
		variables.tile2=data

	elif tile==3:
		variables.tile3=data

	elif tile==4:
		variables.tile4=data

	elif tile==5:
		variables.tile5=data

	elif tile==6:
		variables.tile6=data

	elif tile==7:
		variables.tile7=data

	elif tile==8:
		variables.tile8=data

	else:
		variables.tile9=data

########################################################################
#        F U N C T I O N : G E T                                       #
########################################################################

def get(tile):

	"""Returns the data of the tile corresponding to the tile number."""

	if tile==1:
		return variables.tile1

	elif tile==2:
		return variables.tile2

	elif tile==3:
		return variables.tile3

	elif tile==4:
		return variables.tile4

	elif tile==5:
		return variables.tile5

	elif tile==6:
		return variables.tile6

	elif tile==7:
		return variables.tile7

	elif tile==8:
		return variables.tile8

	else:
		return variables.tile9

########################################################################
#        F U N C T I O N : D A N G E R                                 #
########################################################################

def danger(turn):

	"""Checks if there is a possibility for the opponent to win in its next turn."""

	cond1=(variables.tile1+variables.tile2+variables.tile3==2*opponent(turn)) and (variables.tile1==opponent(turn) or variables.tile2==opponent(turn) or variables.tile3==opponent(turn))
	cond11=variables.tile1*variables.tile2*variables.tile3==0

	cond2=(variables.tile1+variables.tile4+variables.tile7==2*opponent(turn)) and (variables.tile1==opponent(turn) or variables.tile4==opponent(turn) or variables.tile7==opponent(turn))
	cond22=variables.tile1*variables.tile4*variables.tile7==0

	cond3=(variables.tile3+variables.tile6+variables.tile9==2*opponent(turn)) and (variables.tile3==opponent(turn) or variables.tile6==opponent(turn) or variables.tile9==opponent(turn))
	cond33=variables.tile3*variables.tile6*variables.tile9==0

	cond4=(variables.tile7+variables.tile8+variables.tile9==2*opponent(turn)) and (variables.tile7==opponent(turn) or variables.tile8==opponent(turn) or variables.tile9==opponent(turn))
	cond44=variables.tile7*variables.tile8*variables.tile9==0

	cond5=(variables.tile2+variables.tile5+variables.tile8==2*opponent(turn)) and (variables.tile2==opponent(turn) or variables.tile5==opponent(turn) or variables.tile8==opponent(turn))
	cond55=variables.tile2*variables.tile5*variables.tile8==0

	cond6=(variables.tile4+variables.tile5+variables.tile6==2*opponent(turn)) and (variables.tile4==opponent(turn) or variables.tile5==opponent(turn) or variables.tile6==opponent(turn))
	cond66=variables.tile4*variables.tile5*variables.tile6==0

	cond7=(variables.tile1+variables.tile5+variables.tile9==2*opponent(turn)) and (variables.tile1==opponent(turn) or variables.tile5==opponent(turn) or variables.tile9==opponent(turn))
	cond77=variables.tile1*variables.tile5*variables.tile9==0

	cond8=(variables.tile3+variables.tile5+variables.tile7==2*opponent(turn)) and (variables.tile3==opponent(turn) or variables.tile5==opponent(turn) or variables.tile7==opponent(turn))
	cond88=variables.tile3*variables.tile5*variables.tile7==0

	if cond1 and cond11:
		return "123"

	elif cond2 and cond22:
		return "147"

	elif cond3 and cond33:
		return "369"

	elif cond4 and cond44:
		return "789"

	elif cond5 and cond55:
		return "258"

	elif cond6 and cond66:
		return "456"

	elif cond7 and cond77:
		return "159"

	elif cond8 and cond88:
		return "357"

	else:
		return "safe"

########################################################################
#        F U N C T I O N : W I N _ S O O N                             #
########################################################################

def win_soon(turn):

	"""Checks if there is an immediate possibility of the player to win in just one step."""

	cond1=(variables.tile1+variables.tile2+variables.tile3==2*turn) and (variables.tile1==turn or variables.tile2==turn or variables.tile3==turn)
	cond2=(variables.tile1+variables.tile4+variables.tile7==2*turn) and (variables.tile1==turn or variables.tile4==turn or variables.tile7==turn)
	cond3=(variables.tile3+variables.tile6+variables.tile9==2*turn) and (variables.tile3==turn or variables.tile6==turn or variables.tile9==turn)
	cond4=(variables.tile7+variables.tile8+variables.tile9==2*turn) and (variables.tile7==turn or variables.tile8==turn or variables.tile9==turn)
	cond5=(variables.tile2+variables.tile5+variables.tile8==2*turn) and (variables.tile2==turn or variables.tile5==turn or variables.tile8==turn)
	cond6=(variables.tile4+variables.tile5+variables.tile6==2*turn) and (variables.tile4==turn or variables.tile5==turn or variables.tile6==turn)
	cond7=(variables.tile1+variables.tile5+variables.tile9==2*turn) and (variables.tile1==turn or variables.tile5==turn or variables.tile9==turn)
	cond8=(variables.tile3+variables.tile5+variables.tile7==2*turn) and (variables.tile3==turn or variables.tile5==turn or variables.tile7==turn)

	if cond1:
		return "123"

	elif cond2:
		return "147"

	elif cond3:
		return "369"

	elif cond4:
		return "789"

	elif cond5:
		return "258"

	elif cond6:
		return "456"

	elif cond7:
		return "159"

	elif cond8:
		return "357"

	else:
		return "not yet"

########################################################################
#        F U N C T I O N : C O U N T E R _ 0                           #
########################################################################

def counter_0(x):

	"""A helper function for may_win() which counts number of 0 in the passed tile indices."""

	counter=0
	for i in x:
		if get(int(i))==0:
			counter+=1
	return counter

########################################################################
#        F U N C T I O N : F I N D _ Z E R O                           #
########################################################################

def find_zero(x):

	"""A helper function for may_win() which returns the index of the first occurence of 0 in the passed tile indices."""

	for i in x:
		if get(int(i))==0:
			return int(i)

########################################################################
#        F U N C T I O N : T R A C K _ T U R N                         #
########################################################################

def track_turn(x,turn):

	""" A helper function for may_win() which tracks presence of player's turn in given adjacent indices."""

	for i in x:
		if get(int(i))==turn:
			return True

########################################################################
#        F U N C T I O N : M A Y _ W I N                               #
########################################################################

def may_win(turn):

	"""If all the other moves are skipped, this move will be executed expecting a favourable scenario for the player."""

	combin1='123'
	combin2='147'
	combin3='369'
	combin4='789'
	combin5='258'
	combin6='456'
	combin7='159'
	combin8='357'

	if counter_0(combin1)==2 and (track_turn(combin1,turn)):
		return find_zero(combin1)

	if counter_0(combin2)==2 and (track_turn(combin2,turn)):
		return find_zero(combin2)

	if counter_0(combin3)==2 and (track_turn(combin3,turn)):
		return find_zero(combin3)

	if counter_0(combin4)==2 and (track_turn(combin4,turn)):
		return find_zero(combin4)

	if counter_0(combin5)==2 and (track_turn(combin5,turn)):
		return find_zero(combin5)

	if counter_0(combin6)==2 and (track_turn(combin6,turn)):
		return find_zero(combin6)

	if counter_0(combin7)==2 and (track_turn(combin7,turn)):
		return find_zero(combin7)

	if counter_0(combin8)==2 and (track_turn(combin8,turn)):
		return find_zero(combin8)

	if True:
		return "not yet"

########################################################################
#        F U N C T I O N : N O O B _ V S _ N O O B                     #
########################################################################

def noob_vs_noob():

	"""Plays a match between two noob players and returns the result."""

	reset()
	variables.player1_counter=0
	variables.player2_counter=0
	for i in range(1,10):
		variables.turn=1

		if not validBoard():
			print("Board configuration is currently invalid.")
			return None

		x=takeNaiveMove()
		set(x,1)
		variables.player1_counter+=1

		if win():
			return 1
		elif fullboard():
			return 0

		variables.turn=2

		if not validBoard():
			print("Board configuration is currently invalid.")
			return None

		y=takeNaiveMove()
		set(y,2)
		variables.player2_counter+=1

		if win():
			return 2
		elif fullboard():
			return 0

########################################################################
#        F U N C T I O N : N O O B _ V S _ P R O                       #
########################################################################

def noob_vs_pro():

	"""Plays a match between a noob and a pro player and returns the result."""#Assignment-2, Game Tic-tac-toe

	reset()
	variables.player1_counter=0
	variables.player2_counter=0
	for i in range(1,10):
		variables.turn=1

		if not validBoard():
			print("Board configuration is currently invalid.")
			return None
		
		x=takeNaiveMove()
		set(x,1)
		variables.player1_counter+=1

		if win():
			return 1
		elif fullboard():
			return 2

		variables.turn=2

		if not validBoard():
			print("Board configuration is currently invalid.")
			return None

		y=takeStrategicMove()
		set(y,2)
		variables.player2_counter+=1

		if win():
			return 2
		elif fullboard():
			return 0

########################################################################
#        F U N C T I O N : P R O _ V S _ P R O                         #
########################################################################

def pro_vs_pro():

	"""Plays a match between two pro players and returns the result."""

	reset()
	variables.player1_counter=0
	variables.player2_counter=0
	for i in range(1,10):
		
		variables.turn=1

		if not validBoard():
			print("Board configuration is currently invalid.")
			return None

		x=takeStrategicMove()
		set(x,1)
		variables.player1_counter+=1

		if win():
			return 1
		elif fullboard():
			return 0


		variables.turn=2

		if not validBoard():
			print("Board configuration is currently invalid.")
			return None

		y=takeStrategicMove()
		set(y,2)
		variables.player2_counter+=1

		if win():
			return 2
		elif fullboard():
			return 0

if __name__ == '__main__':
	print(game1(10000))
	print(game2(10000))
	print(game3(10000))