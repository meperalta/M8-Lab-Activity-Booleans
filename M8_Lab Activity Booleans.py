#Maria Eden Peralta
#March 12, 2022


#Problem 1:
#Write a function that takes two inputs from a user and
#prints whether they are equal or not.

def Equals(a,b):
    
    if a==b:
        print("{} and {} are equal".format(a,b))
    else:
        print("{} and {} are not equal".format(a,b))

#test function

Equals(10,10)

Equals(10,5)

#Problem 2 – Write a function that takes two inputs from a user and
#prints whether the sum is greater than 10, less than 10, or equal to 10.

def SumGreater(x,y):
    if x+y==10:
        print("Sum is equal to 10")
    elif x+y>10:
        print("Sum is greater than 10")
    else:
        print("Sum is less than 10")

#test function

SumGreater(5,4)

SumGreater(12,3)

SumGreater(6,4)


#Problem 3 – Write a function that takes a list and
#prints if the value 5 is in that list.

def checkFunction(lst):
#Check if 5 is present in list or not
    if 5 in lst:
        print("Value 5 is present in that list.")
    else:
        print("Value 5 is not present in that list.")

checkFunction([1,2,3,4,5])
checkFunction([2,4,6,8,10,12])

#Problem 4 – Write a function that takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise.
#Consider the requirements of a leap year:
    # -	The year is evenly divisible by 4
    # -	If the year can be evenly divided by 100 it is NOT a leap year, unless:
    # o	If the year is also evenly divisible by 400, then it is a leap year.

def checkLeapYear(year):
    #Check if the year is evenly divisible by 4
    if (year % 4) == 0:
        #Check if the year is evenly divisible by 100
        if (year % 100) == 0:
            #Check if the year is evenly divisible by 400
            if (year % 400) == 0:
                #Print it is a leap year
                print("{0} is a leap year".format(year))
            #Else it is not a leap year
            else:
                print("{0} is not a leap year".format(year))
#if the year is not divisible by 100 then Leap year
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))


checkLeapYear(2021)
checkLeapYear(2000)

#Problem 5 - Write a function that checks whether your game character has picked up all the items needed to perform certain tasks and
#checks against any status debuffs. Confirm checks with print statements


class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname


    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
    
    def checks(self,p):
        print("Checks function")
        task = input("What task the character are going to perform(Write,climb,cook)")
        
        # For cooking a dish
        if task == "cook":
            if p.weaknesses == "small":
                print("The character can not cook")
                
            elif ('pan' in p.weapons) and ('groceries' in p.weapons):
                print("The character can cook")     
                
            else:
             print("The character will not Cook")
                
                
        # for climbing a mountain        
        elif task == "climb":
            if p.weaknesses != "slow":
                print("The character can not climb the mountain")
                
            elif ('rope' in p.weapons) and ('coat' in p.weapons) and ("first aid kit") in p.weapons:
                print("The character can climb")
                
            else:
                print("The character will not climb a mountain")
                
        # For writing a book
        elif task == "write":
            if p.weaknesses != "confusion":
                print("The character can not write a book")
                
            elif ('pen' in p.weapons) and ('paper' in p.weapons) and ("idea") in p.weapons:
                print("The character can a write a book")
                
            else:
                print("The character will not write a book")
           

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
    
player1.checks(player1)


