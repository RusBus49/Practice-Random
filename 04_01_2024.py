my_age = 25
her_age = 23
print(my_age - her_age)

def simple():
  global my_age
  my_age = str(25)
  her_age = str(23)
  print("Janelle is " + her_age)
simple()

april = "April Fools"

print(april.index("i"))

stats = (int(70), int(200), int(25))
height, weight, age = stats

def BMI():
  weight // height**2
BMI()
#not sure why this wont print the result

print(type(april))
print(type(age))
print(type(my_age))

#complex type
x = 1j
print(type(x))
#dict type
x = {height : 70, weight : 200}
print(type(x))

'''
three types of numbers are int float and complex
int are whole numbers, can be + or -
floats contain one or more decimals
floats can also have e for the power of 10 (12e3)
complex numbers use j as the imaginary part
'''
#making a random number
import random
print(random.randrange(1,10))

a = """There once was a man,
He ate a ham,
And threw it all up."""
print(a)
#for each number in the string print the number
for x in "taco":
  print(x)

txt = "Janelle is a cutie"
print("cutie" in txt)
#or we can do it with an if statement
if "cutie" in txt:
  print("Yes she is a cutie")

if "dummy" not in txt:
  print("and not a dummy")

