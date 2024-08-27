# Project one
print("_____________Hello World Print out_______________")
print("Hello World")
print("")
print("Project 1 completed🎇🎇🎇✨")
print("")

# project two
print("_____________Number Guessing Game_______________")
import random as kenny
while True:
    computer = kenny.randrange(50)
    user = input("Guess the number: ")
    print(computer)
    if user == "exit":
        break
    if int(user) == computer:
        print("correct🎈🎆🎇✨🎉")
    elif int(user) > computer:
        print("Too high")
    elif int(user) < computer:
        print("Too low")
    else:
        print("wrong input")
print("")
print("Project 2 completed🎇🎇🎇✨")
print("")
# project 3
print("_____________Calculator_______________")
value1 = int(input("input the first value:"))
operator = input("Choose a mathematical sign[+,-,/,%,*]")
value2 = int(input("Input the other value: "))
moreValue = input("do u want to input more value? (Yes | No)")
def val():
    while True:
        operator = input("Choose a mathematical sign")
        extravalue = int(input("input value"))
        moreValue = input("do u want to input more value? (Yes | No)")       
        if moreValue == "yes" or moreValue == "Yes" or moreValue == "YES":
            operator = input("Choose a mathematical sign")
            extravalue = int(input("input value"))
            moreValue = input("do u want to input more value? (Yes | No)")
        else:
            break
            

if moreValue == "yes" or moreValue == "Yes" or moreValue == "YES":
        val()
else:
    print("")
if operator == "+":
    print(value1 + value2)
elif operator == "-":
    print(value1 - value2)
elif operator == "/":
    print(value1 / value2)
elif operator == "*":
    print(value1 * value2)
elif operator == "%":
    print(value1 % value2)
else:
    while operator != "+" or operator != "-" or operator != "/" or operator != "*" or operator != "%":
        operator = input("pls input an operator ") 

print("")
print("Project 3 completed🎇🎇🎇✨")
print("")

# Project 4
print("_____________Hangman Game_______________")
words = "Compass"
print("An instrument use to get direction")
print("You have", len(words), "guesses")
print("one letter at a time| Let's Go🎈🎈🎈")
n = 0
for i in words:
    userguess = input("Guess the letter: ")
    if userguess != i:
        print("aww sorry")
        print(n, "is the number of letters u guessed right")
        break
    elif userguess == i:
        print("nice! move on")
    n += 1
print("")
print("Project 4 completed🎇🎇🎇✨")
print("")

# Project 5
import random as kenny
print("_____________Password Generator_______________")
length = int(input("How many characters do u want ur Password to contain (11 Recomended)\nPls input number only!!! "))
while length < 3:
    length = int(input("sorry,3 is the limit\nPls input another number "))
symbols = input("Should symbols be included(Yes | No)? ")
while symbols != "Yes" and symbols != "No":
    symbols =input("Should symbols be included(Yes | No)? ")
numbers = input("Should numbers be included (Yes | No)? ")
while numbers != "Yes" and numbers != "No":
    numbers = input("Should numbers be included(Yes | No)? ")
case = input("Does uppercase letters need to be included (Yes|No)? ")
while case != "Yes" and case != "No":
    case = input("Does uppercase letters need to be included (Yes|No)? ")
syslength = range(length)
sysymbols = ["!","@","#","$","_","~"]
sysnumber = list(range(10))
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print("Your", length, "character password is")
symbolrandom =str(kenny.choice(sysymbols))
numberrandom = str(kenny.choice(sysnumber))
letterrandom = kenny.choice(letters)
capitalLetterRandom = kenny.choice(letters).upper()
password = [symbolrandom, numberrandom, letterrandom, capitalLetterRandom]
def choose():
    print(kenny.choice(password), end="")
# length is 6, now i want to go into the password 6times but all should show
if symbols == "Yes" and numbers == "Yes" and case == "Yes":
    x = 0
    for y in password:
        print(y, end="")
        x += 1
    if x != length:
        symbolrandom =str(kenny.choice(sysymbols))
        numberrandom = str(kenny.choice(sysnumber))
        letterrandom = kenny.choice(letters)
        capitalLetterRandom = kenny.choice(letters).upper()
        password = [symbolrandom, numberrandom, letterrandom, capitalLetterRandom]
        new = length - x
        new = range(new)
        for m in new:
            symbolrandom =str(kenny.choice(sysymbols))
            numberrandom = str(kenny.choice(sysnumber))
            letterrandom = kenny.choice(letters)
            capitalLetterRandom = kenny.choice(letters).upper()
            password = [symbolrandom, numberrandom, letterrandom, capitalLetterRandom]
            choose()
elif symbols == "No" and numbers == "Yes" and case == "Yes":
        numberrandom = str(kenny.choice(sysnumber))
        letterrandom = kenny.choice(letters)
        capitalLetterRandom = kenny.choice(letters).upper()
        password = [numberrandom, letterrandom, capitalLetterRandom]
        x = 0
        for y in password:
            print(y, end="")
            x += 1
        if x != length:
            numberrandom = str(kenny.choice(sysnumber))
            letterrandom = kenny.choice(letters)
            capitalLetterRandom = kenny.choice(letters).upper()
            password = [numberrandom, letterrandom, capitalLetterRandom]
            new = length - x
            new = range(new)
            for m in new:
                numberrandom = str(kenny.choice(sysnumber))
                letterrandom = kenny.choice(letters)
                capitalLetterRandom = kenny.choice(letters).upper()
                password = [numberrandom, letterrandom, capitalLetterRandom]
                choose() 

