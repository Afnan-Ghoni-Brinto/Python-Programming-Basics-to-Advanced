"""Student manager using JSON for persistent local storage."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")

def load_students():
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
    except (OSError, json.JSONDecodeError):
        pass
    print("Could not load valid student data; using an empty list.")
    return []

def save_students(students):
    DATA_FILE.write_text(json.dumps(students, indent=2), encoding="utf-8")

def main():
    students = load_students()
    while True:
        print("\n1. Add  2. List  3. Search  4. Delete  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            student_id = input("Student ID: ").strip()
            if not student_id or any(s["id"] == student_id for s in students):
                print("ID must be nonempty and unique")
                continue
            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty")
                continue
            students.append({"id": student_id, "name": name})
            save_students(students)
            print("Student added")
        elif choice == "2":
            for student in students:
                print(student["id"], "-", student["name"])
            if not students: print("No students")
        elif choice == "3":
            student_id = input("Search ID: ").strip()
            matches = [s for s in students if s["id"] == student_id]
            print(matches[0] if matches else "Not found")
        elif choice == "4":
            student_id = input("Delete ID: ").strip()
            updated = [s for s in students if s["id"] != student_id]
            if len(updated) == len(students):
                print("Not found")
            else:
                students = updated
                save_students(students)
                print("Deleted")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
