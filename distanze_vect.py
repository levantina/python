#! /usr/bin/python\r

import sys, string, math, traceback
L = 2 #lunghezza vettore di idrofobicita 2L+1
BIN = 0.01

fli = open("disprot_4.5_fastaA.txt", "r")
fscale = open("kyle-doolittle-scale.txt", "r")
fdist1 = open("dist_vettori_kd.txt", "w")
fdist2 = open("distanze_kd.txt", "w")

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
linee = fli.readlines()
count = 0
for i in xrange(0, len(linee)):
	if linee[i].find("DisProt")>0:
		count = count +1
print count		

p = []
i,j=0,0
#creo una lista di stringhe (ogni stringa e una proteina)
for i in xrange(0, len(linee)):
	if linee[i].find("DisProt")>0:
		s2=" "
	elif linee[i].find("DisProt")<0 and linee[i]!="\n":
		s1 = str(linee[i].strip("\n"))
		s2 = s2 + s1
	elif linee[i] == "\n":
		p.append(s2.strip())
		j = j+1
	else: pass
print j

#associo i valori di idrofobicita ad ogni amminoacido per ogni proteina e creo N

N = []
for n in range(0,len(p)):
	nseq = []
	for a in xrange(0,len(p[n])):
		nseq.append(0)
	s = p[n]
	i=0	
	for j in xrange(0,len(s)):
		for x in dict.keys():
			if x == s[j]:
				nseq[i] = float(dict[x])
				i=i+1
	N.append(nseq)

fdist1.write("#Distanze dei vettori di idrofobicita\n")
fdist2.write("#Distanze di idrofobicita\n")

min = 100000.0
max = 0.0
dist = []
i,j,k = 0,0,0
for i in xrange(0,len(N)):
	s = N[i]
	for j in xrange(0, len(s)):
		a = []
		if j < L:
			for l in xrange(-L+j,1):
				a.append(s[len(s)+l-1])
			for l in xrange(0,L+j):
				a.append(s[l])
		elif j > len(s)-1-L:
			for l in xrange(-L,1):
				a.append(s[l])
			for l in xrange(0,k-len(s)+1+L):
				a.append(s[l])
		else:
			for l in xrange(-L,L+1):
				a.append(s[j+l])

		for k in xrange(0, len(s)):
			if j!=k:
				diff = float(abs(s[j]-s[k]))
				fdist2.write("%f\n" % diff)
				d_jk = 0.0
				b = []
				if k < L:
					for l in xrange(-L+k,1):
						b.append(s[len(s)+l-1])
					for l in xrange(0,L+i):
						b.append(s[l])
				elif k > len(s)-1-L:
					for l in xrange(-L,1):
						b.append(s[l])
					for l in xrange(0,k-len(s)+1+L):
						b.append(s[l])
				else:
					for l in xrange(-L,L+1):
						b.append(s[k+l])


				for d in xrange(-L, L+1):
					d_jk += float(a[d]-b[d])**2
					d_jk = math.sqrt(d_jk)

				fdist.write("%f\n" % d_jk)
				
				if d_jk > max:
					max = d_jk
				elif d_jk < min:
					min = d_jk
				
print "max: ",max, "\nmin: ",min
print len(dist)

fdist1.write("\n")
fdist2.write("\n")
fli = close()
fscale = close()
fdist = close()


	