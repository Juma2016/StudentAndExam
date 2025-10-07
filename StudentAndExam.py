print('Welcome in Student and exam Port')
print('Please Choose one from the menu')
print('1) Add Student')
print('2)Add Exercise grading')
print('3)View Student')
print('4)Exercies')

choosen =int(input()) #user choose number as String and we use int to change it to Integer

if(choosen==1):
    print('please Enter your first name:')
    firstname=input()
    print('please insert your Last Name: ')
    lastName=input()
    print('Enter your martikel number: ')
    martikelNumber=input()
    
if(choosen==2):
    print('Please add the exercise identification number')
    idNumber=int(input())
    print('please add the number of points for each student for that exercise')

if(choosen==3):
    print('please insert the exercise number')
    exerciseNumber=int(input())
if(choosen==4):
    print('the data of Student......')
else:
    print('Wrong User input')