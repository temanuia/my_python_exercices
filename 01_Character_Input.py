#http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

from datetime import date

#Ask the user to enter their name and their age
name = input("Give me your name: ")
age = input("Enter your age: ")

#Print out a message addressed to them that tells them the year that they will turn 100 years old.
yob=int(date.today().year)-int(age)
message=("Dear " + name + ", you will be 100 years old in " + str(yob+100) + ". ")
print(message)

#Ask the user for another number and printing out that many copies of the previous message.
repeat=int(input("How many times do you want to print the last message? "))
print(repeat*message)

#Print out that many copies of the previous message on separate lines.
print(repeat*(message+"\n"))

