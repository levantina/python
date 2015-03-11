#! /usr/bin/python\r

import sys, string, math, traceback

fin = open("matr3_disprot45kd.txt", "r")
fout = open("shells3_disprot45kd.txt", "w")
fd = open("degdistr3_disprot45kd.txt", "w")
i,l,max=0,0,0
nprot = 0

leggo = fin.readlines()
for i in xrange(0,len(leggo)):
	leggo[i]=leggo[i].strip("\n")

proteine = []
vertici = []
el = 0
degmax = 0
i,j=0,0

while (i < len(leggo)):
	s = leggo[i]
	if s != "" and s[0]!="#":
		link = []
		while (j < len(s)):
			if int(s[j])!=0 and el!=j:
				link.append(j)
			else: pass
		el = el+1
		vertici.append(link)
		if len(link)>degmax:
			degmax = len(link)
		else: pass
		j += 1
		
	elif s == "" and vertici != []:
		proteine.append(vertici)
		vertici = []
		el = 0
	else: pass
	i += 1
	
n = 0	
while (n < len(proteine)):
	if proteine[n] == []:
		del proteine[n]
	else: pass
	n += 1


print len(proteine)
print "deg ", degmax
degdistr = []
#stampo 3 distribuzione dei gradi per 3 proteine a caso nella famiglia
for d in (0,int(len(proteine)/2),len(proteine)-1):
	deg = {}
	ver = proteine[d]
	for u in xrange(0,degmax+1):
		deg[u] = 0.0
		
	for v in xrange(0,len(ver)):
		deg[len(ver[v])] = deg[len(ver[v])]+1
	for i in deg.keys():
		if deg[i]!=0:
			deg[i] = float(deg[i]/len(ver))
		else: pass
	degdistr.append(deg)

fd.write("#Distribuzione dei gradi per 3 proteine a caso della famiglia\n")
for d in xrange(0,len(degdistr)):
	dict = degdistr[d]
	keys = dict.keys()
	keys.sort()
	for key in keys:
		if dict[key]!=0:
			fd.write("%d %f\n" % (key, dict[key]))
		else: pass
	fd.write("\n")


coda = [] #la queue di appoggio per il pruning
vertici = [] #la lista di adiacenza di 1 proteina per volta
shells = [] #contiene la struttura a shells di 1 proteina per volta
allshells = [] #ogni indice contiene la struttura a shells di una proteina
newmax = 0

for n in xrange(0,len(proteine)):
	vertici = proteine[n]
	print "#amm", len(vertici)
	cut = []
	shells = []
	shell = []
	for u in xrange(0,len(vertici)):
		cut.append("uncut")
		if len(vertici[u])>newmax:
			newmax = len(vertici[u])
		elif vertici[u] == []: #se il vertice non ha vicini
			shell.append(u) #individuo la 0-shell
			cut[u] = "cut" #e lo poto
		else: pass
	degmax = newmax
	shells.append(shell)
	for k in xrange(2,degmax+1):
		shell = []
		for i in xrange(0,len(vertici)):
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
			for j in xrange(0,len(vertici[primo])):
				vicini = vertici[primo][j] #vicini del primo vertice potato
				for v in xrange(0,len(vertici[vicini])):
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
		#print newmax
		shells.append(shell)
		
	for i in xrange(0,len(vertici)):
		#print "resta", len(vertici[i])
		if cut[i]!="cut":
			coda.append(i)
		else: pass
		
	shells.append(coda) #il core massimo
	allshells.append(shells)


fout.write("#struttura a shells delle proteine\n")
for n in xrange(0, len(allshells)):
	for i in xrange(0, len(allshells[n])):
		if len(allshells[n][i])!=0:
			fout.write("%d %f\n" % (i, float(len(allshells[n][i]))/float(len(proteine[n]))))
	fout.write("\n")


fin.close()
fout.close()
fd.close()