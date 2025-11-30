

isDirty = True

while isDirty == True:
    confirm = input("Continue washing? (yes / no)? ").lower()

    if confirm == 'yes':
        print("continue washing...")
        continue

    elif confirm == 'no':
        print("Stopped washing..")
        break
    else:
        print("Invalid yah")
        continue


