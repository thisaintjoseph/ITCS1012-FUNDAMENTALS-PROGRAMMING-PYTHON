import os

print("Student Information System!")
print("================================================\n")



student_records= {}

while True:
    print("SELECT FROM THE OPTIONS BELOW \nA- ADD INFORMATION \nB- SEARCH DATA \nC- SEARCH A RECORD \nD- DELETE A RECORD \nE- EDIT a Record \nF- EXIT ")
    

    choice = input("Your choice:  ").lower()

    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("------------------------------------")
        student_id = input("Input Key to search: ")
        

        first_name = input("Enter your first name: ").upper()
        last_name =  input("Enter your last name: ").upper()
        course =  input("Enter your course: ").upper()
        email =  input("Enter your email: ").upper()

        student_records= {student_id : [first_name, last_name, course, email] }
        print("DATA SAVED.")

        os.system('cls')
        continue

    elif choice == 'b' :
        for id, record in student_records.items():
            print(f"Student ID {id} in Student Record {record}")
            continue


    elif choice == 'c':
        os.system('cls')
        print("Search Student Record..")
        print("=======================================")
        
        for i in student_records[student_id]:
            search_id = input("Input Student ID: ").lower()


        for id in student_records.keys():
            if search_id in student_records.keys():
                print("Record Found :) ")
                for i in student_records[student_id]:
                    print(f"--{i}")
            else:
                print("NO RECORD FOUND :(")

        continue
    elif choice == 'd':
        os.system('cls')
        search_id = input("Input Student ID: ")
        print("DELETE EXISTING RECORD...")
        if search_id in student_records.keys():
                print("Record Found :) ")
                for i in student_records[student_id]:
                    print(f"--{i}")
                
                student_records.pop(search_id)
                print("RECORD DELETED :)")

        else:
                print("NO RECORD FOUND :(")

        continue
    elif choice == 'f':
        print("SYSTEM EXIT..")
        break
    else:
        print("\n INVALID CHOICE, please RE-ENTER YOUR CHOICE! ")



