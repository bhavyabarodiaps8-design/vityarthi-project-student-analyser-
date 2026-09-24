# vityarthi-project-student-analyser-
project about analysis of multiple students grades
PROJECT TITLE:
Student Result Management System

OVERVIEW OF THE PROJECT:
The Student Result Management System is a lightweight, menu-driven Python application designed to streamline academic mark management. Built using Object-Oriented Programming (OOP) principles, it allows educators to store student records, calculate total marks and percentages across 1st-semester subjects, and assign grades with feedback without manual calculation errors.

FEATURES:
- Roll Number Validation: Enforces unique roll numbers to prevent duplicate entries.
- Input Range Checking: Verifies that entered marks fall within valid limits (0 to 100).
- Automatic Grade Calculation: Evaluates student percentage and assigns letter grades (S, A, B, C, D, F) alongside performance feedback.
- Individual Result Cards: Generates a clear subject-by-subject result sheet for a specific student.
- Batch Summary Report: Displays a list of all enrolled students with their percentages and grades.

TECHNOLOGIES/TOOLS USED:
- Programming Language: Python 3
- Paradigms: Object-Oriented Programming (Classes & Objects), Data Structures (Dictionaries & Lists)
- Environment: Any terminal or IDE supporting Python (VS Code, PyCharm, or Command Prompt)

STEPS TO INSTALL & RUN THE PROJECT:
1. Ensure Python 3.x is installed on your computer.
2. Download or save the Python script file as `main.py` in your working directory.
3. Open your terminal or command prompt and navigate to the project directory:
   cd path/to/your/folder
4. Run the program with the following command:
   python main.py

INSTRUCTIONS FOR TESTING:
1. Test Option 1 (Add Student):
   - Select option 1.
   - Enter a Roll Number (e.g., 101) and Name (e.g., John Doe).
   - Enter marks for all 4 subjects (e.g., 85, 90, 75, 88).
   - Test invalid inputs like -5, 105, or letters to confirm error handling works.
2. Test Option 2 (View Single Result):
   - Select option 2.
   - Enter Roll Number 101 to verify the calculated total, percentage, and grade.
   - Try entering an unregistered Roll Number (e.g., 999) to verify the missing record message.
3. Test Option 3 (View All Students Summary):
   - Add a second student using Option 1.
   - Select option 3 to print the full list summary.
4. Test Option 4 (Exit):
   - Select option 4 to terminate the execution cleanly.

SCREENSHOTS:

 
