import time,os

def countdown (count):
	
	while count > 0:
		file = open("output/count.txt","w+")
		m, s = divmod(count,60)
		count_format = "{:02d}:{:02d}".format(m,s)
		print(count_format)
		file.write(count_format)
		time.sleep(1)
		count = count - 1

def action(rounds,numsess):
	
	while numsess <= rounds:
		
		print(f"Round: {numsess}/{rounds}")
		print("Come on! Its time of work m8!")
		countdown(minu*60)
		if numsess < rounds:
			print("Its time of a little break")
			countdown(bre*60)
		numsess=numsess+1
	
print(f" ")
print(f"*----- Pomoide -----*")
print(f" ")

minu = int(input("Agregue cuantos minutos durara cada ronda:"))
bre = int(input("Agregue cuantos minutos durara el break: "))
lonbre = int(input("Agregue cuantos minutos durara el break largo: "))
rounds = int(input("Agregue cantidad de rondas: "))

print("Cuando este listo presione ENTER...")
input()
program=True
numsess=1

while program == True:

	action(rounds,numsess)
	
	print("Its time of a long break")
	countdown(lonbre*60)
	print("")
	x=input("You need add more sessions? (S/N)").upper()
	
	if x == "N":
		program= False
	else:
		rounds=int(input("Type quantity of rounds: ")) + rounds
		print("When you be ready, press ENTER...")
		input()

print("Thx for use the app :D ")
