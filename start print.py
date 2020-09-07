'''
A PROGRAM TO PRINT * 
Takes input from user and if no is odd it prints reverse 
and if input is even number it will print normal 

'''

print("Even number will give Straight and oDd will give Reverse")

def normalStar(mn):
	i=0
	j=0
	while(i<mn):
		for j in range(0,i+1):
			print("* ",end="")
		i+=1
		print("\n")

def reverseStar(mn):
	i=mn
	j=0
	while(i>0):
		for j in range(0,i):
			print("* ",end="")
		i-=1
		print("\n")


user_continue='y'

while (user_continue=='y'):
	user_d=int(input("enter number of max stars :  "))

	if user_d%2==0:
		normalStar(user_d)
		
	else:
		reverseStar(user_d)
			
	
	user_con=input("do you want to continue? Enter y/n :  ")
	if user_con=='n':
	 	break
	 	
		
		