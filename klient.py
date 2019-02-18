import socket

klient = socket.socket() #nawiazanie polaczenia
host = socket.gethostname()
port = 8888
klient.connect((host, port))

make = klient.recv(2).decode()
while make == "1":
	print(klient.recv(1024).decode())
	menu_choice = "Wybierz, co chcesz zrobic: \n (1) Wyswietl zadania \n (2) Wyswietl zadania z danym priorytetem, \n (3) Dodaj nowe zadanie, \n (4) Usun zadanie \n (5) Wyjdz z programu \n"
	user_choose = input(menu_choice)
	user_ch = int(user_choose)
	klient.send(user_choose.encode()) #menu programu

	if user_ch == 5:
		klient.send("0".encode())
		klient.close()
		pass
	elif user_ch == 3:
		newName = input("Dodaj opis zadania: ")
		newPriority = input("Ustal priorytet: ")
		ToSend = newName + "/" + newPriority
		klient.send(ToSend.encode())
		print(klient.recv(50).decode())
		klient.send("1".encode())
	elif user_ch == 4:
		id_to_del = input("Podaj id zadania: ")
		klient.send(id_to_del.encode())
		klient.send("1".encode())
	elif user_ch == 2:
		prioToSend = input("Podaj priorytet: ")
		klient.send(prioToSend.encode())
		klient.send("1".encode())
	elif user_ch == 1:
		klient.send("1".encode())