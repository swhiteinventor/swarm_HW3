#!/usr/bin/env python
from random import randint
from collections import deque 
import copy

class agent:

	def __init__(self, id, threshold, x, y):
		
		self.id = id
		self.threshold = threshold
		self.satisfied = False
		self.x = x
		self.y = y

	def move(self, agent):
		self.id = agent.id
		self.threshold = agent.threshold
		self.satisfied = agent.satisfied
	
	def clear(self):
		self.id = ' '
		self.threshold = 0
		self.satisfied = False

def SpawnWorld(sizeX, sizeY, population, threshold1, threshold1Percent=1, threshold2=0):
	
	"""
	This function creates a 'sizeX' by 'sizeY' grid. Each cell in the 
	grid is randomly populated with an agent that identifies as an 'X',
	an 'O', or an empty cell (' ').
	Parameters:
		sizeX, SizeY - integers that define the size of the world
		population - a fraction of the number of cells that should 
			contain agents
		threshold1 - an integer 0 to 8 that defines how homophilous the
			agent is (how many similar agents nearby are neccesary 
			for the agent to be satisfied); if you just want to
			use a single threshold, then do not specify theshold1Percent
			or threshold2
		threshold1Percent - a fraction of how many agents should have 
			the threshold1 vs having the threshold2; defaults to 1
		threshold2 - just like the previous threshold integer, but lets
			you specify a different threshold value; defaults to 0
	Returns:
		matrix of agents, aka the 'world'
	"""

	#variables
	numX = 0
	numO = 0
	numAgent = int(sizeX*sizeY*population*0.5)
	numBlank = 0
	numNotAgent = sizeX*sizeY - numAgent*2
	numThresh1 = 0
	numThresh1Cap = int(numAgent*2*threshold1Percent)
	numThresh2 = 0
	numThresh2Cap = numAgent*2 - numThresh1Cap

	#initialize our array
	world = []

	#populate the array
	for i in range(sizeY):

		#initialize temporary variables
		tempRow = []
		flagID = ''

		#create boundaries for random selection
		largeNumber = 1000000;
		division1 = 0.5*population*largeNumber
		division2 = population*largeNumber
		divisionThresh = threshold1Percent*largeNumber

		for k in range(sizeX):
			#generate some randome numbers
			randID = randint(0,largeNumber)
			randThreshID = randint(0,largeNumber)

			#decide whether the agents will be 'X', 'O',
			# or ' ' (blank)
			if randID < division1:
				if numX < numAgent:
					flagID = 'X'
				elif numO < numAgent:
					flagID = 'O'
				else:
					flagID = ' '
			if randID >= division1 and randID < division2:
				if numO < numAgent:
					flagID = 'O'
				elif numX < numAgent:
					flagID = 'X'
				else:
					flagID = ' '
			if randID >= division2:
				if numBlank < numNotAgent:
					flagID = ' '
				elif numX < numAgent:
					flagID = 'X'
				elif numO < numAgent:
					flagID = 'O'	

			#set the threshold for agents
			if flagID == 'X' or flagID == 'O':
				if randThreshID < divisionThresh:
						if numThresh1 < numThresh1Cap:
							threshold = threshold1
							numThresh1 += 1
						else:
							threshold = threshold2
							numThresh2 += 1		
				if randThreshID > divisionThresh:
						if numThresh2 < numThresh2Cap:
							threshold = threshold2
							numThresh2 += 1	
						else:
							threshold = threshold1
							numThresh1 += 1

			#create an agent
			if flagID == 'X':
				tempAgent = agent('X', threshold, k, i)
				numX += 1
			elif flagID == 'O':
				tempAgent = agent('O', threshold, k, i)
				numO += 1
			else:
				tempAgent = agent(' ', 0, k, i)
				numBlank += 1	

			#tempAgent = agent('X',threshold)		
			tempRow.append(tempAgent)
		world.append(tempRow)
	'''
	#some debug statements to verify correct generation
	print ("numX = %d" % (numX))
	print ("numO = %d" % (numO))
	print ("numAgent = %d" % (numAgent))
	print ("numBLank = %d" % (numBlank))
	print ("numNotAgent = %d" % (numNotAgent))
	print ("numThresh1 = %d" % (numThresh1))
	print ("numThresh1Cap = %d" % (numThresh1Cap))
	print ("numThresh2 = %d" % (numThresh2))
	print ("numThresh2Cap = %d" % (numThresh2Cap))
	'''
	#check satisfaction and return the world
	world = CheckSatisfaction(world)
	return world

