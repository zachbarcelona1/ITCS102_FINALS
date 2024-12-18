def Act_1():
    print(f"Hello World")
def Act_2():
    name = input ("Enter a name:")

    print ("Hi" + name )


def Act_3():
    name = input("Please input your name here ---> ")
    fname = input("Please input your fname here ---> ")
    mname = input("Please input your mname here ---> ")
    birthdate = input("Please input your birth date here ---> ")
    birthmonth = input("Please input your birthmonth here ---> ")
    birthyear = input("Please input your birthyear here ---> ")
    maritalstatus = input("Please input your maritalstatus here ---> ")
    religion = input("Please input your religion here ---> ")
    ethnicity = input("Please input your ethnicity here ---> ")
    mobile = input("Please input your mobile here ---> ")
    email = input("Please input your email here ---> ")
    gender = input("Please input your gender here ---> ")
    address = input("Please input your address here ---> ")
    age = input(" Please input your age here ---> ")


    print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")


def Act_4():
    number1 = eval(input("please type number--->"))
    number2 = eval(input("please type number--->"))

    answer	= number1 + number2
    print ("the sum of", number1, "and" , number2, "is" ,answer)


def Act_5():
    x = 5

    print (x)

    x = x + 10

    print (x)

    x = x + 15

    print(x)

    x += 10

    print(x)


def Act_6():
    Fah = eval(input("enter temperature in Fahrenheit : "))
    celsius = (Fah - 32) * 5 / 9

    print (" the comversion of" , Fah , "degrees fahrenheit is" , celsius , "degrees celsius")

    print (F" the comversion of {Fah} degrees fahrenheit is {round(celsius,2)} degrees celsius")

def Act_7():
    gold = 0

    miner = input("Enter Name")

    hasmine = input("Did you mine gold today ?")

    if hasmine.lower() == "yes":
        gold +=1
        print (f"Hi {miner}, today you have a total of {gold} gold ")
    else: 
        print (f"Hi {miner}, today you have a total of {gold} gold ")


def Act_8():
    password = input("please enter your password : ")

    if password.lower() == " mahal ko pa sya ":
        print (" congrats ang rupok mo")
        print ("enjoy using the system")
    elif password == "mahal ko pa sya":
        print (" congrats ang rupok mo")
        print ("enjoy using the system")


    else:
        print ("bawal ang marupok")
    print ("thank you for using the system")

    def Act_9():
    age = eval(input(" enter your age : "))
    if age>= 1 and age <= 7 :
        print ("toddler")
    elif age >= 8 and age <= 13:
        print (" pre teen")
    elif age >= 14 and age <= 18:
        print("Teenager")
    elif age <= 21:
        print("Early Adulthood")
    elif age <= 45:
        print("Mid Adulthood")
    elif age <= 59:
        print("Post Adult")
    elif age >= 60 and age <= 100:
        print("Senior")
    else:
        print("INVALID AGE")
def Act_10():
    isDLL= input('Are you a current student of DLL (yes/no):  ')

    if isDLL.lower() == 'yes':
        print('Welcome to the DLL BSIT Scholarship form')
        isCotta= input('Are you from Barangay Cotta (yes/ no):  ')

        if isCotta.lower() == 'yes':
            print('Please fillup the second form')
            isLevel=input('What is your current level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer')
            if isLevel.lower() == 'f':
                print('Hi Freshmen')
            elif isLevel.lower() == 's':
                print('Hi Sophomore')
            elif isLevel.lower() == 'j':
                print('Hi Junior')
            elif isLevel.lower() == 'r':
                print('Hi Senior')
            else:
                print('Invalid choice')
            isNeeded = input('Do you need this scholarship (yes/no):  ')
        
            if isNeeded.lower() == 'yes':
                print('Scholarship Granted')
            else:
                print('Thanks for stopping by')
        else:
            print('Sorry, this Scholarship grant are only for resident of Cotta')

    else:
        print('Thanks for stopping by')
def Act_11():
    for me in range (1 , 101):
        print(me, 'GOODBYE WORLD')
def Act_12():
    for cycle in range (10,0,-1):
        print(cycle)
def Act_13():
    sum = 1
    num=int(input('Enter a number: '))

    for x in range (num,0,-1):
        sum *= x
    print(f"The factorial of {num} is {sum}")


    def Act_14():
    for x in range ( 0, 11,):
        print(x,end =" ")
    for y in range (0, 11):
        print("*",end = " ")
    print("")
def Act_15():
    for x in range ( 0, 11,):
        print(x,end =" ")
    for y in range (0, x):
        print("*",end = " ")
    print("")
def Act_16():
    for x in range (1,11,):
        for y in range (1, x + 1):
            print(" ",end=" ")
        for z in range(11, x, -1):
            print(" * ",end=" ")
        print()
def Act_17():
    col = eval(input("Enter number of columns---> "))


    for x in range (1, 11):
        for y in range (1, col + 1):
            print(f"{x} x {y} = {x*y}" ,end="\t")
        print()
def Act_18():
    tri = eval(input("Enter a number of triangle---> "))

    for x in range (1, 6):
        for r in range (1 , tri + 1):
            for y in range (1 , x + 1):
                print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
        print()
def Act_19():
    tuloy = True
    while tuloy == True:
        name = input("Enter your name: ")
        if name.lower()== "stop":
            print("PROGRAM TERMINATED")
            break
            tuloy = False
        else:
            continue
def Act_20():
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        else:
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
            continue
def Act_21():
    def pang_hi():
        print("HI IT1C")

    def pang_hi_v2(name):
        print(f"Hello {name}")

    def termi():
        print("PROGRAM TERMINATED")

    def activity_2():
        number1 = eval (input("enter a number--->" ))
        number2 = eval (input("enter another number--->" ))
        answer = (number1 + number2)
        print(f"The sum of {number1} and {number2} is {answer}")

    tuloy =  True
    while tuloy == True:
        ask = input("Enter a name---> ")

        if ask.lower() != "stop":
            pang_hi_v2(ask)
            if ask == "2":
                activity_2()
                continue
        else:
            termi()
            break

        def Act_22():
    lup = True
    names = []


    while lup == True:
        askName = input("What name would you like to add?> ")
        if askName.lower() == "stop":
            print(names)
            print(f"You have entered {len(names)} names!")
            break
        else:
            names.append(askName)
def Act_23():
    def factorial(factor):
        """This function is for calculating the factorial of a numver that is provided, it will automatically compute the factorial of the provided number."""
        fact = 1
        for x in range(factor, 0, -1):
            fact *= x
            print(fact)
        return fact

    factorial(5)

    help(factorial)
def Act_24():
    # from actvity23 import factorial

    # print(f"the factorial of 7 is {factorial(7)} ")

    pass
def Act_25():
    fruits = ["apples", "banana", "orange"]

    fruits.append("strawberry")

    fruits.insert(1, "guyabano")

    fruitInsert = input("What fruit would you like to add?> ")

    fruits.append(fruitInsert)


