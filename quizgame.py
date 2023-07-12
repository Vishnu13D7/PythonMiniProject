print("Welcome to Spell Be Quiz Game")
g=input("\nDo you want to play the quiz game? ")
if g.lower()!="yes":
	quit()
print("\nOkay! Lets Rock!")
score=0
count=0
flag = False
while(flag == False and count<3):
	Q1=input("Q1)What Does CPU Stand For? ")
	if Q1.lower()=="central processing unit":
		print("Correct")
		score+=1
		flag=True
		break
	else:
		print("Incorrect")
		count+=1
		if(count<2):
			print("Please Try again : only "+ str((3-count))+" attempt left")
		else:
			print("maxinmum attempt reached!")
count=0
flag = False
while(flag == False and count<3):
	Q2=input("Q2)What Does GPU Stand For? ")
	if Q2.lower()=="graphical processing unit":
		print("Correct")
		score+=1
		flag=True
		break
	else:
		print("Incorrect")
		count+=1

Q3=input("Q3)What Does RAM Stand For? ")
if Q3.lower()=="random access memory":
	print("Correct")
	score+=1
else:
	print("Incorrect")


Q4=input("Q4)What Does PSU Stand For? ")
if Q4.lower()=="power supply":
	print("Correct")
	score+=1
else:
	print("Incorrect")

Q5=input("Q5)What Does PC Stand For? ")
if Q5.lower()=="personal computer":
	print("Correct")
	score+=1
else:
	print("Incorrect")

print("You have got " + str(score) +" Questions Correct")
print("You have got " + str((score/5)*100) +"%")