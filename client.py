from tkinter import *
import os
import urllib.request
import socket

def destr():
	global entree
	global entre
	global r
	maalov = False
	value = entre.get() + entree.get()
	if not "||" in value:
		value = entree.get() + "||" + entre.get()
		maalov = True


	try:
		if maalov == True:
			if len(value) > 0:
				sdestr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sdestr.connect(("127.0.0.1", 1111))
				print("envoie de données: ")
				sdestr.send(value.encode())
				r = sdestr.recv(9999999)
				r = str(r)
				r = r[2:-1]
				r = r.replace("\\n", "\n")
				print(r)
				fenr(rx=70, ry=270, txt="update", cmd=raspberry)
		else:
			lab = Label(canvas, text="nop")
			lab.place(x=100, y=100)

	except:
		pass




def raspberry():
	global r

	darksouls = False

	minecraft = r

	with open("serveur.txt", "r") as rt:
		fallout4 = rt.read()

	with open("clientt.txt", "w") as jk:
		jk.write(r)
	with open("clientt.txt", "r") as rt:
		sheepwars = rt.read()

		darksouls = True

	trouverr = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]
	aar = trouverr(fallout4, '\n')

	superposition = []
	ajout = ""
	b = 0
	while 1:
		try:
			if b == 0:
				tuer = fallout4[0:aar[b]+1]
			else:
				tuer = fallout4[aar[b-1]+1:aar[b]+1]

			if not tuer in minecraft:
				google = tuer.find("}]{")
				tuer = tuer[1:google]
				if "/" in tuer:
					try:
						lol = trouverr(tuer, "/")
						js = tuer[lol[-1]:]
						urllib.request.urlretrieve("https://github.com/debianeuf/download/blob/master/" + tuer + "?raw=true", js)
					except urllib.error.HTTPError:
						print("erreur: impossible de telecharger le fichier: " + a_telecharger)
					except urllib.error.URLError:
						print("erreur lors du telechargement: svp veuillez verifier votre connexion")

				else:
					try:
						a_telecharger = "https://github.com/debianeuf/download/blob/master/" + tuer + "?raw=true"
						urllib.request.urlretrieve(a_telecharger, tuer)
					except urllib.error.HTTPError:
						print ("erreur: impossible de telecharger le fichier: " + a_telecharger)
					except urllib.error.URLError:
						print("erreur lors du telechargement: svp veuillez verifier votre connexion")
					
				if darksouls == True:
					ajout = ajout + tuer

			b = b + 1

		except IndexError:
			break

	if darksouls == True:
		with open("client.txt", "w") as jk:
			jk.write(ajout)




def onSup():
    for w in fen.winfo_children():
        w.destroy()

fen = Tk()
fen.geometry("800x500")
fen.configure(background="#010512")

photo = PhotoImage(file="1285656431.png")

canvas = Canvas(fen,width=800, height=500, bg="#010512",)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack(fill="both", expand="yes")

def fenr(rx, ry, txt, cmd):

	lg = Button(canvas, text =txt, width=22, bg="#010512", fg="white", command=cmd)
	lg.place(x=rx, y=ry)

fenr(rx=70, ry=70, txt="login", cmd=destr)
fenr(rx=70, ry=170, txt="rien", cmd="rien")

entree = Entry(canvas,bg="#010512", fg="white", width=30)
entree.place(x=300, y=70)
entre = Entry(canvas, bg="#010512", fg="white", width=30)
entre.place(x=300, y=110)

Frame2 = LabelFrame(canvas, borderwidth=2, relief=GROOVE, width=800, height=500)
Frame2.place(x=550, y=60)
liste = Listbox(Frame2, bg="#010512", fg="white", height=20)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")

liste.pack()

fen.mainloop()
