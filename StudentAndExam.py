students=[] # dictionary
exercise={} # to save all data about student

while True:
    print('Welcome in Student and exam Portal')
    print('Please Choose one from the menu')
    print('1) Add Student')
    print('2)Add Exercise grading')
    print('3)View Exercise')
    print('4)view Student')
    print('0)Exit')

    choosen =int(input()) #user choose number as String and we use int to change it to Integer

    if(choosen==1):
        print('please Enter Student first name:')
        firstName=input()
        print('please Enter Student Last Name: ')
        lastName=input()
        print('Enter Student martikel number: ')
        martikelNumber=input()

        students={"firstName":firstName,"lastName":lastName,"martikelNumber":martikelNumber}
        

    elif(choosen==2):
        print('Please add the exercise identification number')
        idNumber=int(input())
        points={} # to save the points of every exam 
        for student in students:
            print('please add the number of points for each student for that exercise')
            mark=int(input())
            mark = input(f"Enter points for {student['first_name']} {student['last_name']}: ")
            points[student['martikel']] = mark

            exercise[idNumber]=points

    elif(choosen==3):
        if not exercise:
            print('Not exercise')
        else:
            for idNumber,points in exercise.items():
                print(f'Exercise {idNumber}')
                for martikelNumber,score in points.items():
                    name=next((f'{student["firstName"]}{student["lastName"]}'
                               for student in students
                                 if student['martikelNumber']== martikelNumber),
                                    'unkown')
                    print(f'{name}({martikelNumber}): {score} points')
    elif(choosen==4):
        if not students:
            print('Unkown Student')
        else:
            for student in students:
                print(f"{student['firstName']} {student['lastName']} (martikelNumber: {student['martikelNumber']})")
    elif(choosen==0):
        print('Good Bye :)')
        break

    else:
        print('Wrong User input,try again')