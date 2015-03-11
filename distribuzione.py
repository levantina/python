#! /usr/bin/python\r

import sys, string, math, traceback

fin = open("distribuzione_vect1.txt", "r")
fout = open("distribuzioneP_vect1.txt", "w")

linee = fin.readlines()
distr = []
d = []
fin.close()

MIN = 1000000.0
MAX = 0.0
i = 0
while i < len(linee):
	s = linee[i].split()
	if len(s)==2:
		d.append(float(s[0].strip()))
		distr.append(float(s[1].strip()))
	i += 1
	

if len(d)==len(distr) and len(d)!=0:
	print "ok ", len(d) 
else: print "no"

fout.write("#Distribuzione p(d) delle distanze dei vettori di idrofobicita\n")
j = 0
while j < len(distr)-1:
	fout.write("%f\t%f\n" % (d[j], abs(float(distr[j]-distr[j+1]))))
	j += 1

fout.write("%f\t%f\n" % (d[len(d)-1], distr[len(distr)-1]))

fout.write("\n")
fout.close()

	
