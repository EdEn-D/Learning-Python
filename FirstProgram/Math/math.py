import random
import os
import time

def cls():  #cls function
    os.system('cls' if os.name=='nt' else 'clear')

Mode = input('1. Multiplication\n2. Division\n3. Exponents \n\nChoose program: ') #initial menu
progs = {'1':'Multiplication','2' :'Division','3':'Exponents'}         #dic with the options

def title():
    print(Mode + '. ' + progs[str(Mode)])   # displays title

def limits():
    In2 = input('From: ')   #input from
    In3 = input('To: ')     #input to
    return In2, In3

def multiplication(In2, In3):

    num1 = random.randint(int(In2), int(In3))   #randomize 1st number
    num2 = random.randint(int(In2), int(In3))   #randomize 2nd number
    ans = num1 * num2   #the product
    print(str(num1) + ' x ' + str(num2) + " = ")
    while True:
        question = input() #ask answer
        if int(question) == int(ans):#compare answers
          print("Correct!")
          time.sleep(0.5)
          break
        else:
            print("Wrong, try again")

def exponents2(In2, In3): #rand base, rand exp
    base = random.randint(int(In2), int(In3))   #randomize 1st base
    dicExpMax = {'2': 12, '3':7, '4':6,'5':4,'6':4,'7':4,'8':4,'9':4,'11':3}   #dictionary that defines the max exponent value for each base
    ExpMax = dicExpMax[str(base)] # the max exponent of the randomized base
    Exp = random.randint(2,ExpMax)

    #print (str(base), ' ^ ', str(ExpMax))
    input()


def exponents(In2, In3): # choose a base, limit rand exponents
    exp1 = random.randint(int(In2), int(In3))  # randomize 1st base
    dicExp = {'2': 12, '3': 7}  # dictionary that defines the max exponent value for each base
    input()

cls()
if Mode is '1':
    title()
    lim1, lim2 = limits()   #define limits
    while True:
        cls()
        title()
        multiplication(lim1, lim2)
elif Mode is '3':
    title()
    print("Enter base then max exponent value")
    elim1, elim2 = limits()   #define limits
    while True:
        cls()
        title()
        exponents2(elim1, elim2)


x = input()