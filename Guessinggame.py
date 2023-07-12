import random
print("\nWelcome to number guessing game :) ")
top_range=input("\nEnter a range to guess a number :")

if top_range.isdigit():
	top_range=int(top_range)

	if top_range<=0:
		print("Please enter the correct number :")
		quit() 
else:
	print("Please enter a number next time! Good Bye!!")
	quit()
random_no=random.randint(1,top_range)
#print(random_no)
guesses=0
while True:
	guesses+=1
	user_guess=input("Make a number guess :")
	if user_guess.isdigit():
		user_guess=int(user_guess)
	if user_guess==random_no:
		print("You Got it Right")
		break
	elif user_guess<random_no:
		print("You are below the number :")
	else:
		print("You are above the numer :")

print("You got it in",guesses,"guesses")