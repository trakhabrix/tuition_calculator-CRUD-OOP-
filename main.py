import crud

def tui_calc_menu():
    call = crud.system()
    while True:
        print ("""====== Expense Tracker ======
    1 - Add Student Record
    2 - View All Student Records
    3 - View student details
    4 - Update Student 
    5 - Delete Student Record
    6 - Exit
=============================""")
        #Input
        choice_menu = (input("Enter your choice (1-6): ")).strip()
        #If (for whitespace / empty / letters)
        if choice_menu == "" or not choice_menu.isdigit():
            print("Please Input Only Valid Number.")
            continue
        choice_menu = int(choice_menu)
        #If-Else (for choice)
        if choice_menu == 1:
            call.add_student()
        elif choice_menu == 2:
            call.view_all()
        elif choice_menu == 3:
            call.view_details()
        elif choice_menu == 4:
            call.update_student()
        elif choice_menu == 5:
            call.delete_student()
        elif choice_menu == 6:
            print ('Exiting...\nThanks for Using!!')
            break
        else:
            print ('Invalid Choice')
            
tui_calc_menu()