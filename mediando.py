#! /usr/bin/python\r

import sys, string, math, traceback
MAX = 190

fin = open("distribu_def.txt","r")
fout = open("distrmedia.txt","w")

linee = fin.readlines()
fin.close()

diff = []
num = []
for j in xrange(0,MAX):
	diff.append(0)
	num.appen(0.0)

i=0
count = 0

while i<len(linee):
	if linee[i] == "\n":
		count += 1
	riga = linee.split(" ")
	if len(riga)==2:
		dd = int(float(riga[0].strip())*100)
		diff[dd] += float(riga[1].strip()))
	    num[dd] +=1
		
		i += 1

linee = []

for n in xrange(0,len(diff)):
	diff[n] = float(diff[n]/num[n])
	fout.write("%f %f\n" % (float(n/100),diff[n]))

fout.write("\n")
fout.close()

	