#!/usr/bin/env python
from random import randint

class agent:
	def __init__(self, id, threshold):
		self.id = id
		self.threshold = threshold
		self.satisfied = False

def SpawnWorld(sizeX,sizeY,population,threshold):
	"""
	This function creates a 'sizeX' by 'sizeY' grid. Each cell in the 
	grid is randomly populated with an agent that identifies as an 'X',
	an 'O', or an empty cell (' ').
	Parameters:
		sizeX, SizeY - integers that define the size of the world
		population - a fraction of the number of cells that should 
			contain agents
		threshold - an integer 0 to 8 that defines how homophilous the
			 agent is (how many similar agents nearby are neccesary 
			 for the agent to be satisfied)
	Returns:
		matrix of agents, aka the 'world'
	"""
	#variables
	numX = 0
	numO = 0
	numAgent = int(sizeX*sizeY*population*0.5)
	numBlank = 0
	numNotAgent = sizeX*sizeY - numAgent*2
	#initialize our array
	world = []
	#populate the array
	for i in range(sizeY):
		tempRow = []
		largeNumber = 1000000;
		division1 = 0.5*population*largeNumber
		division2 = population*largeNumber
		for k in range(sizeX):
			randID = randint(0,largeNumber)
			if randID < division1:
				if numX < numAgent:
					tempAgent = agent('X', threshold)
					numX += 1
				elif numO < numAgent:
					tempAgent = agent('O', threshold)
					numO += 1
				else:
					tempAgent = agent(' ', 0)
					numBlank += 1
			if randID >= division1 and randID < division2:
				if numO < numAgent:
					tempAgent = agent('O', threshold)
					numO += 1
				elif numX < numAgent:
					tempAgent = agent('X', threshold)
					numX += 1
				else:
					tempAgent = agent(' ', 0)
					numBlank += 1
			if randID >= division2:
				if numBlank < numNotAgent:
					tempAgent = agent(' ', 0)
					numBlank += 1
				elif numX < numAgent:
					tempAgent = agent('X', threshold)
					numX += 1
				elif numO < numAgent:
					tempAgent = agent('O', threshold)
					numO += 1
				else:
					tempAgent = agent(' ', 0)
					numBlank += 1	
			#tempAgent = agent('X',threshold)		
			tempRow.append(tempAgent)
		world.append(tempRow)

	print ("numX = %d" % (numX))
	print ("numO = %d" % (numO))
	print ("numAgent = %d" % (numAgent))
	print ("numBLank = %d" % (numBlank))
	print ("numNotAgent = %d" % (numNotAgent))
	
	return world

def ShowWorld(world):
	#calculate size of world
	rows = len(world)
	columns = len(world[0])
	
	#function for printing top and bottom borders
	def PrintBorder():
		rowText = '-'
		for i in range(columns*2+2):
			rowText += '-'
		print rowText


	#iterate through world and print agent
	PrintBorder()
	for i in range(rows):
		rowText = '| '
		for k in range(columns):
			rowText += world[k][i].id + ' '
		rowText += "|"
		print rowText
		#print "\n"
	PrintBorder()

def Sim1():
	world_init = SpawnWorld(50,50,0.75,3)
	ShowWorld(world_init)

if __name__ == '__main__':
	Sim1()
