# TODO: Question One

# month = int(input('Enter the month:'))
# match month:
#         case month if month in (1,3,5,7,8,10,12):
#                 print('33 days')
#         case month if month in (4,6,9,11):
#                 print("30 days")
#         case month if month == 2:
#                 print('28 or 29 Days')
#         case _:
#                 print('Month number is invalid')
                

# # Question Two
# name = input('Enter the operation You want to perform:')
# match name:
#   case "addition":
#     print('Please input Two Numbers to perform Addition')
#     numberone = int(input('Enter the numberOne:'))
#     numbertwo = int(input('Enter the numberTwo:'))
#     sum = numberone+numbertwo
#     print(sum)
#   case "substraction":
#     print('Please input Two Numbers to perform Substraction')
#     numberone = int(input('Enter the numberOne:'))
#     numbertwo = int(input('Enter the numberTwo:'))
#     sub = numberone-numbertwo
#     print(sub)
#   case "multplication":
#     print('Please Two input Numbers to perform Multplication')
#     numberone = int(input('Enter the numberOne:'))
#     numbertwo = int(input('Enter the numberTwo:'))
#     mul = numberone*numbertwo
#     print(mul)
#   case "division":
#     print('Please Two input Numbers to perform Divison')
#     numberone = int(input('Enter the numberOne:'))
#     numbertwo = int(input('Enter the numberTwo:'))
#     div = numberone/numbertwo
#     divTwo = numberone//numbertwo
#     print(div)
#     print(divTwo)
  
#   case _:
#     print('Sorry We dont provide this operation right Now it will be added soon')


#TODO: Question Two

# name = input('Enter the operation you want to perform:')
# match name:
#     case name if name  == "addition":
#         numberone = int(input('Enter the numberOne:'))
#         numbertwo = int(input('Enter the numberTwo:'))
#         sum = numberone+numbertwo
#         print(sum)
#     case name if name  == "substraction":
#         print('You have Entered choice Two to perform Substraction')
#         numberone = int(input('Enter the numberOne:'))
#         numbertwo = int(input('Enter the numberTwo:'))
#         sub = numberone-numbertwo
#         print(sub)
#         print()
#     case name if name  == "multplication":
#         print('You have Entered choice Three to perform Multplication')
#         numberone = int(input('Enter the numberOne:'))
#         numbertwo = int(input('Enter the numberTwo:'))
#         mul = numberone*numbertwo
#         print(mul)
#         print()
#     case name if name == "division":
#         print('You have Entered choice Four to perform Divison')
#         numberone = int(input('Enter the numberOne:'))
#         numbertwo = int(input('Enter the numberTwo:'))
#         div = numberone/numbertwo
#         divTwo = numberone//numbertwo
#         print(div)
#         print(divTwo)
#         print()
#     case _:
#         print('Invalid Choice')

# TODO: Question Three
# print("1. To check Isosceles and Right angle Triangle:")
# print("2. To check Equilateral Triangle:")

# print('Enter Your Choice')
# choice = int(input())
# match choice:
#         case 1:
#                 print('You are going to perform for Isosceles Triangle And Right Angle Triangle')
#                 print('Enter Three Number:')
#                 a,b,c = int(input()), int(input()), int(input())
#                 if c**2 == (a+b)**2:
#                                 print('Its an right angle Triangle')
#                 else:
#                         if a == b or b ==c or c== a:
#                                 print('Its an Isosceles Triangle')
                        
                
#         case 2:
#                 print('You are going to perform for Right Equilateral Triangle')
#                 print('Enter three Number:')
#                 a,b,c = int(input()), int(input()),int(input())
#                 if a ==b == c:
#                         print('Its a Equilateral Triangle')
#                 else:
#                         print('Its not a Equilateral Triangle')
#         case _:
#                 exit()




#TODO: Question Four
# age = int(input('Enter the user age:'))

# match age:
#     case age if age<10:
#         print('He is a kid')
#     case age if age>10 and age<20:
#         print('He is teen')
#     case age if age>20 and age<40:
#         print('You are Young')
#     case age if age>40 and age<60:
#         print('Experienced')
#     case age if age >=60 and age<=80:
#         print("Senior Citizen")
    
#     case _:
        # print('Invalid age')
        
#TODO: Question Five

# number = int(input('Enter the number:'))

# match number:
#     case number if number % 2 == 0:
#         print('Saurabh Shukla')
#     case number if number<0 and number %2 !=0:
#         print('Prateek Jain') 
#     case number if number >0 and number %2 !=0:
#         print('Aditya Choudhary')
    
#     case _:
#         print('Invalid number')

# TODO: Question Six

# word = eval(input('Enter the string:'))

# match word:
#     case word if " " in word:
#         print('Its a multiword sting')
#     case word if " " not in word:
#         print('Its a single word')
#     case _:
#         print('Invalid Input')

# TODO: Question 7
# number = int(input('Enter the number:'))

# match number:
#     case number if number >0:
#         print('Its a positive number')
#     case number if number<0:
#         print('Its a negtive number')
#     case number if number ==0:
#         print('Zero')
        

# TODO: Question Eight
# stringOne = input('Enter the string:')
# stringTwo = input('Enter the string:')

# match (stringOne, stringTwo):
#     case (stringOne,stringTwo) if stringOne == stringTwo:
#         print('The given string are identical')
        
#     case (stringOne,stringTwo) if stringOne>stringTwo:
#         print('{} comes after {}'.format(stringOne, stringTwo))
#     case (stringOne,stringTwo) if stringTwo>stringOne:
#         print('{} comes before {}'.format(stringOne, stringTwo))


# TODO: Question 9

# year = int(input('Enter the number:'))
# match year:
#         case year if year % 4 ==0 and year %100 !=0:
#                 print('Its a non century Leap Year')
#         case year if year % 400 == 0:
#                 print('Century Leap Year')
#         case year if year % 100 == 0:
#                 print('Century Non Leap Year')
#         case year if year % 100 !=0 and year % 4 !=0:
#                 print('Non Century Non Leap Year')
                
# Question 10: 

# color = input('Whats Your Favourite Color:')
# match color:
#         case color if "yellow" in color:
#                 print('Monday')
#         case color if "blue" in color:
#                 print('Tuesday')
#         case color if "orange" in color:
#                 print('Wednesday')
#         case color if "white" in color:
#                 print('Thrusday')
#         case color if "black" in color:
#                 print('Friday')
#         case color if "red" in color:
#                 print('Saturday')
#         case _:
                # print('Sunday')

# I neuron Solution

s1 = input('Whats Your Favourite Color:')
l1 = ['yellow','blue','orange','white','black','red']
for color in l1:
        if color in s1:
                c= color
                break
                
        else:
                c= "other"
                
match c:
        case "yellow":
                print(c,"-",'Monday')
        case "blue":
                print(c,"-",'Tuesday')
        case 'orange':
                print(c,"-",'Wednesday')
        case "white":
                print(c,"-",'Thrusday')
        case "black":
                print(c,"-",'Friday')
        case "red":
                print(c,"-",'Saturday')
        case "other":
                print(c,"-",'Sunday')