elif symbols == "Yes" and numbers == "No" and case == "Yes":
        symbolrandom =str(kenny.choice(sysymbols))
        letterrandom = kenny.choice(letters)
        capitalLetterRandom = kenny.choice(letters).upper()
        password = [symbolrandom, letterrandom, capitalLetterRandom]
        x = 0
        for y in password:
            print(y, end="")
            x += 1
        if x != length:
            symbolrandom =str(kenny.choice(sysymbols))
            letterrandom = kenny.choice(letters)
            capitalLetterRandom = kenny.choice(letters).upper()
            password = [symbolrandom, letterrandom, capitalLetterRandom]
            new = length - x
            new = range(new)
            for m in new:
                symbolrandom =str(kenny.choice(sysymbols))
                letterrandom = kenny.choice(letters)
                capitalLetterRandom = kenny.choice(letters).upper()
                password = [symbolrandom, letterrandom, capitalLetterRandom]
                choose() 

elif symbols == "Yes" and numbers == "Yes" and case == "No":
    symbolrandom =str(kenny.choice(sysymbols))
    numberrandom = str(kenny.choice(sysnumber))
    letterrandom = kenny.choice(letters)
    password = [symbolrandom, numberrandom, letterrandom]
    x = 0
    for y in password:
        print(y, end="")
        x += 1
    if x != length:
        symbolrandom =str(kenny.choice(sysymbols))
        numberrandom = str(kenny.choice(sysnumber))
        letterrandom = kenny.choice(letters)
        password = [symbolrandom, numberrandom, letterrandom]
        new = length - x
        new = range(new)
        for m in new:
            symbolrandom =str(kenny.choice(sysymbols))
            numberrandom = str(kenny.choice(sysnumber))
            letterrandom = kenny.choice(letters)
            password = [symbolrandom, numberrandom, letterrandom]
            choose()

elif symbols == "Yes" and numbers == "No" and case == "No":
    symbolrandom =str(kenny.choice(sysymbols))
    letterrandom = kenny.choice(letters)
    password = [symbolrandom, letterrandom]
    x = 0
    for y in password:
        print(y, end="")
        x += 1
    if x != length:
        symbolrandom =str(kenny.choice(sysymbols))
        letterrandom = kenny.choice(letters)
        password = [symbolrandom, letterrandom]
        new = length - x
        new = range(new)
        for m in new:
            symbolrandom =str(kenny.choice(sysymbols))
            letterrandom = kenny.choice(letters)
            password = [symbolrandom, letterrandom]
            choose()

elif symbols == "No" and numbers == "Yes" and case == "No":
    numberrandom = str(kenny.choice(sysnumber))
    letterrandom = kenny.choice(letters)
    password = [numberrandom, letterrandom]
    x = 0
    for y in password:
        print(y, end="")
        x += 1
    if x != length:
        numberrandom = str(kenny.choice(sysnumber))
        letterrandom = kenny.choice(letters)
        password = [numberrandom, letterrandom]
        new = length - x
        new = range(new)
        for m in new:
            numberrandom = str(kenny.choice(sysnumber))
            letterrandom = kenny.choice(letters)
            password = [numberrandom, letterrandom]
            choose()

elif symbols == "No" and numbers == "No" and case == "Yes":
    letterrandom = kenny.choice(letters)
    capitalLetterRandom = kenny.choice(letters).upper()
    password = [capitalLetterRandom,letterrandom]
    x = 0
    for y in password:
        print(y, end="")
        x += 1
    if x != length:
        letterrandom = kenny.choice(letters)
        capitalLetterRandom = kenny.choice(letters).upper()
        password = [capitalLetterRandom,letterrandom]
        new = length - x
        new = range(new)
        for m in new:
            letterrandom = kenny.choice(letters)
            capitalLetterRandom = kenny.choice(letters).upper()
            password = [capitalLetterRandom,letterrandom]
            choose()

elif symbols == "No" and numbers == "No" and case == "No":
    letterrandom = kenny.choice(letters)
    password = [letterrandom]
    x = 0
    for y in password:
        print(y, end="")
        x += 1
    if x != length:
        letterrandom = kenny.choice(letters)
        password = [letterrandom]
        new = length - x
        new = range(new)
        for m in new:
            letterrandom = kenny.choice(letters)
            password = [letterrandom]
            choose()
a = x + len(new)
print(a)
if a <= 5:
    print("\nDear User, This is a weak Password")
elif a > 5 and a <= 10:
    print("\nDear User, This is a fairly strong Password")
elif a >= 11:
    print("\nDear User, This is a very strong Password ")



print("")
print("Project 5 completed🎇🎇🎇✨")
print("")






