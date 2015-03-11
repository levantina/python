#! /usr/bin/python\r

import sys, string, math, traceback

fli = open("disprot_4.5_fastaA.txt", "r")
#leggo la famiglia di proteine da file (txt)	
linee = fli.readlines()

fout = open("taglie.txt", "w")
amm = []
control = 0
while control < 8001:
	amm.append(0)
	control +=1


i,j=0,0
count = 0
s2 = ""
#creo una lista di stringhe (ogni stringa e una proteina)
while i < len(linee):
	linee[i] = linee[i].strip()
	if linee[i].find("DisProt")==1:
		if len(s2)!=0 and count !=0:
			amm[len(s2)] += 1
									
		s2=""
		count += 1
		i += 1
		print "#prot: ", count
	else:
		s1 = str(linee[i])
		s2 = str(s2 + s1)
		i +=1

i = 0

while i< len(amm):
	if amm[i]!= 0:
		fout.write("%d %d\n" %(i, amm[i]))
	i += 1	

i = 0
aa = 0
a = []
N = 1

while i < len(amm):
	if i%100 == 0 and i!=0:
		aa += amm[i]
		a.append(aa)
		aa = 0

	aa += amm[i]
	
	i += 1

fout.write("\n")	
i = 0
while i <len(a):
	fout.write("%d %d\n" %(i, a[i]))
	i +=1
		
fout.write("\n")
fout.close()
