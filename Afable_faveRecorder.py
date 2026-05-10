import openpyxl as josip
from datetime import datetime


workbook = josip.Workbook()
sheet = workbook.active
sheet.title = "Favorite People"


sheet.append(["ID", "First Name", "Last Name", "Birth Year", "Age"])


current_year = datetime.now().year


people_list = []

# Ask user for 3 people
for i in range(1, 4):
    print("Enter details for Person", i)
    fname = input("First Name: ")
    lname = input("Last Name: ")
    birth_year = int(input("Birth Year: "))
    age = current_year - birth_year
    person_id = i

  
    sheet.append([person_id, fname, lname, birth_year, age])

    
    people_list.append([person_id, fname, lname, birth_year, age])


workbook.save("favorite_people.xlsx")

print("\nData saved to favorite_people.xlsx\n")


print("=== Saved Records ===")
for person in people_list:
    print("ID:", person[0], 
          "First Name:", person[1], 
          "Last Name:", person[2], 
          "Birth Year:", person[3], 
          "Age:", person[4])
