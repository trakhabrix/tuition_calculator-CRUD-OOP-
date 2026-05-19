class student_info:
    def __init__(self, student_name, subjects_count, subjects_list, discount):
        self.student_name = student_name
        self.subjects_count = subjects_count
        self.subjects_list = subjects_list
        self.discount = discount
        self.total_fee = self.compute_fee()

    def compute_fee(self):
        subject_cost = 2000.0
        total = self.subjects_count * subject_cost
        total -= total * self.discount
        
        return total
    
class system:
    def __init__(self):
        self.student_store = {}
        self.student_id = 0
    # Add Student
    def add_student(self):
        self.student_id += 1
        student_name = input("Enter Name: ")
        subjects_count = int(input('Number of Subjects: '))
        #Storage of the Subjects
        subjects_list = []
        #Loop for Subjects
        for i in range(subjects_count):
            subject = input(f'Enter Subject {i+1}: ')
            subjects_list.append(subject)

        print("""Choose type of education:
        1 - Tertiary (3% discount)
        2 - Elem to Highschool (10% discount)""")

        choice_disc = int(input('Enter your choice (1 or 2): '))
        # If-else discount
        if choice_disc == 1:
            discount = 0.03
        elif choice_disc == 2:
            discount = 0.10
        else:
            print("Invalid Choice")
        # Create student object
        student = student_info(student_name, subjects_count, subjects_list, discount)
        # Store student
        self.student_store[self.student_id] = student
        # Result
        print(f"\nStudent {student_name} added with ID {self.student_id} Total Fee: {student.total_fee}")
    # View all
    def view_all(self):
        # To check if the storage is empty
        if not self.student_store:
            print ("Not yet record")
            return
        # To show the list of the students
        print("====== Students Record =======")
        for student_id, student in self.student_store.items():
            print(f"[{student_id}] ID {student.student_name} - {student.total_fee}")
    
    # View Details
    def view_details(self):
        self.view_all()
        id_choose = int(input("Enter ID to view details: "))
        # To align the info of student
        for student_id,student in self.student_store.items():
            if id_choose == student_id:
                print (f"""==== Student Record ====
ID: {student_id}
Name: {student.student_name}
Subjects: {', '.join(student.subjects_list)}
Discount: {student.discount * 100}%
Total Fee:{student.total_fee}
                       """)
    # Update Student
    def update_student(self):
        self.view_all()
        id_choose = int(input("Enter ID to update: "))
        # Notes: need to fix (not saving the subject)
        for student_id, student in self.student_store.items():
            if id_choose == student_id:
                new_name = input("Enter new name (leave blank to keep): ")
                if new_name:
                    student.student_name = new_name
                change_subject = input("Update subjects?(y/n)").lower()
                subjects_count = int(input('Number of Subjects: '))
                #Storage of the Subjects
                subjects_list = []
                #Loop for Subjects
                for i in range(subjects_count):
                    subject = input(f'Enter Subject {i+1}: ')
                    subjects_list.append(subject)
                print("""Choose type of education:
1 - Tertiary (3%)
2 - Elem to Highschool (10%)
""")
                new_discount = int(input("Choose new discount type: "))
                if new_discount == 1:
                    student.discount = 0.03
                elif new_discount == 2:
                    student.discount = 0.10
                else:
                    print("Invalid choice, keeping old discount")

                # Recompute fee after update
                student.total_fee = student.compute_fee()
                # Result
                print("Student updated successfully!")
    # Delete Student
    def delete_student(self):
        self.view_all()
        id_choose = int(input("Enter ID to delete: "))

        for student_id, student in self.student_store.items():
            if id_choose == student_id:
                print(f"Student '{student.student_name}' Deleted Successfully!\n")
                del self.student_store[id_choose]
                return
            else:
                print("Student ID not found.")

call = system()
