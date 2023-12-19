import os
from operations import show_all_teacher, add_a_teacher, filter_teachers_based_on_criteria, search_for_a_teacher, update_a_teachers_record, delete_a_teacher

def main():
    teacherlist = []
    print("Landing/Home page")
    choice = 0
    while choice != 7:
        print("1) Show all teachers")
        print("2) Add a teacher")
        print("3) Filter teacher based on criteria")
        print("4) Search for a teacher")
        print("5) Update a teacher's record")
        print("6) Delete a teacher")

        try:
            choice = int(input())
            if choice == 1:
                show_all_teacher(teacherlist)
            elif choice == 2:
                add_a_teacher()
            elif choice == 3:
                filter_teachers_based_on_criteria()
            elif choice == 4:
                search_for_a_teacher()
            elif choice == 5:
                update_a_teachers_record()
            elif choice == 6:
                delete_a_teacher()

        except ValueError:
            print("enter correct input")
        os.system('cls')

if __name__=="__main__":
    main()
    
    


 