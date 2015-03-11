#! /usr/bin/python\r

import sys, string, math, traceback, os
from os import system

fli = open("matr3_disprot45kd.txt", "r")

#leggo le matrici da file
linee = fli.readlines()
fli.close()
righe = []
command = ("python2.5 /Users/Valentina/Documents/FISICA/lab_bio/matrici_/1core_matr.py")
count = 0
i,j=0,0
#creo una lista di stringhe (ogni stringa e una proteina)
for i in xrange(0, len(linee)):
	if linee[i][0]!= "\n":
		righe.append(linee[i].strip())
	elif linee[i][0] == "\n":
		count += 1
		print "#prot: ", count
		fmatr = open("1matrice.txt", "w")
		for l in xrange(0,len(righe)):
			fmatr.write("%s\n" % righe[l])
			
		fmatr.write("\n")
		fmatr.close()
		system(command)
		os.remove("/Users/Valentina/Documents/FISICA/lab_bio/matrici_/1matrice.txt")
			


	

