import socket
import json

iid_tasks = 0

class Task: #klasa zadan
	iid = iid_tasks
	priority = 0
	name = "Nowe zadanie"
	def __init__(self, newPriority, newName):
		self.priority = newPriority
		self.name = newName
		self.iid = iid_tasks + 1

Tasks = [] # tablica zadan
Tasks = list(map(Task, Tasks)) #mapowanie tablicy

def SaveToFile():
	with open('TODO.json', 'w+') as file:
		for i in range(len(Tasks)):
			json.dump({'\nID zadania: ': Tasks[i].iid, '\nZadanie: ': Tasks[i].name, '\nPriorytet: ': Tasks[i].priority}, file)
	return

def ShowTasks():
	print("Twoje zadania do wykonania: \n")
	for i in range(len(Tasks)):
		print("\n" + str(Tasks[i].iid))
		print("\n" + Tasks[i].name)
		print("\n" + "Priorytet: " + str(Tasks[i].priority))
	SaveToFile()
	return

def AddNewTask():
	mes = klient.recv(1028).decode()
	tab = mes.split("/")
	newName = tab[0]
	newPriority = int(tab[1])
	NewTask = Task(newPriority, newName)
	Tasks.append(NewTask)
	print("Dodano nowe zadanie")
	klient.send("Dodano nowe zadanie".encode())
	SaveToFile()
	return

def ShowTasksWithPriority():
	choice_tmp = klient.recv(2).decode()
	choice = int(choice_tmp)
	counter = 0
	for i in range(len(Tasks)):
		if choice == Tasks[i].priority:
			print("\nID: " + str(Tasks[i].iid))
			print("\n" + Tasks[i].name)
			counter = counter + 1
	if counter == 0:
		print("Nie ma zadania o danym priorytecie")
	return

def DeleteTask():
	id_tmp = klient.recv(2).decode()
	id = int(id_tmp)
	counter = 0
	for i in range(len(Tasks)):
		if id == Tasks[i].iid:
			Tasks.remove(Tasks[i])
			counter = counter + 1
	if counter == 0:
		print("Nie ma takiego zadania")
	SaveToFile()
	return

def Fun(wybor_user):
	if wybor_user == 1:
		ShowTasks()
	elif wybor_user == 2:
		ShowTasksWithPriority()
	elif wybor_user == 3:
		AddNewTask()
	elif wybor_user == 4:
		DeleteTask()
	else:
		klient.send("0").encode()
		pass

serwer = socket.socket()
host = socket.gethostname()
port = 8888
serwer.bind((host, port))
serwer.listen(20)
klient, adres = serwer.accept()
print("Jest polaczenie", adres)

make = "1"
klient.send("1".encode())
while (make == "1"):
	klient.send("\nWitaj w aplikacji do tworzenia listy TODO".encode())
	wybor = klient.recv(2).decode()
	choice = int(wybor)
	Fun(choice)
	make = klient.recv(2).decode()

klient.close()