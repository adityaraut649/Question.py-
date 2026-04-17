# Student Management System

Students = []

def add_student(Id, Name, Age):
    Students.append({'Id': Id, 'Name': Name, 'Age': Age})


def view_student():
    if not Students:
        print("No students found")
    else:
        for s in Students:
            print(s)


def update_student(Id, Name, Age):
    for s in Students:
        if s['Id'] == Id:
            s['Name'] = Name
            s['Age'] = Age
            print("Student updated")
            return
    print("Student not found")


def delete_student(Id):
    for i in range(len(Students)):
        if Students[i]['Id'] == Id:
            del Students[i]
            print("Student deleted")
            return
    print("Student not found")


def search_student(Id):
    for s in Students:
        if s['Id'] == Id:
            print("Found:", s)
            return s
    print("Student not found")
    return None


def main():
 
    while True:
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Id = input("Enter Student Id: ")
            Name = input("Enter Student Name: ")
            Age = input("Enter Student Age: ")
            add_student(Id, Name, Age)

        elif choice == "2":
            view_student()

        elif choice == "3":
            Id = input("Enter Student Id: ")
            Name = input("Enter Student Name: ")
            Age = input("Enter Student Age: ")
            update_student(Id, Name, Age)

        elif choice == "4":
            Id = input("Enter Student Id: ")
            delete_student(Id)

        elif choice == "5":
            Id = input("Enter Student Id: ")
            search_student(Id)

        elif choice == "6":
            print("Exit")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()