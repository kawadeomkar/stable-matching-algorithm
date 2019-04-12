# stable matching
import copy 

class StableMatching:
	
	def __init__(self, bigs, littles):
		'''
		self.bigs: dictionary of bigs and their preferences
		self.littles: dictionary of littles and their preferences
		self.matches: matching result after running match function
		'''
		self.bigs = bigs
		self.littles = littles
		self.matches = {}

	def accuracy(self):
		'''
		Returns accuracy of matching
		'''
		littleScore, bigScore, length = 0, 0, 0
		tempBigsDict = {}
		
		for little, big in self.matches.items():
			# take the inverse index and divide by length of list (subtract 1 for base 0)
			littleScore += float(len(self.littles[little]) - 1 - self.littles[little].index(big))/(len(self.littles[little]) - 1) 
			tempBigsDict[self.matches[little]] = little
			# TEMP, make class variable
			length = len(self.littles[little])

		for big, little in tempBigsDict.items():
			# take the inverse index and divide by length of list (subtract 1 for base 0)
			bigScore += float(len(self.bigs[big]) - 1 - self.bigs[big].index(little))/(len(self.bigs[big]) - 1) 
		
		print("Littles Accuracy: " + "{0:.0%}".format(littleScore/length))
		print("Bigs Accuracy: " + "{0:.0%}".format(bigScore/length))	
					
	def match(self):
		'''
		creates copies of big and little preferences and runs gale shapley's stable
		matching algorithm (both are bipartite graphs). 
		returns stable matching pairs
		'''
		matches = {}
		
		# get deep copies of both preference lists
		bigPrefs = copy.deepcopy(self.bigs)
		littlePrefs = copy.deepcopy(self.littles)
		currLittles = set()
	
		while len(matches) != len(self.bigs):
			for big, preferences in bigPrefs.items():
				if big not in matches.values():
					potentialLittle = preferences.pop(0)
					if potentialLittle not in currLittles:
						matches[potentialLittle] = big
						currLittles.add(potentialLittle)
					else:
						# check if  preference of current matching is less than  potential match
						if self.littles[potentialLittle].index(matches[potentialLittle]) > self.littles[potentialLittle].index(big):
							matches[potentialLittle] = big
		self.matches = matches
		return matches

					
	

