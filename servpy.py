# coding: utf-8 
import socket
import threading
import sqlite3


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self):
   
        print("Connection de %s %s" % (self.ip, self.port, ))

        r = self.clientsocket.recv(2048)
        st = str(r)
        st = st[2:-1]
        rs = st.find("||")
        print("Ouverture du fichier pour le compte: " + st[:rs] + "...")
        with open(self.ip + ".txt", "w") as watch:
            watch.write(st[:rs] + st[rs+2:])
        fp = r
        self.clientsocket.send(xunil.encode())

        conn = sqlite3.connect('ma_base.db')

        cursor = conn.cursor()
        user = "mad"

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS """+ user + """(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             mld TEXT,
             dos TEXT
        )
        """)

        conn.commit()

        cursor.execute("""
        INSERT INTO """ + user + """(mld, dos) VALUES(?, ?)""", (st[:rs], st[rs+2:]))

        cursor.execute("""SELECT mld, dos FROM """ + user)
        user1 = cursor.fetchone()
        print(user1)

        print("Client déconnecté... et ")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

try:
    with open("client.txt", "r") as msf:
        xunil = msf.read()
except IOError:
    print "erreur lors de l'ouverture de : " + "client.txt"

while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()