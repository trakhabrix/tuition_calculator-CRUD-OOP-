import CRUD

def tui_calc_menu():
    while True:
        print ("""====== Expense Tracker ======
    1 - Add Student Record
    2 - View All Student Records
    3 - View student details
    4 - Update Student 
    5 - Delete Student Record
    6 - Exit""")
        #Input
        choice_menu = (input("Enter your choice (1-6): ")).strip()
        #If (for whitespace / empty / letters)
        if choice_menu == "" or not choice_menu.isdigit():
            print("Please Input Only Valid Number.")
            continue
        choice_menu = int(choice_menu)
        #If-Else (for choice)
        if choice_menu == 1:
            CRUD.add_student()
        elif choice_menu == 2:
            CRUD.view_all()
        elif choice_menu == 3:
            CRUD.view_details()
        elif choice_menu == 4:
            password = "12345admin"
            admin_perm = int(input("Are you the admin (Yes[1]/NO[2])?"))
            if admin_perm == 1:
                pass_input = (input("Enter Your Password: "))
                if pass_input == password:
                    CRUD.update_student()
                else:
                    ("Wrong Password")
                    tui_calc_menu
            elif admin_perm == 2:
                print ("This is only for admin.")
                tui_calc_menu
            else: 
                print ('Invalid Choice')
        elif choice_menu == 5:
            CRUD.delete_student()
        elif choice_menu == 6:
            print ('Exiting...\nThanks for Using!!')
            break
        else:
            print ('Invalid Choice')
            
tui_calc_menu()