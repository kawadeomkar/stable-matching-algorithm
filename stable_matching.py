# stable matching 

class StableMatching:
	
	def __init__(self, bigs, littles):
		'''
		self.bigs: dictionary of bigs and their preferences
		self.littles: dictionary of littles and their preferences
		'''
		self.bigs = bigs
		self.littles = littles
	
	def match():
		'''
		creates copies of big and little preferences and runs gale shapley's stable
		matching algorithm. 
		returns stable matching pairs
		'''
		matches = {}
		
		# get deep copies of both preference lists
		bigPrefs = self.bigs.copy()
		littlePrefs = self.littles.copy()
		currLittles = set()
	
		while len(matches) != len(self.bigs):
			for big, preferences in bigPrefs.items():
				if big not in matches.values():
					potentialLittle = preferences.pop(0)
					if potentialLittle not in currLittles:
						matches[potentialLittle] = big
						curLittles.add(potentialLittle)
					else:
						# check if  preference of current matching is less than  potential match
						if self.littles[potentialLittle].indexOf(matches[potentialLittle]) > 
							self.littles[potentialLittle].indexOf(big):
							matches[potentialLittle] = big
		return matches

					
	

