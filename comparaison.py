#oublies pas le aaa[] 
import re
import os 
import filecmp

def main(taihu, light):
	global path
	global path2
	global arm
	global arm2

	if taihu[-1] == "/":
		taihu = taihu[:-1]
	if light[-1] == "/":
		light = light[:-1]

	arm = taihu.count("/")
	arm2 = light.count("/")

	debianhuit(taihu, light)

developement = 0

def debianhuit(path, path2):

	abst = path.count("/")

	fichier=[]

	with open("donnesfich.txt", "a") as fich:
		fich.write("")

	for root, dirs, files in os.walk(path):  
		for i in files:
			fichier.append(os.path.join(root, i))

	for a in fichier:
		
		v = a + "}]{" + "1" + "\n"

		with open("donnesfich.txt", "r") as tes:
			t = tes.read()

		if not a + "}]{" in t:
			if os.path.exists(a):
				with open("donnesfich.txt", "a") as fich:
					fich.write(v)

	with open("donnesfich.txt", "r") as rt:
		fallout4 = rt.read()

	trouverr = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]
	aar = trouverr(fallout4, '\n')

	superposition = ""

	suppr = []

	b = 0
	jsp = []
	while b < len(aar):

		if b == 0:
			tuer = fallout4[0:aar[b]]
			ar = tuer.find('}]{')
			quantique = tuer[:ar]
			try:
				with open(quantique): pass
			except:
				jsp.append(tuer)
		else:
			tuer = fallout4[aar[b-1]:aar[b]]
			ar = tuer.find('}]{')
			quantique = tuer[1:ar]
			try:
				with open(quantique): pass
			except:
				jsp.append(tuer)

		b = b + 1

	for marre in jsp:
		fallout4 = fallout4.replace(marre, "")

	with open("donnesfich.txt", "w") as fich:
		fich.write(fallout4)

	rmls(path, path2)

def rmls(path, path2):
	global developement
	global develop
	global tl
	fichier=[]
	fichier2=[]
	trouver = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]

	for root, dirs, files in os.walk(path):  
		for i in files:  
			fichier.append(os.path.join(root, i)) 

	for root, dirs, files in os.walk(path2):  
		for i in files:  
			fichier2.append(os.path.join(root, i))

	nb = 1

	testfi = []
	testfi2 = []


	for g in fichier:

		aaa = trouver(g, '/')
		m = aaa[arm]
		g = g[m:]
		testfi.append(g)

	for h in fichier2:

		aaa = trouver(h, '/')
		k = aaa[arm2]
		h = h[k:]
		testfi2.append(h)

	develop = 0

	gg = []
	hh = []
	ajouter = []

	for z in testfi:
		if not z in testfi2:
			develop = develop + os.path.getsize(path+z)
			ajouter.append(z)


	for z in testfi:
		for y in testfi2:
			if z == y:			
				gg.append(z)
				hh.append(y)



	with open("donnesfich.txt", "r") as tes:
		tl = tes.read()

	aar = trouver(tl, '\n')
	bb = 0
	fin = []
	maalov = []

	while bb < len(gg):

		if filecmp.cmp(path2 + gg[bb], path + hh[bb]):

			bb = bb+1

		else:
			fin.append(gg[bb])

			developement = developement + os.path.getsize(path+gg[bb])
			maalov.append(bb)
			bb = bb+1

	pulsar = 0
	continu = []
	presquelafin = []
	fin2 = []

	y = 0
	hp = 0

	gf = ""
	for a in ajouter:
		fin.append(a)
	print fin

	for rm in fin:
		ad = tl.find(rm)
		kk = tl.find("\n", ad)
		hg = tl[ad:kk]

		presquelafin.append(hg)
		fr = hg.find("}]{")
		tch = hg[fr+3:]

		alle = int(tch)
		alle = alle+1
		hg = hg.replace(hg, hg[:fr+3]+str(alle))
		fin2.append(hg)

	ss = 0
	for msi in fin2:
		tl = tl.replace(presquelafin[ss], msi)
		ss = ss+1

	with open("donnesfich.txt", "w") as intel:
		intel.write(tl)

	print "difference:", convertm(developement)
	print "a ajouter:", convertm(develop)

	raspberry()

def convertm(developement):
	destruct = "octets"

	vm = (int(len(str(developement)))-1)/3

	destruct = "octets"

	if vm == 1:
		destruct = " ko "
	elif vm == 2:
		destruct = " mo "
	elif vm == 3:
		destruct = " go "
	elif vm == 4:
		destruct = " to "

	if not destruct == 0:
		developement = float(developement)/10**(vm*3)

	redirection = round(developement, 2)

	return str(redirection) + destruct

def raspberry():
	global tl
	trouverr = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]
	fallout4 = tl
	aar = trouverr(fallout4, '\n')
	superposition = ""
	b = 0
	while 1:
		try:
			if b == 0:
				tuer = fallout4[0:aar[b]]
			else:
				tuer = fallout4[aar[b-1]:aar[b]]
			ar = trouverr(tuer, '/')
			quantique = tuer[ar[arm]:]
			superposition = superposition + quantique+ "\n"
			b = b + 1

		except IndexError:
			break
	
	with open("serveur.txt", "w") as southnorth:
		southnorth.write(superposition)

print 'si vous etes sur windows evitez les "\\" pour le chemin du dossier, mrc'
km = raw_input("chemin vers l'ancien dossier dossier (depuis la racine) : ")
kh_ma = raw_input("chemin vers le nouveau dossier (depuis la racine) : ")

main(km, kh_ma)
