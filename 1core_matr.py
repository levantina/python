#! /usr/bin/python\r

import sys, string, math, traceback

fm = open("1matrice.txt", "r")
fcore1 = open("shells_soglia3kd.txt","a")
#fcore2 = open("shells_soglia2.txt", "a")
#fcore3 = open("shells_soglia3.txt","a")

line = fm.readlines()

print "#len", len(line)
vertici = []
link = []
el = 0
degmax = 0

for i in range(1,len(line)):
	riga = line[i].strip()
	link = []
	if len(riga)!=0:
		for j in range(0, len(riga)):
			if int(riga[j])!=0 and el!=j:
				link.append(j)
		el = el+1
		vertici.append(link)
		if len(link)>degmax:
			degmax = len(link)


fm.close()

newmax = 0
coda = []
print "#amm", len(vertici)
cut = []
shells = []
shell = []
for u in range(0,len(vertici)):
	cut.append("uncut")
	if len(vertici[u])>newmax:
		newmax = len(vertici[u])
	elif vertici[u] == []: #se il vertice non ha vicini
		shell.append(u) #individuo la 0-shell
		cut[u] = "cut" #e lo poto
	else: pass
degmax = newmax
shells.append(shell)
for k in range(2,degmax+1):
	shell = []
	for i in range(0,len(vertici)):
		if len(vertici[i])>newmax and cut[i]!="cut":
			newmax = len(vertici[i])
		else: pass
		if len(vertici[i])<k and cut[i]!="cut":
			shell.append(i)
			cut[i] = "cut" #indico che il vertice e' stato potato durante il pruning	
			coda.append(i)
		else: pass
	while len(coda)>0:
		primo = coda.pop()
		for j in range(0,len(vertici[primo])):
			vicini = vertici[primo][j] #vicini del primo vertice potato
			for v in range(0,len(vertici[vicini])):
				if primo == vertici[vicini][v]:
					del vertici[vicini][v]
					break
				else: pass
			if len(vertici[vicini])<k and cut[vicini]!="cut":
				coda.append(vicini)
				cut[vicini] = "cut"
				shell.append(vicini)
			else: pass
	degmax = newmax
	shells.append(shell)
		
for i in range(0,len(vertici)):
	if cut[i]!="cut":
		coda.append(i)
	else: pass
	
shells.append(coda) #il core massimo

for i in xrange(0,len(shells)):
	if len(shells[i])!=0:
		fcore1.write("%d %f\n" % (i, float(len(shells[i]))/float(len(vertici))))


fcore1.write("\n")
fcore1.close()

		