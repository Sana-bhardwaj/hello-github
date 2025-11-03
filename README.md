# hello-github
My first GitHub repository — experimenting with code, version control, and basic projects.

🏫 Hostel Room Allocation System (CLI Version)

📌 Overview
The Hostel Room Allocation System is a menu-driven Command Line Interface (CLI) application built in Python to manage hostel room assignments for students efficiently — without the use of databases.
All data is handled in-memory using Python’s built-in data structures like dictionaries, lists, sets, and tuples.

This project was created as part of my college coursework to demonstrate my understanding of data structures, logic building, and CRUD-based application design.

💡 Features

✅ Admin Authentication — Secure access with password protection
✅ Add / Modify / Delete Students — Manage student details dynamically
✅ Automatic Room Tracking — Keeps track of occupancy, vacancies, and capacity
✅ Search Functionality — Quickly find students by name or ID
✅ Reports Section

Occupancy summary

Student list report

Room availability overview
✅ Fully In-Memory — No database required, simple and lightweight
✅ User-Friendly CLI Menu — Clear options, smooth navigation, and validations

🧠 Project Highlights

Language Used: Python

Paradigm: Procedural programming

Focus Areas: Fileless data management, data validation, and interactive CLI

Complexity Level: Beginner–Intermediate

Time Spent: ~2–3 hours of coding and testing

⚙️ Tech Stack
Component	Technology
Language	Python 3.x
Interface	Command Line (CLI)
Data Handling	Dictionaries, Sets, Lists
Storage	In-Memory (no external DB)
🧩 Folder Structure
📦 Hostel-Room-Allocation-CLI
 ┣ 📜 hostel_allocation.py      # Main Python source file
 ┣ 📜 README.md                 # Project documentation
 ┗ 📜 LICENSE (optional)        # Add if you choose a license

🚀 How to Run

Clone this repository

git clone https://github.com/<your-username>/Hostel-Room-Allocation-CLI.git


Navigate to the folder

cd Hostel-Room-Allocation-CLI


Run the program

python hostel_allocation.py


Login using the admin password
Enter admin password: admin123

🧭 Menu Options
Option	Description
1	Add New Student
2	Modify Student Details
3	Delete Student Record
4	Search Student by ID or Name
5	Generate Reports
6	Exit the Application
📊 Sample Output
===== Hostel Room Allocation Menu =====
1. Add Student
2. Modify Student
3. Delete Student
4. Search Student
5. Reports
6. Exit
Enter your choice: 1

--- Add New Student ---
Student ID: S101
Name: Riya Sharma
Course: BTech CSE
Year/Semester: 2nd Year
Contact: 9876543210
Available Rooms:
Room 101: Capacity 2, Occupied 1, Free 1
Room 102: Capacity 1, Occupied 0, Free 1
Enter room number: 101
Student Riya Sharma added successfully!

🛠️ Future Improvements

💾 Add JSON file storage to persist data between runs

🧍 Add gender-based room filtering

🏢 Add hostel block and floor-level grouping

📈 Add summary dashboard using simple terminal charts

📚 Learning Outcomes

Implemented CRUD operations using Python data structures

Strengthened understanding of loops, conditionals, and input validation

Designed a modular and menu-driven CLI system

Practiced error handling and logical structuring in Python

Author 👩🏻‍💼

Sana Bhardwaj
🎓 B.Tech (Computer Science & Data Science)
📍 Passionate about Python, UI/UX, and building simple yet effective software systems.

🪪 License

This project is open-source 

Feel free to use, modify, or enhance it for learning purposes.

🌟 If you like this project

Give it a ⭐ on GitHub to show your support and inspire future improvements!
