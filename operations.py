from teacher import Teacher

def display_teacher(teacher):
    print("ID: ", teacher.id)
    print("Name: ", teacher.full_name)
    print("Age: ", teacher.age)
    print("DOB: ", teacher.dob)
    print("No Of Classes: ", teacher.no_of_classes)
    print()

def show_all_teacher(teacherlist):
    print("Displaying all teacher details")
    for teacher in teacherlist:
        display_teacher(teacher)

def add_a_teacher(teacherlist):
    id = len(teacherlist) + 1
    print("enter the teacher full name")
    fullname=str(input())
    print("enter the age")
    age=int(input())
    print("enter the dob")
    dob=str(input())
    print("enter the no of classes")
    noc=int(input())
    
    teacher=Teacher(id,fullname,age,dob,noc)
    teacherlist.append(teacher)

def filter_teachers_based_on_criteria(teacherlist):
    print("1)filter by age")
    print("2)filter by no of cls")
    choice=int(input())

    if choice == 1:
        print("Enter the age")
        age=int(input())
    else:
        print("Enter the no of classes")
        no_of_classes = int(input())
    
    for teacher in teacherlist:
        if choice == 1 and teacher.age == age:
            display_teacher(teacher)
        elif choice == 2 and teacher.no_of_classes == no_of_classes:
            display_teacher(teacher)

def search_for_a_teacher(teacherlist):
    print("enter the full_name")
    full_name=str(input())

    for teacher in teacherlist:
        if full_name in teacher.full_name:
            display_teacher(teacher)

def update_a_teachers_record(teacherlist):
    print("enter the id")
    id=int(input())
    print("enter the teacher full name")
    fullname=str(input())
    print("enter the age")
    age=int(input())
    print("enter the dob")
    dob=str(input())
    print("enter the no of classes")
    noc=int(input())

    for teacher in teacherlist:
        if teacher.id == id:
            teacher.full_name = fullname
            teacher.age = age
            teacher.dob = dob
            teacher.no_of_classes = noc   

def delete_a_teacher(teacherlist):
    print("enter the id")
    id=int(input())

    for teacher in teacherlist:
        if teacher.id == id:
            teacherlist.remove(teacher) 
