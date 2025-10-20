students=[] # list to save all data about student
exercise={} # dictionary, where the exercises and points will be stored

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
student_exists= False
        for student in students:
            if student['martikelNumber']== martikelNumber:
                student_exists=True
                break
        if student_exists:
            print(f'Error: Student with martikel number {martikelNumber} already existiert!')
            continue
        else:
            student={"firstName":firstName,"lastName":lastName,"martikelNumber":martikelNumber} #making temporary variable and add it then in dictionary

        students.append(student) # to make more than dictionary in students
        

    elif(choosen==2):
        print('Please add the exercise identification number')
        idNumber=int(input())
        points={} # to save the points of every exam 
        for student in students:
            print('please add the number of points for each student for that exercise')
            mark=int(input())
            mark = input(f"Enter points for {student['first name']} {student['last name']}: ")
            points[student['martikelNumber']] = mark

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
                                 if student['martikelNumber']== martikelNumber), 'unknown')
                    print(f'{name}({martikelNumber}): {score} points')
    elif(choosen==4):
        if not students:
            print('Unkown Student')
        else:
            for student in students:
                fname = student["firstName"]
                lname = student["lastName"]
                mid = student["martikelNumber"]
                print(f"{fname} {lname} (martikelNumber: {mid})")

    elif(choosen==0):
        print('Good Bye :)')
        break

    else:
        print('Wrong User input,try again')