def CheckSatisfaction(world):
	
	"""
	This function checks the world to see which agents are 
	satisfied and which are not, adjusting the world accordingly.
	Parameters:
		world - pass in a matrix of agents, aka the world
	Returns:
		world - a world with updated satisfaction
	"""
	
	#calculate size of world
	rows = len(world)
	columns = len(world[0])
	
	#iterate through world and check satisfaction
	for i in range(rows):
		for k in range(columns):
			
			#find neighbors and set some variables for counting
			neighbors = FindNeighbors(world, k, i)
			neighborsX = 0
			neighborsO = 0
			neighborsNot = 0
			
			#count the types of neighbors
			for j in range(len(neighbors)):
				if neighbors[j].id == 'X':
					neighborsX += 1
				elif neighbors[j].id == 'O':
					neighborsO += 1
				else:
					neighborsNot += 1
			
			#decide if agent is satisfied
			if world[i][k].id == 'X' and neighborsX >= world[i][k].threshold:
				world[i][k].satisfied = True
			elif world[i][k].id == 'O' and neighborsO >= world[i][k].threshold:
				world[i][k].satisfied = True
			elif world[i][k].id == ' ' and neighborsNot >= world[i][k].threshold:
				world[i][k].satisfied = True
			else:
				world[i][k].satisfied = False

	#all done updating satisfaction
	return world

def FindNeighbors(world, targetX, targetY):
	
	"""
	This function finds the neighboring cells of a given cell in
	the world.
	Parameters:
		world - pass in a matrix of agents, aka the world
		targetX - x-position in the world matrix of target cell
		targetY - y-position in the world matrix of target cell
	Returns:
		neighbors - an array of cells
	"""

	#calculate size of world
	rows = len(world)
	columns = len(world[0])
	neighbors = []
	upOffset = 1
	rightOffset = 1

	#check for overshoot, undershoot automatically loops
	if targetX == columns-1:
		rightOffset = -1*targetX
	if targetY == rows-1:
		upOffset = -1*targetY

	'''
	#some debug statements to verify correct array wrapping
	print ("targetX = %d" % (targetX))
	print ("columns = %d" % (columns))
	print ("targetY = %d" % (targetY))
	print ("rows = %d" % (rows))
	print ("rightOffset = %d" % (rightOffset))
	print ("upOffset = %d" % (upOffset))
	'''

	#retrieve neighbors
	neighbors.append(world[targetY+upOffset][targetX+rightOffset])
	neighbors.append(world[targetY+upOffset][targetX+0])
	neighbors.append(world[targetY+upOffset][targetX-1])
	neighbors.append(world[targetY+0][targetX+rightOffset])
	neighbors.append(world[targetY+0][targetX-1])
	neighbors.append(world[targetY-1][targetX+rightOffset])
	neighbors.append(world[targetY-1][targetX+0])
	neighbors.append(world[targetY-1][targetX-1])

	#all done finding neighbors
	return neighbors

