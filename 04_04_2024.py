b = "Hello World"
print(b.strip())
print(len(b))
print(b[2:5])
print(b.split("o"))
print(b.count("o"))
#can combine strings and numbers with format()
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print(10 > 9)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

number = int(input("Pick a number between 1 and 10 "))
def number_guess():
  import random
  n = random.randint(1,2)
  if n == number:
    print("Good guess!")
  if n != number:
    print("Better luck next time.")
    exit()

number_guess()

x = int(input("Give a number for X "))
y = int(input("Give a number for Y "))

z = x+y
print(z)

name = input("What is your name? ")
def hello():
  if name == "Russell":
    print("Welcome back sir.")
  if name != "Russell":
    print("What do you want?")
    
hello()

