# demo.py
import sys
import getopt


def preprocess(inputFile1, inputFile2, outputFile):
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

	
# print if input is incorrect
def printHelp():
	print("Please enter in the format demo.py --ifile=<inputfile>,<inputfile> --ofile=<outputfile>")


if __name__ == '__main__':
	opts = ''
	args = ''
	inputFile1 = ''
	inputFile2 = '' 
	outputFile = ''

	try:
		opts, args = getopt.getopt(sys.argv[1:], "h", ["ifiles=", "ofile="])
		print(opts)
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

	preprocess(inputFile1, inputFile2, outputFile)
