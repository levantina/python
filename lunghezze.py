#! /usr/bin/python\r

import sys, string, math, traceback

fli = open("disprot_4.5_fastaA.txt", "r")
fo = open("lunghezze.txt", "w")
linee = fli.readlines()

N = []
p = []
i, j = 0, 0 
#creo una lista di stringhe (ogni stringa e una proteina)
for i in xrange(0, len(linee)):
	if linee[i].find("DisProt")>0: #riconosco una proteina dall'intestazione
		s2=" "
	elif linee[i].find("DisProt")<0 and linee[i]!="\n":
		s1 = str(linee[i].strip("\n"))
		s2 = s2 + s1  #concateno tutte le stringhe di una stessa proteina
	elif linee[i] == "\n":
		p.append(s2.strip()) #inserisco la proteina completa in una lista
		N.append(len(s2))
		j = j+1
	else: pass
print j

i=0
while i<len(N):
	fo.write("%d\n" % N[i])
	i +=1
fo.close()