def ShowWorld(world, simulation, step, threshold1, threshold1Percent, threshold2, setting):
	
	"""
	This function prints the world into the terminal. You have
	the option of showing a property of the agent other than id.
	Parameters:
		world - pass in a matrix of agents, aka the world
		simulation - what simulation number
		step - what step of the simulation
		threshold1 - an integer 0 to 8 that defines how homophilous an
			agent is
		threshold1Percent - a fraction of how many agents should have 
			the threshold1 vs having the threshold2
		threshold2 - just like the previous threshold integer, but lets
			you specify a different threshold value
		setting - either 'id', 'threshold', or 'satisfied'; use
			to specify the display to show a property
	Returns:
		nothing
	"""

	#calculate size of world
	rows = len(world)
	columns = len(world[0])
	
	#function for printing top and bottom borders
	def PrintBorder():
		rowText = '-'
		widthWorld = columns*2+2
		
		for i in range(widthWorld):
			rowText += '-'
		print rowText

	#print a fancy title
	PrintBorder()
	print("----------------------->    SIMULATION Number: %2d    STEP Number: %4d    <----------------------------") % (simulation, step)
	print("------------>    %2d%%  agents with Threshold: %1d      %2d%% agents with Theshold 2: %1d    <---------------") % (threshold1Percent*100, threshold1, (100 - threshold1Percent*100), threshold2)
	PrintBorder()
	
	#count numbers satisfied and not satisfied
	numSatisfied = 0
	numUnsatisfied = 0

	#iterate through world and print agent
	for i in range(rows):
		rowText = '| '
		for k in range(columns):
			#count satisfied agents
			if world[i][k].satisfied:
				numSatisfied += 1
			else:
				numUnsatisfied += 1

			if setting == 'threshold':
				if world[i][k].id != ' ':
					rowText += str(world[i][k].threshold) + ' '
				else:
					rowText += '  '			
			elif setting == 'satisfied':
				if world[i][k].id != ' ':
					if world[i][k].satisfied:
						rowText += '@ '
					else:
						 rowText += '* '
				else:
					rowText += '  '
			else:
				rowText += world[i][k].id + ' '

		rowText += "|"
		print rowText

	#print fancy footer
	PrintBorder()
	populationPercent = (numSatisfied+numUnsatisfied)*100/(rows*columns) #should be the same as what was entered eariler
	print("------>    STATS:    %4d agents satisfied, %4d agents not satisfied,    %d%% population    <----------") % (numSatisfied, numUnsatisfied, populationPercent)
	PrintBorder()
	if setting == 'id':
		print("----------------------->    KEY:    'X' = 'Agent X'    'O' = 'Agent O'    <----------------------------")
	elif setting == 'threshold':
		print("------------------>    KEY:    'N' = 'threshold value N, ranging from 0 to 8'    <---------------------")
	elif setting == 'satisfied':
		print("------------------>    KEY:    '@'' = 'satisfied'     '*' = 'not satisfied'    <-----------------------")
	PrintBorder()
	print("\n")

def UpdateWorld(world):
	
	"""
	This function goes through the world moving unsatisfied
	agents to the closest empty spot that would satisfy their 
	threshold requirement.
	Parameters:
		world - pass in a matrix of agents, aka the world
	Returns:
		worldUpdated - an updated world
	"""
	

	#calculate size of world
	rows = len(world)
	columns = len(world[0])

	#make a deep copy of the world
	worldUpdated = copy.deepcopy(world)

	#iterate through the old world to populate the new world
	for i in range(rows):
		for k in range(columns):
			#print("id = %s, threshold = %d, satisfied = %d, x = %d, y = %d") % (world[i][k].id, world[i][k].threshold, world[i][k].satisfied, world[i][k].x, world[i][k].y)
			#if the cell isn't blank in the old world and isn't 
			# satisfied in the new world, check the new world
			# for a place to move to
			if world[i][k].id != ' ' and worldUpdated[i][k].satisfied == False:
				
				#finds somewhere to move to
				move = FindSatisfaction(worldUpdated, k, i)

				#copy agent to new world
				worldUpdated[move[1]][move[0]].move(world[i][k])
				#print("moves   agent %s at (%d,%d) to (%d,%d)") % (world[i][k].id, world[i][k].x, world[i][k].y, move[0], move[1])
				#print("before: agent %s at (%d,%d) ---------") % (world[move[1]][move[0]].id, world[move[1]][move[0]].x, world[move[1]][move[0]].y)
				#print("now     agent %s at (%d,%d) ---------") % (worldUpdated[move[1]][move[0]].id, worldUpdated[move[1]][move[0]].x, worldUpdated[move[1]][move[0]].y)

				#erase agent's old location
				worldUpdated[i][k].clear()
				#print("And gone:     %s at (%d,%d) ---------") % (worldUpdated[i][k].id, worldUpdated[i][k].x, worldUpdated[i][k].y)
			'''
			elif world[i][k] == ' ':
				print("EMPTY:  agent %s at (%d,%d) <<<<<<<<<<<<<<<<<<<<<<<<") % (world[i][k].id, world[i][k].x, world[i][k].y)
			elif worldUpdated[i][k].satisfied == True:
				print("HAPPY:  agent %s at (%d,%d) <<<<<<<<<<<<<<<<<<<<<<<<") % (world[i][k].id, world[i][k].x, world[i][k].y)
			'''

		#update the new world's satisfaction
		worldUpdated = CheckSatisfaction(worldUpdated)

	return worldUpdated

