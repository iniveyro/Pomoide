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

print(f" ")
print(f"*----- Pomoide -----*")
print(f" ")

band="1"
minu = int(input("Type minutes of the round: "))
bre = int(input("Type minutes of the break: "))
lonbre = int(input("Type minutes of the long break: "))
rounds = int(input("Type quantity of rounds: "))

print("When you be ready, press ENTER...")
input()

while band == "1":

	numsess=1
	while numsess <= rounds:
	
		print(f"Round: {numsess}/{rounds}")
		print("Come on! Its time of work m8!")
		countdown(minu*60)
		numsess=numsess+1
		print("Its time of a little break")
		countdown(bre*60)
	
	print("Its time of a long break")
	countdown((lonbre)*60)
	print("")
	print("When you be restart the pomodore, press ENTER or type another key...")
	band= input()
	if (band != "1"):
		rounds = int(input("How many more rounds?: "))

print("FINISH")
