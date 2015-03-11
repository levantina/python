#! /usr/bin/python\r

import sys, string, math, traceback, random

fli = open("lettere.txt", "r")
fli2 = open("lunghezze.txt", "r")
flo = open("rand_disprot_ex.txt", "w")

#leggo la famiglia di proteine da file (txt)	
lettere = fli.readlines()
lung = fli2.readlines()
random.seed()
amm = []
seq = lettere[0]
i = 0
while i<len(seq):
	amm.append(seq[i])
	i+=1
	

i=0
while i < len(lettere):
	lettere[i] = lettere[i].strip()
	print "i", len(lettere[i])
	i +=1
print len(lettere)
print len(lung)

i = 0
p = []
while i < len(lung):
	s = lung[i].strip()
	if len(s) !=0:
		j=0
		flo.write(">DisProt\n")
		while j < int(s):
			index = random.randint(0,19)
			p.append(amm[index])
			j+=1
		k = 0
		while k<len(p):	
			flo.write("%s" % p[k])
			k+=1
		p = []
		flo.write("\n\n")
	i+=1


