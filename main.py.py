# List of topics strictly extracted from the provided syllabus
SUBJECTS = [
    "Introduction to problem solving",
    "Effective Technical Communcation",
    "Environmental Sustainibility",
    "Calculus"]
    

class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def add_marks(self, subject, score):
        self.marks[subject] = score

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_percentage(self):
        if not self.marks:
            return 0.0
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "S,Well done, Keep it up.."
        elif percentage >= 80:
            return "A, Excellent you are at the right place.. "
        elif percentage >= 70:
            return "B, Good focus more on yourself.."
        elif percentage >= 60:
            return "C,Fine, Work hard..."
        elif percentage >= 50:
            return "D,Not fine, better luck next time "
        else:
            return "F,Focus on studies...."


class ResultManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        roll_no = input("Enter Roll Number: ").strip()
        if roll_no in self.students:
            print("Student with this roll number already exists!")
            return

        name = input("Enter Student Name: ").strip()
        student = Student(roll_no, name)

        print("\nEnter marks out of 100 for each module:")
        for subject in SUBJECTS:
            while True:
                try:
                    score = float(input(f"  {subject}: "))
                    if 0 <= score <= 100:
                        student.add_marks(subject, score)
                        break
                    print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        self.students[roll_no] = student
        print(f"\nStudent '{name}' added successfully!")

    def view_result(self):
        roll_no = input("Enter Roll Number to view result: ").strip()
        student = self.students.get(roll_no)

        if not student:
            print("No student found with that roll number.")
            return

        print("\n" + "=" * 65)
        print(f"RESULT CARD: {student.name.upper()} (Roll No: {student.roll_no})")
        print("=" * 65)
        print(f"{'Subject:'} | {'Score:'}")
        print("-" * 65)
        for subject, score in student.marks.items():
            print(f"subject:","score")
        print("-" * 65)
        print(f"Total Marks : {student.calculate_total()} / {len(SUBJECTS) * 100}")
        print(f"Percentage  : {student.calculate_percentage()}%")
        print(f"Grade       : {student.calculate_grade()}")
        print("=" * 65)

    def view_all_students(self):
        if not self.students:
            print("No records available.")
            return

        print("\n" + "-" * 75)
        print(f"{'Roll No:'} | {'Name:'} | {'Percentage:'} | {'Grade:'}")
        print("-" * 75)
        for s in self.students.values():
            print(f"{s.roll_no} | {s.name} | {s.calculate_percentage()}% | {s.calculate_grade()}")
        print("-" * 75)


def main():
    system = ResultManagementSystem()
    while True:
        print("\n--- Student Result Management System ---")
        print("1. Add Student & Enter Marks")
        print("2. Search & View Student Result")
        print("3. View All Students Summary")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()
        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.view_result()
        elif choice == "3":
            system.view_all_students()
        elif choice == "4":
            print("Exiting program..,have a great day")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()