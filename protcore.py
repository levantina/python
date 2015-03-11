#! /usr/bin/python\r

import sys, string, math, traceback

SOGLIA = 2.0

fli = open("provetta.txt", "r")
fscale = open("kyle-doolittle-scale.txt", "r")
fout = open("struttura_cores2.txt", "w")

#creo il dizionario con la scala di idrofobicita
scala = fscale.readlines()
dict = {}
i=0

while i < len(scala):
	riga = string.split(scala[i],',')
	if len(riga) == 2:
		first = str(riga[0])  #lettera
		second = float(riga[1]) #numero
		dict[first] = round(second,2)
		i = i+1
	else:
		print "Errore nella lettura della scala di idrofobicita\n"
		break

#leggo la famiglia di proteine da file (txt)	
nomi = []
linee = fli.readlines()
count = 0
for i in range(0, len(linee)):
	if linee[i].find("DisProt")>0:
		nomi.append(linee[i]) #memorizzo l'intestazione di ciascuna proteina
		count = count +1
print count		
p = []
#creo una lista di stringhe (ogni stringa e una proteina)
for i in range(0, len(linee)):
	if linee[i].find("DisProt")>0:
		s2=" "
	elif linee[i].find("DisProt")<0 and linee[i]!="\n":
		s1 = str(linee[i].strip("\n"))
		s2 = s2 + s1
	elif linee[i] == "\n":
		p.append(s2.strip())
	else: pass

#associo i valori di idrofobicita ad ogni amminoacido per ogni proteina e creo N
N = []
for n in range(0,len(p)):
	nseq = []
	for a in range(0,len(p[n])):
		nseq.append(0)
	s = p[n]
	i=0	
	for j in range(0,len(s)):
		for x in dict.keys():
			if x == s[j]:
				nseq[i] = float(dict[x])
				i=i+1
	N.append(nseq)

#creo il grafo associto alla SOGLIA per ogni proteina e costruisco la matrice di adiacenza
i,j,k=0,0,0
m = []
	
for j in range(0,len(N)):
	s=N[j]
	l=p[j]
	prote=[]*len(s)
	for k in range(0,len(s)):
		prote.append([])
		for i in range(0,len(s)):
			if abs(s[k]-s[i]) <= SOGLIA and p[j][k]!=p[j][i]:
				prote[k].append(1) #la matrice la faccio quadrata per tutti gli elementi
			else: prote[k].append(0)
	m.append(prote)

#qui inizia il raccordo tra i due programmi
proteine = []
vertici = []
for i in range(0,len(m)):
	link = []
	for j in range(0, len(m[i])):
		for k in range(0,len(m[i][j])):
			if m[i][j][k]!=0:
				link.append(j)
			else: pass
		vertici.append(link)
	proteine.append(vertici)
	vertici = []
print "qui"
coda = [] #la queue di appoggio per il pruning
ver = [] #la lista di adiacenza di 1 proteina per volta
shells = [] #contiene la struttura a shells di 1 proteina per volta
allshells = [] #ogni indice contiene la struttura a shells di una proteina
newmax = 0

for n in range(0,len(proteine)):
	ver = proteine[n]
	print "#amm", len(ver)
	cut = []
	shells = []
	shell = []
	for u in range(0,len(ver)):
		cut.append("uncut")
		if len(ver[u])>newmax:
			newmax = len(ver[u])
		elif ver[u] == []: #se il vertice non ha vicini
			shell.append(u) #individuo la 0-shell
			cut[u] = "cut" #e lo poto
		else: pass
	degmax = newmax

	shells.append(shell)
	for k in range(2,degmax+1):
		shell = []
		for i in range(0,len(ver)):
			if len(ver[i])>newmax and cut[i]!="cut":
				newmax = len(ver[i])
			else: pass
			if len(ver[i])<k and cut[i]!="cut":
				shell.append(i)
				cut[i] = "cut" #indico che il vertice e stato potato durante il pruning	
				coda.append(i)
			else: pass
		while len(coda)>0:
			primo = coda.pop()
			for j in range(0,len(ver[primo])):
				vicini = ver[primo][j] #vicini del primo vertice potato
				for v in range(0,len(ver[vicini])):
					if primo == ver[vicini][v]:
						del vertici[vicini][v]
						break
					else: pass
				if len(ver[vicini])<k and cut[vicini]!="cut":
					coda.append(vicini)
					cut[vicini] = "cut"
					shell.append(vicini)
				else: pass
		degmax = newmax
		print newmax
		shells.append(shell)
		
	for i in range(0,len(ver)):
		print "resta", len(ver[i])
		if cut[i]!="cut":
			coda.append(i)
		else: pass
		
	shells.append(coda) #questo e il core massimo
	allshells.append(shells)
	
#print vertici,cut						
#print shells

fout.write("#struttura a shells delle proteine\n")
for n in range(0, len(allshells)):
	for i in range(0, len(allshells[n])):
		if len(allshells[n][i])!=0:
			fout.write("%d %f\n" % (i, float(len(allshells[n][i]))/float(len(proteine[n]))))
	fout.write("\n")

fli.close()
fscale.close()
fout.close()