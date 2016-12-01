import numpy

import loaddata
import sys



def main():
	
filename=sys.argv[2]
	
data = loaddata.load(filename)
	
print(filename)
	
print(data.mean(axis=1))



main()
