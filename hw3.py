#!/usr/bin/env python
from random import randint

class agent:
	def __init__(self, id, threshold):
		self.id = id
		self.threshold = threshold
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
				tempAgent = agent('X', threshold)
				numX += 1
			elif flagID == 'O':
				tempAgent = agent('O', threshold)
				numO += 1
			else:
				tempAgent = agent(' ', 0)
				numBlank += 1	

			#tempAgent = agent('X',threshold)		
			tempRow.append(tempAgent)
		world.append(tempRow)
	
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
	
	return world

def ShowWorld(world, setting='id'):
	"""
	This function prints the world into the terminal. You have
	the option of showing a property of the agent other than id.
	Parameters:
		world - pass in a matrix of agents, aka the world
		setting - either 'id', 'threshold', or 'satisfied'; use
			to specify the display to show a property; defaults
			to 'id'
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
		
		if setting == 'satisfied':
			widthWorld = columns*3+2
		
		for i in range(widthWorld):
			rowText += '-'
		print rowText


	#iterate through world and print agent
	PrintBorder()
	for i in range(rows):
		rowText = '| '
		for k in range(columns):
			if setting == 'threshold':
				if world[k][i].id != ' ':
					rowText += str(world[k][i].threshold) + ' '
				else:
					rowText += '  '					
			elif setting == 'satisfied':
				if world[k][i].id != ' ':
					if world[k][i].satisfied:
						rowText += ':) '
					else:
						 rowText += ':( '
				else:
					rowText += '   '
			else:
				rowText += world[k][i].id + ' '

		rowText += "|"
		print rowText
		#print "\n"
	PrintBorder()

def Sim1():
	world_init = SpawnWorld(50,50,0.75,3,.75,5)

	ShowWorld(world_init)
	#ShowWorld(world_init, 'threshold')
	#ShowWorld(world_init, 'satisfied')


if __name__ == '__main__':
	Sim1()
