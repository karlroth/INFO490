#!/usr/bin/env python3 
import sys

#We explicitly define the seperator token.
sep = '\t'

#We open STDIN and STDOUT 
with sys.stdin as fin: 
	with sys.stdout as fout:

		header = 1

		#For every line in STDIN 
		for line in fin:
			if header == 1:
				header = 0
				continue 
			
			#Split data into columns
			data = line.split(',')
			
			#Grab the origin column
			city = data[16]
			
			#Send to STDOUT
			fout.write("{0}{1}1\n".format(city, sep))
		
		
		  

