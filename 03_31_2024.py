print("Hello World ")
# simple print command

# creating a variable
character_name = "Sam"
character_age = "12"
print("There once was a man named " + character_name + ", ")
print("He was " + character_age + ".")
# \n inside the quotes makes a new line

n1 = 0
added = n1 + 4
print(added)
# concatenation is combining two or more variables, have to be same string or integer
phrase = "Silly Goose"
print(phrase + character_name)

print(len(phrase))

# how to index a string
print(phrase.index("i"))

# replacing in a string
print(phrase.replace("Silly", "Wacky"))

# variable practice
x = str(3)
y = int(3)
z = float(3)

# unpacking a list
vegetables = [1,2,3]
a, b, c = vegetables
print(a)
print(b)
print(c)
print(sum(vegetables))
# using def to create a function that can be called on later
def chaos():
  print(phrase, y+a, vegetables)

chaos()

# global establishes a variable inside the function and out

x = ("apple", "banana", "cherry")
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

x = True
print(type(x))