#Storage
student_info = []
student_id = 0
# Add Section
def add_student():
    global student_id
    global student_info
    student_id += 1
    print (f"{29 * "="}")
    name_student = input("Enter Name: ")
    subjects_count = int(input('Number of Subjects: '))
    #Store the subjects/cost
    subjects = []
    # Loop for subjects
    for i in range(subjects_count):
        subject_name = input(f'Enter Subject {i+1}: ')
        subjects.append(subject_name)
    #Discount
    print("""Choose type of education:
    1 - Tertiary (3% discount)
    2 - Elem to Highschool (10% discount)""")
    choice_educ = int(input('Enter your choice (1 or 2): '))
    #If-Else Discount
    if choice_educ == 1:
        discount_rate = 0.03
    elif choice_educ == 2:
        discount_rate = 0.10
    else:
        print('Invalid Choice')
    #Total Computation
    total_cost = subjects_count * 2000.0
    #Discount Computation
    discount = total_cost * discount_rate
    final_total = total_cost - discount
    #Store the Student the info
    student_info.append({
        "ID": student_id,
        "STUDENT": name_student,
        "SUBJECT": subjects,
        "DISCOUNT": discount_rate,
        "TOTAL": final_total
    })
    print (f"Student {name_student} added with an ID {student_id}. Total Fee: {final_total} ")
    print (f"{29 * "="}")
# View all section
def view_all():
    #To check if the storage have data
    if not student_info:
        print("\nNot Yet Record")
        return
    print (f"{29 * "="}")
    for students in student_info:
        print(f"{students['ID']}[ID] {students['STUDENT']} - ₱{students['TOTAL']}")
    print (f"{29 * "="}")
# View student details
def view_details():
    #To check if the storage have data
    if not student_info:
        print("\nNot Yet Record")
        return
    print (f"{29 * "="}")
    for students in student_info:
        print(f"{students['ID']}[ID] {students['STUDENT']}")
    id_choose = int(input("Enter ID to view details: "))
    # To align the info of student
    for students in student_info:
        if students["ID"] == id_choose:
            # To format the subjects
            subjects_formatted = ", ".join(students["SUBJECT"])
            print (f"""==== Student Record ====
ID: {students["ID"]}
Name: {students["STUDENT"]}
Subjects: {subjects_formatted}
Discount: {students["DISCOUNT"] * 100}%
Total: ₱{students["TOTAL"]}
{f"{29 * "="}"}""")
# Update students
def update_student():
    #To check if the storage have data
    view_all()
    if not student_info:
        print("No records found.")
        return
    choose_upd = int(input("Enter ID to update: "))
    # Update Part
    for students in student_info:
        if students["ID"] == choose_upd:
            print ("==== Update Student ====")
            # Update Name
            new_name = input("Enter new name (leave blank to keep): ")
            if new_name:
                students["STUDENT"] = new_name
            # Update Subjects
            choice = input("Update subjects?(y/n)").lower()
            if choice == "y":
                subjects_count = int(input('Number of Subjects: '))
                #Store the subjects/cost
                subjects = []
                # Loop for subjects (note :NEED TO FIX LATER)
                for i in range(subjects_count):
                    subject_name = input(f'Enter Subject {i+1}: ')
                    subjects.append(subject_name)
                print("""Choose type of education:
1 - Tertiary (3%)
2 - Elem to Highschool (10%)
""")
                new_discount = int(input("Choose new discount type: "))
                #If-Else Discount
                if new_discount == 1:
                    students["DISCOUNT"] = 0.03
                elif new_discount == 2:
                    students["DISCOUNT"] = 0.10
                else:
                    print('Invalid Choice')
                # Recompute Total Fee
                total_cost = subjects_count * 2000.0
                discount = total_cost * students["DISCOUNT"]
                final_total = total_cost - discount
                # Update Total
                students["TOTAL"] = final_total
                print (f"Student {new_name} updated with an ID {student_id}. Total Fee: {final_total} ")
    print (f"{29 * "="}")
# Delete students
def delete_student():
    view_all()
    #To check if the storage have data
    if not student_info:
        print("No records found.")
        return
    
    choose_dlt = int(input("Enter ID to delete: "))
    for students in student_info:
        if students["ID"] == choose_dlt:
            print(f"Student '{students['STUDENT']}' Deleted Successfully!\n{29 * '='}")
            student_info.remove(students)
            return