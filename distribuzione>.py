#! /usr/bin/python\r

import sys, string, math, traceback

BIN = 0.1

fin = open("distanze_vettori_kd.txt", "r")
fout = open("distribuzione>_vectL2.txt", "w")

linee = fin.readlines()
dist = []
fin.close()

MIN = 1000000.0
MAX = 0.0

for i in xrange(1,len(linee)):
	s = linee[i].strip()
	if s!="":
		dist.append(float(s))
		if float(s) < MIN:
			MIN = float(s)
		if float(s) > MAX:
			MAX = float(s)
		
fout.write("#Distribuzione P_>(d) delle distanze dei vettori di idrofobicita\n")
d = 0.0
frac = 0.0
while(d <= MAX):
	for dd in dist:
		if dd > d:
			frac += float(1.0/len(dist))
	fout.write("%f %f\n" %(d,frac))
	d+= BIN
	frac = 0.0


fout.write("\n")
fout.close()

	
