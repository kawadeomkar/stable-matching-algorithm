# demo.py
import sys
import getopt
from stable_matching import *

def preprocess(inputFile1, inputFile2):
	big, little = {}, {}
	# open first file 
	with open(inputFile1) as ifile1:
		for line in ifile1:
			line = line.rstrip().split(':')
			big[line[0]] = line[1].split(', ')
	# open second file
	with open(inputFile2) as ifile2:
		for line in ifile2:
			line = line.rstrip().split(':')
			little[line[0]] = line[1].split(', ')

	return big, little
	
# print if input is incorrect
def printHelp():
	print("Please enter in the format demo.py --ifile=<inputfile>,<inputfile> --ofile=<outputfile>")

# print out preference list, formatted
def printFormattedPrefList(bigs, littles):
	print("---BIGS PREFERENCES---")
	for big, prefList in bigs.items():
		littlesList = ", ".join(prefList)
		print(big + ": " + littlesList)
				
	print("---LITTLES PREFERENCES---")
	for little, prefList in littles.items():
		bigsList = ", ".join(prefList)
		print(little+ ": " + bigsList)


if __name__ == '__main__':
	opts = ''
	args = ''
	inputFile1 = ''
	inputFile2 = '' 
	outputFile = ''

	try:
		opts, args = getopt.getopt(sys.argv[1:], "h", ["ifiles=", "ofile="])
	except getopt.GetoptError:
		printHelp()	
	
	if len(opts) > 0:
		for opt in opts:
			if '-h' in opt:
				print("Hello, please enter in two text files containing your matching preferences " +
					"and an output file where you'd like to store the results. Check the README.md " + 
					"for more information")
				sys.exit()
			elif '--ifiles' in opt:
				ifiles = opt[1].split(',')
				if len(ifiles) != 2:
					printHelp()
				else:
					inputFile1 = ifiles[0]
					inputFile2 = ifiles[1]
			elif '--ofile' in opt:
				outputFile = opt[1]

		bigList, littleList = preprocess(inputFile1, inputFile2)
		printFormattedPrefList(bigList, littleList)	
		
		matcher = StableMatching(bigList, littleList)
		print(matcher.match())
		matcher.accuracy()
