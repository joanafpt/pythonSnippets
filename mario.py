
#Prints out any number of question marks, as specified by user
from cs50 import get_int
#Prompt user for a positive number
while True:
    n = get_int("Positive number: ")
    if n > 0:
        break
#Print out this many rows
for i in range(n):
    #Prints out this many columns
    for j in range(n):
        print("#", end="")
    print()