def FindSatisfaction(world, targetX, targetY):

	"""
	This function looks trhough the provided world to identify
	and return the closest position that would make the given
	agent satisfied.
	Parameters:
		world - pass in a matrix of agents, aka the world
		targetX - x-position in the world matrix of target cell
		targetY - y-position in the world matrix of target cell
	Returns:
		moveX
		moveY
	"""

	search = world[targetY][targetX]
	openSet = deque()
	closedSet = []

	openSet.append(world[targetY][targetX])

	while len(openSet) != 0:
		cell = openSet.popleft()
		closedSet.append(cell)
		cellNeighbors = FindNeighbors(world, cell.x, cell.y)
		for i in range(len(cellNeighbors)):
			if cellNeighbors[i] not in closedSet:
				if cellNeighbors[i].id == ' ':
					#check if cell would satisfy agent
					checkNeighbors = FindNeighbors(world, cellNeighbors[i].x, cellNeighbors[i].y)
					searchCount = 0
					for k in range(len(checkNeighbors)):
						if checkNeighbors[k].id == search.id and checkNeighbors[k].x != search.x and checkNeighbors[k].y != search.y:
							searchCount += 1
					if searchCount >= search.threshold:
						return [cellNeighbors[i].x, cellNeighbors[i].y]
				openSet.append(cellNeighbors[i])

	#print("didn't find a spot")
	return [targetX, targetY]


class Simulation:

	def __init__(self, simNumber, totalRuns, sizeX, sizeY, population, threshold1, threshold1Percent=1, threshold2=0):
		
		self.simNumber = simNumber
		self.totalRuns = totalRuns
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.population = population
		self.threshold1 = threshold1
		self.threshold1Percent = threshold1Percent
		self.threshold2 = threshold2
		self.worlds = []
		print("Calculating run    0 for simulation %2d") % (simNumber)
		self.worlds.append(SpawnWorld(sizeX, sizeY, population, threshold1, threshold1Percent, threshold2))
		#run the simulation
		for i in (range(self.totalRuns)):
			print("Calculating run %4d for simulation %2d") % (i+1, simNumber)
			self.worlds.append(UpdateWorld(self.worlds[i]))


	def show(self, showRuns, setting = 'id'):
		"""
		This function lets you print any of the simulation runs 
		that were calculated.
		Parameters:
			showRuns - an array of integers that represent the 
				runs that should be displayed
			setting - either 'id', 'threshold', or 'satisfied'; use
			to specify the display to show a property
		Returns:
			nothing
		"""
		#iterate through runs to show
		if type(showRuns).__name__ == 'int':
			run = showRuns
			showRuns = []
			showRuns.append(run)
		for i in range(len(showRuns)):
			if i >= 0 and showRuns[i] < len(self.worlds):
				ShowWorld(self.worlds[showRuns[i]], self.simNumber, showRuns[i], self.threshold1, self.threshold1Percent, self.threshold2, setting)
			else:
				print("Entered simulation number %d is invalid and therefore was not displayed. \n") % (showRuns[i])

if __name__ == '__main__':
	simA = Simulation(1,10,50,50,0.6,5)
	simA.show(range(10))
	#simA.show([4], "satisfied")