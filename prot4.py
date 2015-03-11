#! /usr/bin/python\rimport sys, string, math, tracebackSOGLIA = 3.0fli = open("disprot_4.5_fastaA.txt", "r")fscale = open("kyle-doolittle-scale.txt", "r")flo1 = open("graf3_disprot45kd.txt", "w")flo2 = open("matr3_disprot45kd.txt", "w")#creo il dizionario con la scala di idrofobicitascala = fscale.readlines()dict = {}i=0while i < len(scala):	riga = string.split(scala[i],',')	if len(riga) == 2:		first = str(riga[0])  #lettera		second = float(riga[1].strip()) #numero		dict[first] = round(second,2)		i = i+1	else:		print "Errore nella lettura della scala di idrofobicita\n"		break#leggo la famiglia di proteine da file (txt)	linee = fli.readlines()count = 0for i in range(0, len(linee)):	if linee[i].find("DisProt")>0:		count = count +1print count		p = []i=0j=0#creo una lista di stringhe (ogni stringa e una proteina)for i in range(0, len(linee)):	if linee[i].find("DisProt")>0:		s2=" "	elif linee[i].find("DisProt")<0 and linee[i]!="\n":		s1 = str(linee[i].strip())		s2 = (s2 + s1).strip()	elif linee[i] == "\n":		p.append(s2.strip())		j = j+1	else: passprint j#associo i valori di idrofobicita ad ogni amminoacido per ogni proteina e creo NN = []for n in range(0,len(p)):	nseq = []	for a in range(0,len(p[n])):		nseq.append(0)	s = p[n]	i=0		for j in range(0,len(s)):		for x in dict.keys():			if x == s[j]:				nseq[i] = float(dict[x])				i=i+1	N.append(nseq)flo1.write("#Grafi: soglia idrofobicita = %f\n" % SOGLIA)#creo il grafo associto alla SOGLIA per ogni proteina e lo stampo come serie di archii,j,k=0,0,0m = []*len(N)for i in range(0,len(N)):	m.append([])	for j in range(0,len(N)):	s=N[j]	l=p[j]	prote=[]*len(s)	for k in range(0,len(s)):		prote.append([])		for i in range(0,len(s)):			if abs(s[k]-s[i]) <= SOGLIA and p[j][k]!=p[j][i]:				prote[k].append(1) #la matrice la faccio quadrata per tutti gli elementi				#if p[j][k]!=p[j][i]:				flo1.write("%d %d\n" % (k,i)) #la stampa degli archi e doppia ma senza loop				#else: pass			else: prote[k].append(0)	m.append(prote)	flo1.write("\n")#associo 1 o 0 alla presenza del link in una proteina e stampo la matrice quadrata corrispondenteflo2.write("#Matrici: soglia idrofobicita = %f" % SOGLIA)for x in m:	for y in x:		for z in y:			num = repr(z)			flo2.write(num)		flo2.write("\n")	flo2.write("\n")fli.close()fscale.close()flo1.close()flo2.close()