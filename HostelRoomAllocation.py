"""
Hostel Room Allocation - CLI Version

This is a menu-driven command line interface for managing hostel room allocations.
All data is stored in memory using Python data structures (dictionaries, lists, sets, tuples).

Name   = Sana
Course = BTech Cs Ds
"""


#---------------------------------- Password condition -------------------------------------------
ADMIN_PASSWORD = "admin123"
MAX_LOGIN_ATTEMPTS = 3


#---------------------------------- In Memory Data ------------------------------------------
students = {}
rooms = {
    101: (101,2),
    102: (102,1),
    103: (103,3),
    104: (104,2),
    105: (105,1)
}
room_occupants = {room: set() for room in rooms}


#------------------------------------ Helper Function -----------------------------------------
def pause():
    input("\nPress Enter to continue...")
pass

def authenticate():
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        pwd = input("Enter admin password: ")
        if pwd == ADMIN_PASSWORD:
            print("\nLogin successful. Welcome, Administrator!\n")
            return True
        else:
            attempts += 1
            print(f"Incorrect password. Attempts left: {MAX_LOGIN_ATTEMPTS - attempts}")
    print("Maximum login attempts exceeded. Exiting.")
    return False

def get_int(prompt):
    while True:
        val = input(prompt).strip()
        if val.isdigit():
            return int(val)
        print("Please enter a valid number.")


#--------------------------------- CRUD Operations --------------------------------------
def add_student():
    print("\n--- Add New Student ---")
    sid = input("Student ID: ").strip()
    if sid in students:
        print("Student ID already exits!")
        return

    name = input("Name: ").strip()
    course = input("Course: ").strip()
    year = input("Year/Semester: ").strip()
    contact = input("Contact number: ").strip()

    print("\nAvailable Rooms:")
    for r, (num,cap) in rooms.items():
        occ = len(room_occupants[r])
        print(f"Room {r}: Capacity {cap}, Occupied {occ}, Free {cap - occ}")

    room = get_int("Enter room number: ")
    if room not in rooms:
        print("Invalid room number!")
        return

    if len(room_occupants[room]) >= rooms[room][1]:
        print("Room full!")
        return

    room_occupants[room].add(sid)
    students[sid] = {
        "name": name,
        "course": course,
        "year": year,
        "contact": contact,
        "room": room
    }
    print(f"Student {name} added successfully!")

def modify_student():
    print("\n--- Modify Student ---")
    sid = input("Enter Student ID: ").strip()
    if sid not in students:
        print("Student not found!")
        return

    stu = students[sid]
    print(f"Current details: {stu}")

    name = input(f"Name [{stu['name']}]: ").strip() or stu['name']
    year = input(f"Year [{stu['year']}]: ").strip() or stu['year']
    course = input(f"Course [{stu['course']}]: ").strip() or stu['course']
    contact = input(f"Contact [{stu['contact']}]: ").strip() or stu['contact']

    change_room = input("Change room (y/n): ").strip().lower()
    new_room = stu['room']
    if change_room == 'y':
        print("\nAvailable Rooms:")
        for r, (num,cap) in rooms.items():
            occ = len(room_occupants[r])
            print(f"Room {r}: Capacity {cap}, Occupied {occ}, Free {cap - occ}")
        room_num = get_int("Enter new room number: ")
        if room_num in rooms and len(room_occupants[room_num]) < rooms[room_num][1]:
            room_occupants[stu['room']].discard(sid)
            room_occupants[room_num].add(sid)
            new_room = room_num
            print(f"Room changed to {room_num}.")
        else:
            print("Invalid or full room!")

    students[sid] = {
        "name": name,
        "course": course,
        "year": year,
        "contact": contact,
        "room": new_room
    }
    print("Students details updated successfully!")

def delete_student():
    print("\n--- Delete Student ---")
    sid = input("Enter student ID: ").strip()
    if id not in students:
        print("Student not found!")
        return

    room = students[sid]['room']
    room_occupants[room].discard(sid)
    del students[sid]
    print("Student deleted successfully!")

def search_student():
    print("\n--- Search Student ---")
    query = input("Enter student ID or name: ").strip()
    found = False
    for sid, details in students.items():
        if query.lower() in sid.lower() or query.lower() in details['name'].lower():
            print(f"\nStudent ID: {sid}")
            for k, v in details.items():
                print(f" {k}: {v}")
            found = True
    if not found:
        print("No matching student found.")


#---------------------------------- Reports ----------------------------------------------
def occupancy_report():
    print("\n--- Occupancy Report ---")
    total_rooms = len(rooms)
    total_capacity = sum(cap for (_, cap) in rooms.values())
    occupied_beds = sum(len(occ) for occ in room_occupants.values())
    print(f"Total rooms: {total_rooms}")
    print(f"Total capacity: {total_capacity}")
    print(f"Occupied beds: {occupied_beds}")
    print(f"Vacant beds: {total_capacity - occupied_beds}")

def student_list_report():
    print("\n--- Student List ---")
    if not students:
        print("No records found!")
        return
    for sid, data in students.items():
        print(f"\nStudent ID: {sid}")
        for k, v in data.items():
            print(f"  {k}: {v}")


def room_availability_report():
    print("\n--- Room Availability ---")
    for r, (num, cap) in rooms.items():
        occ = len(room_occupants[r])
        print(f"Room {r}: Capacity {cap}, Occupied {occ}, Free {cap - occ}")


def view_reports():
    while True:
        print("\nReports Menu:")
        print("1. Occupancy Report")
        print("2. Student List")
        print("3. Room Availability")
        print("4. Back")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            occupancy_report(); pause()
        elif choice == '2':
            student_list_report(); pause()
        elif choice == '3':
            room_availability_report(); pause()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")


#----------------------------------- Main Menu -------------------------------------
def main_menu():
    while True:
        print("\n===== Hostel Room Allocation Menu =====")
        print("1. Add Student")
        print("2. Modify Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Reports")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_student(); pause()
        elif choice == '2':
            modify_student(); pause()
        elif choice == '3':
            delete_student(); pause()
        elif choice == '4':
            search_student(); pause()
        elif choice == '5':
            view_reports()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")


#------------------------------ Entry Point --------------------------------------
print("Hostel Room Allocation System - CLI (No Database)")
if authenticate():
    main_menu()
