print("Hello World")
# question 01

seconds = int(60)
minutes = int(60)
hours = int(24)
days = int(365)

print("There are " + str(seconds) + " in a minute.")
print("There are " + str(seconds * minutes) + " in an hour.")
print(" There are " + str(hours * seconds * minutes) + " in a day.")
print("There are " + str(days * hours * seconds * minutes) + " in a year.")

# question 02
a= "Peter"
colour= "purple"

print(a + ':' + " couldnt you see that the traffic light was " + colour)
b= "Mary"
number= 13
noun= "fish"

print(b + ':' + " but I had", + number)
adjective= "sweet!"

print(a + ':' + "That is so " + adjective + " you couldve killed them.")

# question 03

year = int(input("Enter your birth year: "))
if year < 2000:
	print("Welcome from your previous century")
else:
	print("WELCOME")

# question 04
# Simple Interest = (Principal Amount * Rate of Interest * Number of Years) / 100

P = float(input("Enter Principal Amount:"))
r = float(input("Enter Rate of Interest:"))
t = float(input("Enter Number of Years:"))

print("SimpleInterest: {0}" .format(SimpleInterest))
def Simple_Interest_calculator(p,r,t):
	SimpleInterest = (p*r*t)/100

	print("SimpleInterest:{0}" .format(Simple_Interest_calculator(p,r,t)))
	





