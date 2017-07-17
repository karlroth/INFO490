#!/usr/bin/env python3

import sys 

# We explicitly define the word/count separator token.
sep = '\t'

# We open STDIN and STDOUT
with sys.stdin as fin:
	with sys.stdout as fout:
	
		# Keep track of current city and count 
		ccity = None 
		ccount = 0
		city = None
	
		# For every line in STDIN
		for line in fin:

			# Split word into city and count, based on
			# predefined separator token.
		
			city, scount = line.split('\t', 1)

			# Assume count is always an integer
	
			count = int(scount)

			# city is either repeated or new

			if ccity == city:
				ccount += count
			else:
				# We have to handle the first city explicitly
				if ccity != None:
					fout.write("{0:s}{1:s}{2:d}\n".format(ccity, sep, ccount))
			
				# New city, so reset variables
				ccity = city
				ccount = count
		else:
			# Output final word count
			if ccity == city:
				fout.write("{0:s}{1:s}{2:d}\n".format(city, sep, ccount))
